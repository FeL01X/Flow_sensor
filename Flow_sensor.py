# Project zero: Flow-sensor

## imports
import numpy as np
import matplotlib.pyplot as plt

## 
class Sensor:
    def __init__(self,sensor_id):
        self.power = False
        self.calibration_coefficient = 5
        self.id = sensor_id
        print(f"Initiallization of the sensor: {self.id}")
        self.memory = np.zeros(100)

    def turn_on(self):
        self.power = True
        print(f"Sensor is activated!")

    def read_memory(self):
        print(f"Reading Memory of sensor {self.id} ... \n Data Format: time:value")
        print(15*"=====")
        print(f"{self.memory}")
        print(15*"=====")

    def record_data(self):
        if self.power:
            pass




ss1 = Sensor(1)
ss1.turn_on()
ss1.read_memory()