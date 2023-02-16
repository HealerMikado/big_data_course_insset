from pyflink.common import WatermarkStrategy, Encoder, Types
from pyflink.datastream import StreamExecutionEnvironment

from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types

import random
import time
import json
import logging
import sys
data=[
    {"account_id":1, "value":300},
    {"account_id":2, "value":300},
    {"account_id":3, "value":300},
    {"account_id":4, "value":300},
    {"account_id":5, "value":300},
    {"account_id":6, "value":300},
    {"account_id":7, "value":300},
    {"account_id":8, "value":300},
    {"account_id":9, "value":300},
    {"account_id":10, "value":300},
    {"account_id":11, "value":300},
]


def data_generation():
    data = []
    toggle = False
    for _ in range(100):

        account_id = random.randint(1,10)
        event = {
        "account_id" : account_id,
        "value" : round(random.uniform(0,500), 2),
        "timestamp" : time.time()+random.uniform(-5,5)
    }
        if account_id==9:
            if toggle :
                toggle = False
                event["value"] = round(random.uniform(500,100), 2)
            else :
                toggle = True
                event["value"] = round(random.random(), 2)
        data.append(event)
    return data

class FraudDetector(KeyedProcessFunction):

    def __init__(self):
        self.state = None

    def open(self, runtime_context: RuntimeContext):
        flag_descriptor = ValueStateDescriptor("flag", Types.BOOLEAN())
        self.state = runtime_context.get_state(flag_descriptor)

    def process_element(self, value, ctx: 'KeyedProcessFunction.Context'):
        yield f"!!! Alert !!! Account {value['account_id']} seems suspicious !"

class FraudDetectionJob :

    def main(self): 
        env = StreamExecutionEnvironment.get_execution_environment()
        env.set_parallelism(2)

        ds = env.from_collection(
        collection=data_generation())
        alert = ds.key_by(lambda trans : trans["account_id"])\
            .process(FraudDetector(), Types.STRING()).name("fraud-detector") \
            .print()
            

        env.execute("Fraud Detection");


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    fraud_detection_job =FraudDetectionJob() 
    fraud_detection_job.main()