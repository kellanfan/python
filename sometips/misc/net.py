# -*- coding: utf-8 -*-

import random
from netaddr import IPAddress, IPNetwork


def random_mac():
    mac = None
    MAC = [0x52, 0x56,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff)
    ]
    return ':'.join(map(lambda x: "%02x" % x, MAC))

def is_valid_address(address, version=4):
    if version == 6 and address.upper().startswith('FE80'):
        return False

    try:
        address = IPAddress(address, flags=1)
        if address.version != version:
            return False
        else:
            return True
    except Exception:
        return False

def get_valid_address(address):
    try:
        return IPAddress(address, flags=1)
    except:
        return None

def is_valid_network(network, version=4):
    try:
        network = IPNetwork(network, flags=1)
        if network.version != version:
            return False
        else:
            if network.prefixlen in [31, 32, 127, 128]:
                return False
            else:
                return True
    except:
        return False

def get_valid_network(network):
    try:
        return IPNetwork(network, flags=1)
    except:
        return None