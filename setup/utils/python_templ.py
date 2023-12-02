
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Provide Module Description
https://github.com/bndr/pipreqs
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
__author__ = ["Hiran Patel"]
__version__ = "1.0.0"
__module__ = "ModName"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# Imports
import argparse
import os
import logging
import sys
import subprocess

# Create a custom logger
log = logging.getLogger(__name__)
logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Parse input args
def parse_args():
    parser = argparse.ArgumentParser(description='Script description')
    # Positional Arguments
    parser.add_argument('argument_name',
                        help="argument description",
                        nargs='?',
                        const=0)

    # Optional Arguments
    parser.add_argument("-f", "--foo",
                        help="specify foo",
                        action='store_true')
    parser.add_argument("-b", "--bar",
                        help="specify bar",
                        metavar='BAR',
                        nargs=1)
    return parser.parse_args()

# main code 
def main():
    options = parse_args()
    if options.foo:
        subprocess.run(["echo", "bar"])
    if options.argument_name:
        print("Argument name: %s" % args.argument_name)
    if options.bar:
        print("Specified bar: %s" % args.bar)
    print("str % options")
    
if __name__ == "__main__":
    
    try:
        #print("\n".join(main(options)))
        main()
        log.info("Starting script")
    except Exception as e:
        log.exception("%s", e)
        sys.exit(1)
    sys.exit(0)
