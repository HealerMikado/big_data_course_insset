from pyflink.common import WatermarkStrategy, Encoder, Types
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors.file_system import (FileSource, StreamFormat, FileSink,
                                                       OutputFileConfig, RollingPolicy)

from fraud_detector import FraudDetector
from transaction_source import TransactionSource
class FraudDetectionJob :

    def main(): 
        env = StreamExecutionEnvironment.get_execution_environment()

        transactions_src = TransactionSource()
        ds = env.add_source(transactions_src)
        alert = ds.key_by(lambda trans : trans["account_id"])\
            .process(FraudDetector()).name("fraud-detector") \
            .print()
            

        # alerts
        #     .addSink(new AlertSink())
        #     .name("send-alerts");

        env.execute("Fraud Detection");
