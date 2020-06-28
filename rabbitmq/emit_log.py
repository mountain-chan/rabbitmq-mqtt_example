import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

for i in range(10000):
    channel.basic_publish(exchange='logs', routing_key='', body="Log: " + str(i))
connection.close()


# i = 1
# while True:
#     channel.basic_publish(exchange='logs', routing_key='', body="Log: " + str(i))
#     print("Sent log: " + str(i))
#     i += 1
#     time.sleep(2)



