
from states.abstract_state import AbstractState


class okState(AbstractState):
    @staticmethod
    def get_temperature(weather):
        pass

    @staticmethod
    def get_humidity(weather):
        pass

    @staticmethod
    def get_wind_speed(weather):
        pass

    @staticmethod
    def get_wind_direction(weather):
        pass