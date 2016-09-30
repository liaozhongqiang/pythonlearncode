#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import hashlib
import base64


def hash_value(channel, code, companyid):
    md5 = hashlib.md5()
    s = channel + "&" + code + "&" + companyid
    md5.update(s.encode('utf-8'))
    b = md5.digest()
    re = ((b[3] & 0xFF) << 24) | ((b[2] & 0xFF) << 16) | ((b[1] & 0xFF) << 8) | (b[0] & 0xFF)
    print(re & 0xffffffff)


hash_value("12", "15889692432", "19000")
hash_value("12", "15889692432", "19000")
hash_value("12", "15889692432", "19000")