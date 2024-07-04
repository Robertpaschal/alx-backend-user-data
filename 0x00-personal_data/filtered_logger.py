#!/usr/bin/env python3
"""
This module contains a log filter function
"""
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str,
        seperator: str) -> str:
    """
    Function that returns the log message obfuscated

    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field
            will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
            is separating all fields in the log line (message)

    returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = '|'.join([f'(?<={field}=)[^{seperator}]+' for field in fields])
    return re.sub(pattern, redaction, message)
