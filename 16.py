#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys
import collections
import functools
import operator

Packet = collections.namedtuple('Packet', ['version', 'type_id', 'subpackets', 'data'])

def decode(ch):
    mapping = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111',
    }

    return mapping[ch]


BITS = ''.join(decode(ch) for ch in input().strip())
BITS_pointer = 0


def readbit():
    global BITS, BITS_pointer
    res = BITS[BITS_pointer]
    BITS_pointer += 1
    return res


def readbits(k):
    s = ''
    for _ in range(k):
        s += readbit()
    return s


def bin_to_int(s):
    return int(s, base=2)


def parsePacket() -> Packet:
    ver = bin_to_int(readbits(3))
    tp = bin_to_int(readbits(3))

    if tp == 4:
        data = ''
        while True:
            stop_bit = readbit()
            data += readbits(4)

            if stop_bit == '0':
                break

        return Packet(ver, tp, [], bin_to_int(data))
    else:
        length_type_bit = readbit()

        subpackets = []
        
        if length_type_bit == '1':
            num_packets = bin_to_int(readbits(11))

            for i in range(num_packets):
                subpackets.append(parsePacket())
        else:
            total_len = bin_to_int(readbits(15))

            cur_pos = BITS_pointer
            while BITS_pointer != cur_pos + total_len:
                subpackets.append(parsePacket())

        return Packet(ver, tp, subpackets, None)

def total_versions(packet):
    print(packet)
    result = packet.version

    for subpacket in packet.subpackets:
        result += total_versions(subpacket)
    return result


def calculate(packet):
    if packet.type_id == 4:
        return packet.data

    f = None
    if packet.type_id == 0:
        f = operator.add
    elif packet.type_id == 1:
        f = operator.mul
    elif packet.type_id == 2:
        f = min
    elif packet.type_id == 3:
        f = max
    elif packet.type_id == 5:
        f = lambda x, y: int(x > y)
    elif packet.type_id == 6:
        f = lambda x, y: int(x < y)
    elif packet.type_id == 7:
        f = lambda x, y: x == y

    return functools.reduce(f, map(calculate, packet.subpackets))

packet = parsePacket()
print(total_versions(packet))
print(calculate(packet))
    
    
