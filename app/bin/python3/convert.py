#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from: https://stackoverflow.com/questions/33137741/fastest-way-to-convert-a-dicts-keys-values-from-bytes-to-str-in-python3

to convert python dict whose key and value is types to string
"""


def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    elif isinstance(data, dict):
        return dict(map(convert, data.items()))
    elif isinstance(data, tuple):
        return map(convert, data)
    return data


if __name__ == "__main__":
    original_dict = {b'a': b'Tom'}
    print(convert(original_dict))
