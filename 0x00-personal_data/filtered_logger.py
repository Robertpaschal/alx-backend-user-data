#!/usr/bin/env python3
"""
This module contains a log filter function
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, seperator: str) -> str:
    """Function that returns the log message obfuscated"""
    pattern = '|'.join([f'(?<={field}=)[^{seperator}]+' for field in fields])
    return re.sub(pattern, redaction, message)
