import matplotlib.pyplot as pyplot
import numpy as np


def soliton_func(x, t, a):
    return 12 * (a ** 2) / ((np.cosh(a ** 2 * ((x - 15.) - 4. * (a ** 2.) * t))) ** 2)


class KDV:
    def __init__(self, u, x_start, x_end, t_start, t_end, dx, dt, a):
        self.dx = float(dx)
        self.dt = float(dt)
        self.x_start = x_start
        self.x_end = x_end
        self.t_start = t_start
        self.t_end = t_end
        self.particular_solution = u

        self.h_range = np.arange(int(x_start / self.dx), int(x_end / self.dx) + 1) * self.dx

        self.t_range = np.arange(int(t_start / self.dt), int(t_end / self.dt) + 1) * self.dt

        points_int = []

        for i in self.h_range:
            points_int.append(self.particular_solution(i, t_start, a))

        points_int = np.array(points_int)

        self.data = [points_int]

    def plot_many_graphs_on_one_graph(self, t_lst):
        pyplot.figure(1)
        for t in t_lst:
            pyplot.plot(self.h_range, self.data[t], label="t = " + str(t * self.dt))
        pyplot.legend()
        pyplot.xlabel("x")
        pyplot.ylabel("U")
        pyplot.savefig('all_graphs_on_one_graph.png')
        pyplot.show()

    def plot_graph_for_specific_time(self, t):
        pyplot.figure(t)
        pyplot.plot(self.h_range, self.data[t], 'b')
        pyplot.xlabel("x")
        pyplot.ylabel("U")
        pyplot.savefig(str(t) + '.png')
        pyplot.show()

    def runge_kutta_func(self, extra_u, i):
        u_f1 = np.roll(self.data[i] + extra_u, -1)
        u_b1 = np.roll(self.data[i] + extra_u, 1)
        u_f2 = np.roll(self.data[i] + extra_u, -2)
        u_b2 = np.roll(self.data[i] + extra_u, 2)
        return (-(self.dt / self.dx) * (u_f1 ** 2 - u_b1 ** 2) - 0.5 * (self.dt / self.dx ** 3) * (
                u_f2 - 2. * u_f1 + 2. * u_b1 - u_b2))

    def runge_kutta_method_u_next(self, i):
        u_0 = self.data[i]
        k1 = self.runge_kutta_func(0., i)
        k2 = self.runge_kutta_func(0.5 * k1, i)
        k3 = self.runge_kutta_func(0.5 * k2, i)
        k4 = self.runge_kutta_func(k3, i)

        return u_0 + (1. / 6) * (k1 + 2. * k2 + 2. * k3 + k4)

    def propagate_kdv_solver(self):
        for j in range(int(self.dt), len(self.t_range)):
            self.data.append(self.runge_kutta_method_u_next(j))


solution = KDV(soliton_func, 0, 100., 0, 30., 0.1, 0.001, 0.4)
solution.propagate_kdv_solver()

time_periods = [_ * 1600 for _ in range(0, 10)]
solution.plot_many_graphs_on_one_graph(time_periods)

for t in time_periods:
    solution.plot_graph_for_specific_time(t)
