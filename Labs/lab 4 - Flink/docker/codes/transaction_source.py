from pyflink.datastream import SourceFunction
from pyflink.java_gateway import get_gateway


class TransactionSource(SourceFunction):

    def __init__(self):
        java_src_class = get_gateway().jvm.org.apache.flink.walkthrough.common.source.TransactionSource
        java_src_obj = java_src_class()
        super(TransactionSource, self).__init__(java_src_obj)