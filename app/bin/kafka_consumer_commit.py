#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import base64
import zlib
import time
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition
from kafka import OffsetAndMetadata


def parse_payload(value):
    print(value)
    return value


if __name__ == "__main__":
    topic = "test"
    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        group_id='test_2017-0905',
        auto_offset_reset='earliest',
        enable_auto_commit=False)
    consumer.subscribe(topic)
    partitions = consumer.partitions_for_topic(topic)

    topicpartitions = [
        TopicPartition(topic, partitionId) for partitionId in partitions]

    # for tp in topicpartitions:
    #     consumer.commit({tp: OffsetAndMetadata(1000, None)})

    for message in consumer:
        print message.partition, message.offset
        # commit offset manually
        topic_partition = TopicPartition(topic, message.partition)
        offset_meterdata = OffsetAndMetadata(450, None)
        offset = {topic_partition: offset_meterdata}

        consumer.commit(offset)
        print message.offset
        time.sleep(1)
        # break
        # print(message.value)
        # payload = parse_payload(message.value)
        # print(payload)
