#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
An example from effective python, telling about consider generators instead
of list, item 16.
"""


def index_words_iter(text):
    """
    append change to yield?
    :param text:
    :return:
    """
    if text:
        yield 0
        for index, letter in enumerate(text):
            if letter == ' ':
                yield index + 1


def index_words(text):
    """
    original code
    :param text:
    :return:
    """
    result = []
    if text:
        result.append(0)
        for index, letter in enumerate(text):
            if letter == ' ':
                result.append(index + 1)
    return result


if __name__ == "__main__":
    test_string = "This is a book describing the story of King Author"

    res = index_words_iter(test_string)
    for item in res:
        print item

    print index_words(test_string)
