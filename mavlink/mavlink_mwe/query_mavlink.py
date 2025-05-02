import argparse
from pymavlink import mavutil

def main():
    parser = argparse.ArgumentParser(prog="query_mavlink", description="Example of using pymavlink to read data")

    # Note this URL is non-standard and needs to be manually created as a "Mavlink endpoint" on the ROV.
    # See the README
    parser.add_argument("--mavlink-url", default='tcp:192.168.2.2:6777', help="Mavlink URI to connect to")

    args = parser.parse_args()

    connection = mavutil.mavlink_connection(args.mavlink_url)

    # Wait for the first heartbeat
    #   This sets the system and component ID of remote system for the link
    connection.wait_heartbeat()
    print("Heartbeat from system (system %u component %u)" % 
        (connection.target_system, connection.target_component))

    while True:
        # See https://mavlink.io/en/messages/
        # for list of all message types
        msg = connection.recv_match(type='HEARTBEAT', blocking=True)

        print(f"Got a heartbeat from device type {msg.type}, autopilot type {msg.autopilot} Mavlink version {msg.mavlink_version}")