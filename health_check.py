#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
import emails

if os.name != "nt":
    import fcntl
    import struct

if __name__ == "__main__":

    obj_Disk = psutil.disk_usage('/')

    performance={}

    mb_ram = psutil.virtual_memory().available >> 20

    performance['cpu'] = psutil.cpu_percent()
    performance['ram'] = mb_ram
    performance['disk'] = obj_Disk.percent * 100
    performance['localhost'] = socket.gethostbyname(socket.gethostname())

    for key in performance:
        print(f"{key}: {performance[key]}")