import time


class TrackVehicle:
    def change_direction(self, left, on):
        print('Tracks: ', left, on)


class WheeledVehicle:
    def change_direction(self, left, on):
        print('Wheels: ', left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)  # when calling from a function, do not add self there
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheel = Vehicle(WheeledVehicle())
wheel.turn(True)

track = Vehicle(TrackVehicle())
track.turn(False)
