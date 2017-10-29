#!/usr/bin/python

from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp, hexdump

NET_SSID = 'yoloSSID'
INTERFACE = 'wlan0mon'

dot11 = Dot11(
		type = 0,
		subtype = 8,
		addr1 = 'ff:ff:ff:ff:ff:ff',
		addr2 = '22:22:22:22:22:22',
		addr3 = '33:33:33:33:33:33' )

beacon =  Dot11Beacon( cap = 'ESS+privacy' )

essid = Dot11Elt( ID = 'SSID', info = NET_SSID, len = len( NET_SSID ) )

rsn = Dot11Elt( ID = 'RSNinfo', info = (
'\x01\x00'
'\x00\x0f\xac\x02'
'\x02\x00'
'\x00\x0f\xac\x04'
'\x00\x0f\xac\x02'
'\x01\x00'
'\x00\x0f\xac\x02'
'\x00\x00' ) )

frame = RadioTap() / dot11 / beacon / essid / rsn

frame.show()

print( "\nHexdump of frame:" )
hexdump( frame )

raw_input( "\nPress enter to start\n" )

sendp( frame, iface = INTERFACE, inter = 0.100, loop = 1 )
