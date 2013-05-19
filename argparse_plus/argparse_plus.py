#!/usr/bin/env python

import argparse
import sys

class ArgumentParserPlus(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        if 'epilog' in kwargs:
            kwargs['epilog'] = kwargs['epilog'] % {'prog' : sys.argv[0]}
        if 'formatter_class' not in kwargs:
            kwargs['formatter_class'] = argparse.RawDescriptionHelpFormatter
        super(ArgumentParserPlus, self).__init__(*args, **kwargs)

