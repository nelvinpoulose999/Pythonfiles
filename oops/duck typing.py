class Swift:
    def start(self):
        print('swift car start')
    def accelerate(self):
        print('swift car accelrate')
    def stop(self):
        print('swift car stop')
class Seltos:
    def start(self):
        print('seltos car start')
    def accelerate(self):
        print('seltos car accelrate')
    def stop(self):
        print('seltos car stop')
class BMW:
    def start(self):
        print('BMW car start')
    def accelerate(self):
        print('BMW car accelrate')
    def stop(self):
        print('BMW car stop')

class Person:
    def person(self,car):
        car.start()
        car.accelerate()
        car.stop()
sw=Swift()
p=Person()
p.person(sw)