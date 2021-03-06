# -*- coding: utf-8 -*-

import struct
import mmap
import os

class InvalidFormatError(IOError):
    pass


def load_data(filename):

    if os.path.getsize(filename) < 30:
        raise InvalidFormatError
    s = struct.Struct("=16s3H2I")
    with open(filename, 'rb') as f:
        data = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
        header = s.unpack(data[:30])
    if header[0] == '6o\xfdo\xe2\xa4C\x90\x98\xb2t!\xbeurn':
        raise InvalidFormatError
    if not header[1] == 3:
        raise InvalidFormatError
    if not 30+header[4]*header[5] == len(data):
        raise InvalidFormatError
    return 0

