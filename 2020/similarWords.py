from abc import ABC, abstractmethod


class VehicleSize(Enum):
    small, compact, large = 1,2,3


class Vehicle(ABC):
    def __init__(self, licencePlate, vehichleSize, spotSize):
        self.licencePlate = licencePlate
        self.vehicleSize = vehichleSize
        self.spotSize = spotSize
        self.parked = False

    def clearSpot(self):
        self.parked = False
        self.spotSize = -1

    def takeSpot(self, num):
        self.spotSize = num
        self.parked = True

    @abstractmethod
    def can_fit_in_spot(self):
        pass


class Car(Vehicle):
    def __init__(self, licencePlate,vehicleSize,spotSize):
        super(Car,self).__init__(licencePlate,vehicleSize,spotSize)

    def can_fit_in_spot(self):
        return True


class OperationalStatus(Enum):
    Running = 0
    UnderMaintenance = 1
    Closed = 2


class Parking(object):
    def __init__(self, location, size, ):
        self.location= location
        self.size = size
