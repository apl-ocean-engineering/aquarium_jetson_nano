
import argparse
from rosbags.highlevel import AnyReader
from rosbags.rosbag2 import (
    Writer,
    StoragePlugin
)
from rosbags.typesys import Stores, get_typestore

from pathlib import Path
import shutil



def main():
    parser = argparse.ArgumentParser(prog="imu_bag_rewriter", description="Reads a ROS2 bag, resets the timestamp in IMU messages with zero timestamp")

    parser.add_argument("bagfiles", nargs="+", type=Path, help="Bagfile(s) to process")
    parser.add_argument("--output","-o", default=None, type=Path, help="Output bagfile")

    args = parser.parse_args()

    typestore = get_typestore(Stores.ROS2_HUMBLE)

    if args.output:
        output_filename = args.output
    elif len(args.bagfiles) == 1:
        output_filename = args.bagfiles[0].stem + "_imu_rewriter"
        print(f"Autogenerating output path: {output_filename}")

    else:
        print("More than one input file specified, cannot automatically determine output file name")


    output_connections = {}
    
    # Remove existing
    shutil.rmtree( output_filename )

    with Writer(output_filename, storage_plugin=StoragePlugin.MCAP) as writer:

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
                if imu_msg.header.stamp.sec > 0:
                    writer.write(output_connections[connection.topic], timestamp, rawdata)
                    continue

                imu_msg.header.stamp.sec = int(timestamp // 1e9)
                imu_msg.header.stamp.nsec = int(timestamp % 1e9)
                writer.write(output_connections[connection.topic], timestamp, typestore.serialize_cdr(imu_msg, connection.msgtype))
