import json
import random
import time
from kafka import KafkaProducer
from datetime import datetime, timedelta

KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "measurements"

# producer = KafkaProducer(
#    bootstrap_servers=KAFKA_BROKER,
#    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
# )


def simulate_measurement(base_value, variation):
    return round(base_value + random.uniform(-variation, variation), 2)


def generate_message():
    timestamp = (datetime.now() - timedelta(hours=1)).isoformat()
    message = {
        "MMXU": {
            "Vol": {
                "phsA": {
                    "mag": simulate_measurement(230.0, 5),
                    "ang": 0.0,
                    "q": "Good",
                    "t": timestamp,
                },
                "phsB": {
                    "mag": simulate_measurement(230.0, 5),
                    "ang": -120.0,
                    "q": "Good",
                    "t": timestamp,
                },
                "phsC": {
                    "mag": simulate_measurement(230.0, 5),
                    "ang": 120.0,
                    "q": "Good",
                    "t": timestamp,
                },
            },
            "A": {
                "phsA": {
                    "mag": simulate_measurement(100.0, 5),
                    "q": "Good",
                    "t": timestamp,
                },
                "phsB": {
                    "mag": simulate_measurement(95.0, 5),
                    "q": "Good",
                    "t": timestamp,
                },
                "phsC": {
                    "mag": simulate_measurement(98.0, 5),
                    "q": "Good",
                    "t": timestamp,
                },
            },
            "W": {
                "tot": {
                    "mag": simulate_measurement(50000.0, 1000),
                    "q": "Good",
                    "t": timestamp,
                }
            },
            "VAr": {
                "tot": {
                    "mag": simulate_measurement(30000.0, 1000),
                    "q": "Good",
                    "t": timestamp,
                }
            },
            "VA": {
                "tot": {
                    "mag": simulate_measurement(60000.0, 1000),
                    "q": "Good",
                    "t": timestamp,
                }
            },
            "PF": {
                "tot": {
                    "mag": simulate_measurement(0.85, 0.05),
                    "q": "Good",
                    "t": timestamp,
                }
            },
        }
    }
    return message


def main():
    for _ in range(1000):
        message = generate_message()
        print(message)
        # producer.send(TOPIC_NAME, value=message)
        time.sleep(1)


if __name__ == "__main__":
    main()
