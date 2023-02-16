from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types
from alert import Alert

class FraudDetector(KeyedProcessFunction):

    def __init__(self):
        self.state = None

    def open(self, runtime_context: RuntimeContext):
        flag_descriptor = ValueStateDescriptor("flag", Types.BOOLEAN()())
        self.state = runtime_context.get_state(flag_descriptor)

    def process_element(self, value, ctx: 'KeyedProcessFunction.Context'):
        alert = Alert(value["account_id"])
        yield alert
