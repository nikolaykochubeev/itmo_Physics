from math import log
import matplotlib.pyplot as pt


class Electron:
    def __init__(self, v, r1, r2, l):
        self.x = 0
        self.y = (r2 - r1) / 2 + r1
        self.r1 = r1
        self.r2 = r2
        self.vx = v
        self.vy = 0
        self.q = -1.6 * 10 ** -19
        self.m = 9.1 * 10 ** -31
        self.l_ = l
        self.t = 0

    def aay(self, U):
        return (self.q * U) / (self.y * self.m * log(self.r2 / self.r1))

    def motion(self, U):
        dt = 1 / 1000000000000
        while self.x < self.l_ and self.y > self.r1:
            dvy = self.aay(U)
            self.vy += dvy * dt
            self.y += self.vy * dt
            self.x += self.vx * dt
            self.t += dt

    def motion_for_graphic(self, U):
        dt = 1 / 1000000000000
        yx = []
        vy = []
        ay = []
        yt = []
        while self.x < self.l_ or self.y > self.r1:
            yx.append((self.x, self.y))
            vy.append((self.t, self.vy))
            dvy = self.aay(U)
            ay.append((self.t, dvy))
            yt.append((self.t, self.y))
            self.vy += dvy * dt
            self.y += self.vy * dt
            self.x += self.vx * dt
            self.t += dt
        return [yx, vy, ay, yt]


with open("input.txt", "r") as f:
    a = [[float(j) for j in i.split(" ")] for i in f.read().split("\n")]
ind = int(input()) - 1
Umax = 1000
Umin = 0
while Umax - Umin > 0.0000001:
    Electron_ = Electron(a[ind][2], a[ind][0], a[ind][1], a[ind][3])
    U = (Umax + Umin) / 2
    Electron_.motion(U)
    if Electron_.x >= Electron_.l_:
        Umin = U
    else:
        Umax = U
Electron_ = Electron(a[ind][2], a[ind][0], a[ind][1], a[ind][3])
yx, vy, ay, yt = Electron_.motion_for_graphic(U)
print("Минимальное напряжение", U)
print("Время полета", Electron_.t)
print("Скорость конечная", (Electron_.vy ** 2 + Electron_.vx ** 2) ** 0.5)
pt.title('Зависимость высоты от расстояния')
pt.xlabel('Пройденное расстояние, м')
pt.ylabel('Высота, м')
pt.plot([i[0] for i in yx], [i[1] for i in yx])
pt.grid()
pt.savefig('y(x)', )
pt.show()
pt.title('Зависимость скорости от времени')
pt.xlabel('Время, c')
pt.ylabel('Скорость, м/c')
pt.grid()
pt.plot([i[0] for i in vy], [i[1] for i in vy])
pt.savefig('Vy(t)', )
pt.show()
pt.title('Зависимость ускорения от времени')
pt.xlabel('Время, c')
pt.ylabel('Ускорение, м/c^2')
pt.grid()
pt.plot([i[0] for i in ay], [i[1] for i in ay])
pt.savefig('ay(t)', )
pt.show()
pt.title('Зависимость высоты от времени')
pt.xlabel('Время, с')
pt.ylabel('Высота, м')
pt.grid()
pt.plot([i[0] for i in yt], [i[1] for i in yt])
pt.savefig('y(t)', )
pt.show()
