#!/usr/bin/python
# -*- coding: utf-8 -*-


def text_remove_duplicate(original_file, processed_file):
    file_buffer = []
    with open(original_file, "r") as f:
        for line in f.readlines():
            if line not in file_buffer:
                file_buffer.append(line)
    with open(processed_file, "w") as f:
        f.writelines(file_buffer)

text_remove_duplicate("a.txt", "b.txt")