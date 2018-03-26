#!/usr/bin/env python

from . import _version

import argparse
import sys

def parse_args(args):
    parser = argparse.ArgumentParser(
        prog = "iotraven",
        description = "Pull energy meter data from a RaVEn USB device and publish to an AWS IoT MQTT topic"
    )

    parser.add_argument('-V', '--version', action='version',
            version='%(prog)s {version}'.format(version=_version.__version__))

def exit_if_unsupported_python():
    if sys.version_info.major == 2 and sys.version_info.minor < 7:
        print("iotraven requires Python 2.7 or higher")
        sys.exit(1)

def main(cli_args):
    try:
        exit_if_unsupported_python()

        args = parse_args(cli_args)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    cli_args = sys.argv[1:]
    main(cli_args)
