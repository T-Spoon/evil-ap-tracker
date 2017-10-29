#!/usr/bin/python

from scapy.all import Dot11, sniff

from datetime import datetime


INTERFACE = 'wlan0mon'
CTS_SUBTYPE = 12


def lfilter( packet ):
	return packet.haslayer( Dot11 ) and \
		packet.type == 1 and \
		packet.subtype == CTS_SUBTYPE


def onPacket( packet ):
	print "{0}\tCTS {1} ---> {2} [{3}]".format(
			datetime.now(),  packet[Dot11].addr2,
			packet[Dot11].addr1, packet[Dot11].addr3 )

sniff( iface = INTERFACE, lfilter = lfilter, prn = onPacket )
