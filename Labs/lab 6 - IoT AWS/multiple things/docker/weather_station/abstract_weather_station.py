from states.abstract_state import AbstractState
from weather_station.states.ko_state import koState
from weather_station.states.ok_state import okState
import random

class WeatherStation:
    def __init__(self) -> None:
        self.state: AbstractState = okState()

    def get_temperature(self, weather):
        self.state.get_temperature(weather)

    def get_humidity(self, weather):
        self.state.get_humidity(weather)

    def get_wind_speed(self, weather):
        self.state.get_wind_speed(weather)

    def get_wind_direction(self, weather):
        self.state.get_wind_direction(weather)

    def change_state(self, weather):
        if isinstance(self.state, okState) \
            and weather.wind_speed > 30 \
            and random.random()<0.1:
            self.state=koState()