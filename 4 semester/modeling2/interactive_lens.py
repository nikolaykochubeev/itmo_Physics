import numpy as np
import matplotlib as m
import matplotlib.pyplot as plt
from matplotlib import cm
import lensdemo_funcs as ldf
from matplotlib.widgets import Slider

m.use('TkAgg')
m.interactive(True)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.60)
myargs = {'interpolation': 'nearest', 'origin': 'lower', 'cmap': cm.get_cmap("nipy_spectral")}

nx = 501
ny = 501
xhilo = [-2.5, 2.5]
yhilo = [-2.5, 2.5]
x = (xhilo[1] - xhilo[0]) * np.outer(np.ones(ny), np.arange(nx)) / float(nx - 1) + xhilo[0]
y = (yhilo[1] - yhilo[0]) * np.outer(np.arange(ny), np.ones(nx)) / float(ny - 1) + yhilo[0]

g_amp = 1.0  # максимальная яркость (амплитуда)
g_sig = 0.05  # гауссова сигма
g_xcen = 0  # x-координата центра
g_ycen = 0  # y-координата центра
g_axrat = 1  # соотношение сторон
g_pa = 0  # угол поворота осей
gpar = np.asarray([g_amp, g_sig, g_xcen, g_ycen, g_axrat, g_pa])

# Set some SIE lens-model parameters and pack them into an array:
l_amp = 1.5  # Einstein radius
l_xcen = 0  # x-координата центра
l_ycen = 0  # y-координата центра
l_axrat = 1  # соотношение сторон
l_pa = 0  # угол поворота осей
lpar = np.asarray([l_amp, l_xcen, l_ycen, l_axrat, l_pa])

(xg, yg) = ldf.sie_grad(x, y, lpar)
g_lensimage = ldf.gauss_2d(x - xg, y - yg, gpar)

f = plt.imshow(g_lensimage, **myargs)

ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slamp = Slider(ax, 'Einstein radius', 0.001, 3.0, valinit=l_amp)

ax = plt.axes([0.25, 0.15, 0.65, 0.03])
slaxrat = Slider(ax, 'Lens Axis Ratio', 0.001, 2.0, valinit=l_axrat)

ax = plt.axes([0.25, 0.20, 0.65, 0.03])
sgaxrat = Slider(ax, 'Gaussian Axis Ratio', 0.001, 2.0, valinit=g_axrat)

ax = plt.axes([0.25, 0.25, 0.65, 0.03])
sgpa = Slider(ax, 'Gaussian Major-Axis Angle', 0.0, 360.0, valinit=g_pa)

ax = plt.axes([0.25, 0.30, 0.65, 0.03])
sgxcen = Slider(ax, 'Gaussian X-center', -1.5, 1.5, valinit=g_xcen)

ax = plt.axes([0.25, 0.35, 0.65, 0.03])
sgycen = Slider(ax, 'Gaussian Y-center', -1.5, 1.5, valinit=g_ycen)

ax = plt.axes([0.25, 0.40, 0.65, 0.03])
slxcen = Slider(ax, 'Lens X-center', -1.5, 1.5, valinit=l_xcen)

ax = plt.axes([0.25, 0.45, 0.65, 0.03])
slycen = Slider(ax, 'Lens Y-center', -1.5, 1.5, valinit=l_ycen)

ax = plt.axes([0.25, 0.5, 0.65, 0.03])
sgsig = Slider(ax, 'Gaussian Sigma', 0.01, 1, valinit=g_sig)


def update(val):
    l_amp = slamp.val
    g_axrat = sgaxrat.val
    g_xcen = sgxcen.val
    g_ycen = sgycen.val
    g_pa = sgpa.val
    g_sig = sgsig.val
    l_axrat = slaxrat.val
    l_xcen = slxcen.val
    l_ycen = slycen.val

    gpar = np.asarray([g_amp, g_sig, g_xcen, g_ycen, g_axrat, g_pa])
    lpar = np.asarray([l_amp, l_xcen, l_ycen, l_axrat, l_pa])

    # g_image = ldf.gauss_2d(x, y, gpar)
    (xg, yg) = ldf.sie_grad(x, y, lpar)
    g_lensimage = ldf.gauss_2d(x - xg, y - yg, gpar)
    f.set_data(g_lensimage)
    fig.canvas.draw_idle()


slamp.on_changed(update)
slxcen.on_changed(update)
slycen.on_changed(update)
slaxrat.on_changed(update)
sgaxrat.on_changed(update)
sgycen.on_changed(update)
sgxcen.on_changed(update)
sgpa.on_changed(update)
sgsig.on_changed(update)

plt.show(block=True)
