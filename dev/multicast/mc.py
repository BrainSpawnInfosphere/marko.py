#!/usr/bin/env python3
##############################################
# The MIT License (MIT)
# Copyright (c) 2018 Kevin Walchko
# see LICENSE for full details
##############################################
#
from colorama import Fore
import time
import sys
import traceback
import struct

from pymarko.mcsocket import MultiCastSocket


if len(sys.argv) != 2:
    print("Usage: ./mc.py message")
    exit(1)

msg = sys.argv[1]
msg = "gecko:"+ msg
msg = msg.encode("utf8")
mc = MultiCastSocket(group=('224.0.0.251', 5353), ttl=2, timeout=1)
print(">>", mc.info())

while True:
    try:
        mc.cast(msg)
        time.sleep(1)
        print(f"{Fore.YELLOW}<< beacon sent: {msg}{Fore.RESET}")
        # data, address = mc.recv()
        data, address = mc.recv_nb()
        if data is None:
            continue
        elif data[:5] != b"gecko":
            continue

        print(f"{Fore.GREEN}>> {data} from {Fore.CYAN}{address}{Fore.RESET}")

    except KeyboardInterrupt:
        print("ctrl-z")
        break
    except:
        traceback.print_exc()
        break
