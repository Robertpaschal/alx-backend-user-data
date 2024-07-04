#!/usr/bin/env python3
"""
This module contains a log filter function
"""
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
def filter_datum(
        fields: List[str], redaction: str, message: str,
        seperator: str) -> str:
    """
    Function that returns the log message obfuscated
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, seperator), replace(redaction), message)
