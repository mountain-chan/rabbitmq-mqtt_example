import timeit

setup = """
import asyncio
import time
from urllib.parse import urlparse

from gmqtt import Client as MQTTClient

client = MQTTClient(client_id="pub-client-id", receive_maximum=24000)

async def main(broker_host, username, password):
    client.set_auth_credentials(username=username, password=password)
    await client.connect(broker_host)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    broker_address = "paho_mqtt://bootai:1234567aA@@localhost:1883"
    broker_url = urlparse(broker_address)
    loop.run_until_complete(main(broker_url.hostname, broker_url.username, broker_url.password))
"""

ex1 = """ 
for i in range(1000):
        client.publish(message_or_topic='TEST/T1', payload=str(i), qos=1, retain=True, message_expiry_interval=60)
"""

long = timeit.timeit(ex1, setup=setup, number=1)
print(long)
