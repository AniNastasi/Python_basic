# # 1
# from time import sleep
#
# class TrafficLight:
#     __color = ['red', 'yellow', 'green']
#
#     def running(self):
#
#         for i, el in enumerate (TrafficLight.__color, 0):
#             print(f'Traffic light color is \n' f'{el}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(20)
#
# TrafficLight = TrafficLight()
# TrafficLight.running()
#
# # 2
# class Road:
#     def __init__(self, _length, _width):
#         self._l = _length
#         self._w = _width
#
# class Mass(Road):
#     def __init__(self, _length, _width, mass, depth):
#         super().__init__(_length, _width)
#         self.m = mass
#         self.d = depth
#
#     def mass(self):
#         return self._l * self._w * self.m * self.d
#
# road1 = Mass(20, 5000, 25, 5)
# print(f'needed mass of asphalt to build road #1 (in kg) is: {road1.mass()}')
#
# # 3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#
# W1 = Position('Dmitri', 'Karamazov', 'carouse', 50000, 10000)
# print(W1.get_full_name())
# print(W1.position)
# print(W1.get_total_income())
#
# # 4
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('The car started')
#
#     def stop(self):
#         print('The car stopped')
#
#     def turn_left(self):
#         print('The car turned to the left')
#
#     def turn_right(self):
#         print('The car turned to the right')
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police, show_speed):
#         Car.__init__(self, speed, color, name, is_police)
#         self.show_speed = show_speed
#         print(f'Current speed of the town car {self.name} is {self.show_speed}')
#         if self.show_speed > 60:
#             print('!!! The speed exceeded the allowed value \n')
#         else:
#             print('The car goes within the allowed value \n')
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police, show_speed):
#         Car.__init__(self, speed, color, name, is_police)
#         self.show_speed = show_speed
#         print(f'Current speed of the work car {self.name} is {self.show_speed}')
#
#         if self.is_police == True:
#             print('The car goes within the allowed value \n')
#         elif self.show_speed > 40:
#             print('!!! The speed exceeded the allowed value \n')
#
# car1 = TownCar(120, 'black', 'VolksWagen', False, 59)
# car2 = TownCar(100, 'white', 'BMW', False, 100)
# car3 = WorkCar(60, 'gray', 'Niva', False, 45)
# car4 = WorkCar(200, 'colored by police symbols', 'BMW', True, 140)
# print(car1.go())
# print(car2.stop())
# print(car3.turn_left())
# print(car4.turn_right())
#
# # 5
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Drawn {self.title}'
#
# class Pen(Stationery):
#     def draw(self):
#         return f'you use the {self.title} pen for drawing'
#
# class Pencil(Stationery):
#     def draw(self):
#         return f'you use the {self.title} pencil for drawing'
#
# class Handle(Stationery):
#     def draw(self):
#         return f'you use the {self.title} handle for drawing'
#
# pen1 = Pen('Bic')
# pen2 = Pen('Gel')
# pencil1 = Pencil('HB')
# pencil2 = Pencil('H')
# handle1 = Handle('Permanent')
# handle2 = Handle('CD')
# print(pen1.draw())
# print(pen2.draw())
# print(pencil1.draw())
# print(pencil2.draw())
# print(handle1.draw())
# print(handle2.draw())