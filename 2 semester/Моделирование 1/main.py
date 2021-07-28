import math
import matplotlib.pyplot as pt


class Rocket:
    def __init__(self, _x0=0, _y0=0, _angle=0, _rocket_mass=0, _fuel_mass=0, _gas_outflow=0, _fuel_burn=0):
        self.earth_mass, self.g, self.x0, self.y0, self.angle, \
            self.rocket_mass, self.fuel_mass, self.gas_outflow, self.fuel_burn = \
            5.97e+20, 9.81, _x0, _y0, _angle, _rocket_mass, _fuel_mass, _gas_outflow, _fuel_burn

    def x(self, time):
        return self.x0 + time * time * (self.fuel_burn * self.gas_outflow / (
                self.rocket_mass + self.fuel_mass - self.fuel_burn * time)) * math.cos(self.angle * math.pi / 180) / 2

    def y(self, time):
        return self.y0 + time * time * ((self.fuel_burn * self.gas_outflow / (
                self.rocket_mass + self.fuel_mass - self.fuel_burn * time)) * math.sin(
            self.angle * math.pi / 180) - self.g) / 2

    def speedX(self, time):
        return self.fuel_burn * self.gas_outflow / (
                self.rocket_mass + self.fuel_mass - self.fuel_burn * time) * math.cos(
            self.angle * math.pi / 180) * time

    def speedY(self, time):
        return ((self.fuel_burn * self.gas_outflow / (
                self.rocket_mass + self.fuel_mass - self.fuel_burn * time)) * math.sin(
            self.angle * math.pi / 180) - self.g) * time

    def speed(self, time):
        return math.fabs(((self.fuel_burn * self.gas_outflow / (
                self.rocket_mass + self.fuel_mass - self.fuel_mass * time)) - self.g) * time)

    def FuelMass(self, time):
        return self.fuel_mass - self.fuel_burn * time


rocket = Rocket(0, 0, 70, 100000, 70000, 3000, 2000)
speed = []
mass = []
traekt = []
for t in range(35):
    '''print("Секунд со старта: ", t, '\n', "Координата по оси Ox: ", rocket.x(t), '\n', "Координата по оси
Oy: ",
 rocket.y(t), '\n', "Скорость по оси Ox: ", rocket.speedX(t), '\n', "Скорость по оси Oy: ",
 rocket.speedY(t), '\n', "Модуль скорости: ", rocket.speed(t), '\n', "Масса топлива: ",
rocket.fuelMass(t),
 '\n')'''
    traekt.append([rocket.x(t), rocket.y(t)])
    mass.append([t, rocket.FuelMass(t)])
    speed.append([rocket.speedX(t), rocket.speedY(t)])
pt.title('Траектория полета ракеты')
pt.plot([i[0] for i in traekt], [i[1] for i in traekt])
pt.grid()
pt.savefig('traekt', )
pt.show()
pt.title('Скорость ракеты по осям')
pt.xlabel('Скорость по оси Ox')
pt.ylabel('Скорость по оси Oy')
pt.grid()
pt.plot([i[0] for i in speed], [i[1] for i in speed])
pt.savefig('speed', )
pt.show()
pt.title('Изменение массы ракеты')
pt.xlabel('Масса, кг')
pt.ylabel('Время, c')
pt.grid()
pt.plot([i[0] for i in mass], [i[1] for i in mass])
pt.savefig('mass', )
pt.show()
