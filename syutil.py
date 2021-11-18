"""Utility module
"""


def to_num(arg):
    """String to Float or Integer, otherwise no conversion

        arg         return
        "10.3"  ->  10.3 (float)
        "7"     ->  7 (int)
        "abc"   ->  "abc" (no conversion)

    Args:
        arg (string): number expressed as str

    Returns:
        float, int, or same as arg: number expressed as actual type
    """

    if type(arg) is not str:
        return arg

    if arg.isdecimal():
        return int(arg)
    else:
        try:
            return float(arg)
        except ValueError:
            return arg
