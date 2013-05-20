

Usage
-----
Automatically resolve `%(prog)s` to name of python file in `epilog`.

::
    epilog = """

    Examples:
    %(prog)s --verbose --conf=dev.conf
    """
    argp = ArgumentParserPlus(epilog=epilog)


 
