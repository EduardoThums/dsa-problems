class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_lots = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if self.parking_lots[carType] == 0:
            return False

        self.parking_lots[carType] -= 1
        return True
