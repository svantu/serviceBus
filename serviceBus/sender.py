from conf import *
from azure.servicebus.control_client import ServiceBusService
from azure.servicebus import QueueClient, Message
import os, json, time
from threading import Timer


q_client = QueueClient.from_connection_string(conn_str, q_name)
line_count = 0
# t1 = time.time()
msg_count =0

def sendmsg(m):
    q_client.send(msg)

with open("patient.ndjson") as f:
    for line in f:
        # line_count += 1
        s = json.loads(line)
        msg = Message(s)
        if msg_count == 0:
            t1 =  time.time() * 1000
        # sendmsg(msg)
        Timer(0,sendmsg,(msg,)).start()
        msg_count = msg_count + 1
        if msg_count == 15:
            t2 =  time.time() * 1000
            print('Sent all messages ', t2 - t1)
            break
        # print('Sent ', msg)
# print(file_name, 'has', line_count, 'records and took', time.time() - t, 'seconds to get uploaded into ServiceBus')

