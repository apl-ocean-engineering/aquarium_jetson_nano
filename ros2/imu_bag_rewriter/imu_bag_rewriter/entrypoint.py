
import argparse
from rosbags.highlevel import AnyReader
from rosbags.rosbag2 import (
    Writer,
    StoragePlugin
)
from rosbags.typesys import Stores, get_typestore

from pathlib import Path
import shutil
import pandas as pd
from sklearn import linear_model
import tqdm



def main():
    parser = argparse.ArgumentParser(prog="imu_bag_rewriter", description="Reads a ROS2 bag, resets the timestamp in IMU messages with zero timestamp")

    parser.add_argument("bagfiles", nargs="+", type=Path, help="Bagfile(s) to process")
    parser.add_argument("--output","-o", default=None, type=Path, help="Output bagfile")

    args = parser.parse_args()

    typestore = get_typestore(Stores.ROS2_HUMBLE)

    if args.output:
        output_filename = args.output
    elif len(args.bagfiles) == 1:
        output_filename = Path(args.bagfiles[0].stem + "_imu_rewriter")
        print(f"Autogenerating output path: {output_filename}")

    else:
        print("More than one input file specified, cannot automatically determine output file name")

    use_simple_method = True


    imu_data = []
    bag_time_data = []

    # First, analysis pass
    seq = 0
    with AnyReader(args.bagfiles, default_typestore=typestore) as reader:
    
        connections = [c for c in reader.connections if c.msgtype == "sensor_msgs/msg/Imu"]

        for connection, timestamp, rawdata in tqdm.tqdm(reader.messages(connections=connections), total=reader.message_count):

            imu_msg = typestore.deserialize_cdr(rawdata, connection.msgtype)
            if imu_msg.header.stamp.sec > 0:

                imu_data.append( { 'bag_ts': timestamp,
                                    'header_ts_sec': imu_msg.header.stamp.sec,
                                    'header_ts_nanosec': imu_msg.header.stamp.nanosec})

            bag_time_data.append({ 'bag_ts': timestamp, 'seq': seq})
            seq += 1


    bag_time_frame = pd.DataFrame(bag_time_data)
    print(f"Loaded {bag_time_frame.size} bag timestamps")
    reg = linear_model.LinearRegression()
    reg.fit(bag_time_frame[['seq']], bag_time_frame[['bag_ts']])
    r2_score = reg.score(bag_time_frame[['seq']], bag_time_frame[['bag_ts']])
    print(f"R-squared value: {r2_score}")

    print(reg.coef_)
    bag_ts_dt = reg.coef_[0][0]
    bag_ts_offset = bag_time_frame['bag_ts'][0]


    if len(imu_data) == 0:
        ## Use simple method

        print("No IMU messages have header timestamps, just copying bag timestamps")

        # The actual data time will be earlier than the bagfile timestamp
        # However, we have only anecdotal evidence
        #
        # This value taken from a short bagfile with the "fixed" driver
        # And both cameras
        bag_ts_to_header_stamp_fudge_ns = 750000
        print(f"Using fudge value of {bag_ts_to_header_stamp_fudge_ns} ns")

        output_connections = {}
        
        imu_msg_count = 0

        # Remove existing
        if output_filename.exists():
            shutil.rmtree( output_filename )
        with Writer(output_filename, storage_plugin=StoragePlugin.MCAP) as writer:

            with AnyReader(args.bagfiles, default_typestore=typestore) as reader:
            
                for connection, timestamp, rawdata in tqdm.tqdm(reader.messages(), total=reader.message_count):

                    if connection.topic not in output_connections:
                        print(f"Adding connection for topic {connection.topic}")
                        output_connections[connection.topic] = writer.add_connection(connection.topic, connection.msgtype)

                    if connection.msgtype != 'sensor_msgs/msg/Imu':
                        writer.write(output_connections[connection.topic], timestamp, rawdata)
                        continue

                    # Else, actually parse the message
                    imu_msg = typestore.deserialize_cdr(rawdata, connection.msgtype)

                    adjusted_ts = bag_ts_offset + (bag_ts_dt*imu_msg_count) - bag_ts_to_header_stamp_fudge_ns

                    imu_msg.header.stamp.sec = int(adjusted_ts // 1e9)
                    imu_msg.header.stamp.nanosec = int(adjusted_ts % 1e9)

                    writer.write(output_connections[connection.topic], timestamp, typestore.serialize_cdr(imu_msg, connection.msgtype))

                    imu_msg_count += 1


    else:
        # Have _some_ IMU timestamps, do more complex analysis

        imu_frame = pd.DataFrame(imu_data)
 
        imu_frame.drop_duplicates(subset=['header_ts_sec','header_ts_nanosec'], keep='first', inplace=True)
        imu_frame['header_ts'] = 1000000000*imu_frame.header_ts_sec + imu_frame.header_ts_nanosec

        imu_frame['bag_delay'] = imu_frame.bag_ts - imu_frame.header_ts

        print(f"Loaded {imu_frame.size} non-zero IMU timestamps")
        print(imu_frame.head())

        mean_delay = imu_frame.bag_delay.mean()
        delay_dev = imu_frame.bag_delay.std()
        print(f"Bag time lags header time by {mean_delay} ns, stddev {delay_dev}")



        output_connections = {}
        
        # Remove existing
        if output_filename.exists():
            shutil.rmtree( output_filename )
        with Writer(output_filename, storage_plugin=StoragePlugin.MCAP) as writer:

            seq = 0
            with AnyReader(args.bagfiles, default_typestore=typestore) as reader:
            
                for connection, timestamp, rawdata in reader.messages():

                    if connection.topic not in output_connections:
                        print(f"Adding connection for topic {connection.topic}")
                        output_connections[connection.topic] = writer.add_connection(connection.topic, connection.msgtype)

                    if connection.msgtype != 'sensor_msgs/msg/Imu':
                        writer.write(output_connections[connection.topic], timestamp, rawdata)
                        continue

                    # Else, actually parse the message
                    imu_msg = typestore.deserialize_cdr(rawdata, connection.msgtype)

                    adjusted_ts = (seq * bag_ts_dt) + bag_ts_offset - mean_delay

                    imu_msg.header.stamp.sec = int(adjusted_ts // 1e9)
                    imu_msg.header.stamp.nanosec = int(adjusted_ts % 1e9)


                    print(f"{seq} {imu_msg.header.stamp.sec} {imu_msg.header.stamp.nanosec}")

                    writer.write(output_connections[connection.topic], timestamp, typestore.serialize_cdr(imu_msg, connection.msgtype))

                    seq+=1
