import sys
from kafka import KafkaConsumer


def consume_messages(broker, topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[broker],
        auto_offset_reset="earliest",
        #group_id="my-group",
        value_deserializer=lambda x: x.decode("utf-8"),
    )

    try:
        for message in consumer:
            print(message.key, message.value)
            #print(message.value)
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        consumer.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python consumer.py <broker> <topic>")
        sys.exit(1)
    
    broker = sys.argv[1]
    topic = sys.argv[2]

    consume_messages(broker, topic)

