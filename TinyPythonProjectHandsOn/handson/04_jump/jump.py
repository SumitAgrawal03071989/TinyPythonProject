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

    parser.add_argument('input_code',
                        metavar='input_code',
                        help='String to enctrypt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    watch_dict = {'1':'9','2':'8','3':'7','4':'6','5':'0','6':'4','7':'3','8':'2','9':'1','0':'5'}
    args = get_args()
    input_code = args.input_code

    output_code = "";


    for word in input_code:
        if(word in watch_dict):
            output_code = output_code + watch_dict.get(word)
            continue

        output_code = output_code + word

    #print(f'input_code = "{input_code}"')
    print(output_code)
# --------------------------------------------------
if __name__ == '__main__':
    main()
