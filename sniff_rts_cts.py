#!/usr/bin/python

from scapy.all import Dot11, sniff
INTERFACE = 'wlan0'

DST_ADDR = '94:94:26:06:49:60'
SRC_ADDR = '22:22:22:22:22:22'

def packetHandler( packet ):
    subtypes = (11, 12)
    if packet.haslayer( Dot11 ) and packet.type == 1 and packet.subtype in subtypes:
        packet.summary()

sniff( iface = INTERFACE, prn = packetHandler )
