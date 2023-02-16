import json
import logging
import sys

from pyflink.datastream import StreamExecutionEnvironment


def process_json_data():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)

    # define the source
    ds = env.from_collection(
        collection=[
            (1, '{"name": "Flink", "tel": 123, "addr": {"country": "Germany", "city": "Berlin"}}'),
            (2, '{"name": "hello", "tel": 135, "addr": {"country": "China", "city": "Shanghai"}}'),
            (3, '{"name": "world", "tel": 124, "addr": {"country": "USA", "city": "NewYork"}}'),
            (4, '{"name": "PyFlink", "tel": 32, "addr": {"country": "China", "city": "Hangzhou"}}')]
    )

    def update_tel(data):
        # TODO add the phone prefix to each phone a tuple (id, {json})
        phone_prefix = {
            "Germany:" : "+49",
            "China:" : "+86",
            "USA:" :"+1"
        }
        return ...

    def filter_by_country(data):
        #TODO return true if country == China

    #TODO : update the phone number and filter by country==China
    ds.

    ds.print()
    # submit for execution
    env.execute()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")

    process_json_data()