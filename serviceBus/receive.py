from azure.servicebus import ServiceBusClient, QueueClient, Message
from conf import *
from time import *
import time

q_client = QueueClient.from_connection_string(conn_str, q_name)
msg_count = 0
with q_client.get_receiver() as q_receiver:
    
     while msg_count != MSG_COUNT:
        #print('before getmessage') 
        msgs = q_receiver.fetch_next(timeout=3)
        #print('after getmessage') 
        # sleep(0.5)
        
        for msg in msgs:
            if msg_count == 0:
                t1 =  time.time() * 1000
            # print(msg)
            msg_count = msg_count + 1
            if msg_count == MSG_COUNT:
                t2 =  time.time() * 1000
                print('Recevied all messages ', t2 - t1)
                break
print(' NUMBER of MESSAGES RECEIVED ' , msg_count)
print('MESSAGES RECEIVED/CAN BE RECEIVED IN ONE SECOND ', (msg_count * 1000)/(t2 - t1))
