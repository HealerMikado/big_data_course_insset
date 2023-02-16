from abc import ABC, abstractmethod


class AbstractState(ABC):

    @abstractmethod
    @staticmethod
    def get_temperature(weather):
        pass

    @abstractmethod
    @staticmethod
    def get_humidity(weather):
        pass

    @abstractmethod
    @staticmethod
    def get_wind_speed(weather):
        pass

    @abstractmethod
    @staticmethod
    def get_wind_direction(weather):
        pass