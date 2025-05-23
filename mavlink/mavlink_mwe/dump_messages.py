"""
Read a tlog file and dump all messages of a given type(s) to stdout.

Example usage:
    python dump_messages.py --types DISTANCE_SENSOR 00128-2025-01-28_17-54-56.tlog
"""

import argparse
from pymavlink import mavutil

def main():
    parser = argparse.ArgumentParser(prog="dump_messages", description="Read messages from a tlog file")

    # See https://mavlink.io/en/messages/ for a list of all message types
    parser.add_argument("--types", default=None, help="Comma-separated list of types, default is all types")
    parser.add_argument('path', help="Path to tlog file")

    args = parser.parse_args()

    types = args.types.split(",") if args.types else None

    connection = mavutil.mavlink_connection(args.path)

    while True:
        msg = connection.recv_match(type=types, blocking=False)

        if not msg:
            print("No more messages of the selected type(s)")
            return

        # The message type
        msg_type = msg.get_type()

        # The message source
        system_id = msg.get_srcSystem()
        component_id = msg.get_srcComponent()

        # Time that the message was written to the tlog file
        timestamp = getattr(msg, '_timestamp', 0.0)

        print(f"Message of {msg_type} received at {timestamp}, sent by {system_id, component_id}")


if __name__ == '__main__':
    main()
