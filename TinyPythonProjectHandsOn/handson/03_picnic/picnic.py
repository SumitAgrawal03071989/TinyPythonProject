#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument("--sorted", "-s",  required=False, action='store_true', help="pass this as true if you need your items sorted", dest="sorted")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    list_size = len(items)

    if args.sorted:
        items.sort()

    if list_size == 1:
        print(f"You are bringing {items[0]}.")
    elif list_size == 2:
        print(f"You are bringing {items[0]} and {items[1]}.")
    elif list_size > 2:
        and_csv = ", ".join(items[0:list_size-1])
        print(f"You are bringing {and_csv}, and {items[list_size-1]}.")

# --------------------------------------------------
if __name__ == '__main__':
    main()
