#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
some method to decompress and parse tar.bz2 or gzip file with out cache them
on disk.

such as, an tar.bz2 file download with requests could be decompressed before
write it to disk, which will save IO read and write. This helps when the IO
load is heavy.
"""
import StringIO
import bz2
import tarfile
import requests
from io import BytesIO
import gzip


url = "www.google.com"
filename = "res_test.csv"


def decompress_tar_bz2_from_net(url, filename):
    """
    decompress the tar.bz2 format file in memory, instead of buffer it on disk
    and then decompress.
    :param url:
    :param filename:
    :return:
    """
    fileobj = BytesIO(requests.get(url).content)
    contents = tarfile.open(fileobj=fileobj).extractfile(filename).read()
    return contents


def parse_tar_bz2(bz2_filename=None, content_filename=None, mode="r:*"):
    """
    parse tar.bz2 file content in memory
    :param bz2_filename: tar.bz2 file to decompress, contain directory
    :param content_filename: the file name of the content of tar.bz2 file
    :param mode: mode to open file, r:bz2 for bz2 file, r:* is more compatible
    such as gzip file
    :return: content of file
    """
    file_obj = tarfile.open(bz2_filename, mode)
    content = file_obj.extractfile(content_filename).read()
    file_obj.close()
    return content


# test to handle tar.bz2 file with io.BytesIO
with open("/app/tmp/res_test.tar.bz2", "rb") as f:
    content = f.read()
    compressedFile = BytesIO(content)
    tf = tarfile.open(fileobj=compressedFile)
    csvfile = tf.extractfile('res_test.csv').read()
    print csvfile


# handle gzip file
with open("/app/tmp/res_test.tar.bz2", "rb") as f:
    content = f.read()
    compressedFile = StringIO.StringIO(content)
    decompressedFile = bz2.BZ2File(compressedFile.buf.encode("utf8"))
    print decompressedFile
    decompressedFile = gzip.GzipFile(fileobj=compressedFile)
    compressedFile.seek(0)

    with open("/app/tmp/decompress_test", 'w') as outfile:
        outfile.write(decompressedFile)


# handle bz2 file
with bz2.BZ2File("/app/tmp/res_test.tar.bz2", "r") as f:
    content = f.read()
    # content = f.readlines()
    with open("/app/tmp/res_test_01.csv", "w") as f_csv:
        f_csv.write(content)
    print content
