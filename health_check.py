#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
import emails
import sys

def alert_needed(stats):
    # send alert if any of the alerts are over the threshold
    alert = False
    subject_line = []

    if stats['cpu'] > 80:
        alert = True
        subject_line.append('Error - CPU usage is over 80%')

    if stats['ram'] < 500:
        alert = True
        subject_line.append('Error - Available memory is less than 500MB')

    if stats['disk'] < 20:
        alert = True
        subject_line.append('Error - Available disk space is less than 20%')

    if stats['localhost'] != '127.0.0.1':
        alert = True
        subject_line.append('Error - localhost cannot be resolved to 127.0.0.1')
    
    return alert, subject_line

if __name__ == "__main__":

    performance={}
    obj_disk = psutil.disk_usage('/')
    mb_ram = psutil.virtual_memory().available >> 20 # bitwise shift (I don't understand this yet)

    performance['cpu'] = psutil.cpu_percent()
    performance['ram'] = mb_ram
    performance['disk'] = obj_disk.percent * 100
    performance['localhost'] = socket.gethostbyname(socket.gethostname())

    prob_detected, details = alert_needed(performance)

    if prob_detected:
        subject_line = details[0]
        from_user="automation@example.com"
        username="student-00-dd910962cda2@example.com"

        body="Please check your system and resolve the issue as soon as possible."
        msg = emails.generate(from_user,username,subject_line,body)
        #print(msg)
        emails.send(msg)

    #for key in performance:
        #print(f"{key}: {performance[key]}")