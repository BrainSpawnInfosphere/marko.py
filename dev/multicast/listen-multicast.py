#!/usr/bin/env python3
##############################################
# The MIT License (MIT)
# Copyright (c) 2018 Kevin Walchko
# see LICENSE for full details
##############################################
# Listens to multicast messages on network. Most of the data will be binary
# since this can't decode it, but there is typically some strings in each
# message to give you an idea about them.
# 
# https://pymotw.com/2/socket/multicast.html
#
import traceback
from pymarko.mcsocket import MultiCastSocket

mc = MultiCastSocket(group=('224.0.0.251', 5353), ttl=2, timeout=1)
print(">>", mc.info())

while True:
    try:
        data, address = mc.recv()
        # data, address = mc.recv_nb()
        if data is None:
            continue

        print(">> {} from {}".format(data, address))

    except KeyboardInterrupt:
        print("ctrl-z")
        break
    except:
        traceback.print_exc()
        break
