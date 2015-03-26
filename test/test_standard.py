# coding: utf-8

import pytest
import gsm0338

def decode_gsm(message):
    lines = open('GSM0338.txt').read().split('\n')
    parsed = [l[2:].split('\t') for l in lines if l and not l.startswith('#')]
    key = dict([(a, chr(int(b, 0))) for a,b,c,d in parsed])
    done = ''.join([key.get(x, '') for x in seq(message)])
    return done.replace('@', '')

@pytest.fixture
def codec():
    return gsm0338.Codec()

def test_standard_compliance(codec):
    """ Proove that codec follows unicode standard using unicode mapping source.
    http://unicode.org/Public/MAPPINGS/ETSI/GSM0338.TXT
    """
    assert ...
