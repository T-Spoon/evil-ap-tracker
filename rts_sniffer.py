#!/usr/bin/python

from scapy.all import Dot11, sniff

from datetime import datetime

INTERFACE = 'wlan0mon'
RTS_SUBTYPE = 11
TARGET_STATION = '40:e3:d6:3e:2f:81'


def lfilter( packet ):
	return packet.haslayer( Dot11 ) and \
		packet.type == 1 and \
		packet.subtype == RTS_SUBTYPE


def onPacket( packet ):
	print "{0}\tRTS {1} ---> {2} {3} [{4}]".format(
			datetime.now(),  packet[Dot11].addr2,
			packet[Dot11].addr1, packet[Dot11].ID,
			packet[Dot11].addr3 )

sniff( iface = INTERFACE, lfilter = lfilter, prn = onPacket )
