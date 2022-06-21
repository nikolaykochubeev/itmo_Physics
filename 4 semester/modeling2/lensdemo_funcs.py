import numpy as N


# трансформируем переданные x, y координаты в повернутые в новой системе на угол фи
def xy_rotate(x, y, xcen, ycen, phi):
    phirad = N.deg2rad(phi)
    xnew = (x - xcen) * N.cos(phirad) + (y - ycen) * N.sin(phirad)
    ynew = (y - ycen) * N.cos(phirad) - (x - xcen) * N.sin(phirad)
    return xnew, ynew


# вводим 2д-функцию гаусса
def gauss_2d(x, y, par):
    """
        par[0]: амплитуда
        par[1]: гауссова сигма
        par[2]: x-координата центра
        par[3]: y-координата центра
        par[4]: соотношение сторон
        par[5]: поворот осей
    """
    (xnew, ynew) = xy_rotate(x, y, par[2], par[3], par[5])
    r_ell_sq = ((xnew ** 2) * par[4] + (ynew ** 2) / par[4]) / N.abs(par[1]) ** 2
    return par[0] * N.exp(-0.5 * r_ell_sq)


# Моделируем линзирование
def sie_grad(x, y, par):
    """
        par[0]: радиус эйнштейна
        par[2]: x-координата центра
        par[3]: y-координата центра
        par[4]: соотношение сторон
        par[5]: поворот осей
    """
    b = N.abs(par[0])
    xzero = 0. if (len(par) < 2) else par[1]
    yzero = 0. if (len(par) < 3) else par[2]
    q = 1. if (len(par) < 4) else N.abs(par[3])
    phiq = 0. if (len(par) < 5) else par[4]
    eps = 0.001
    if (q > 1.):
        q = 1.0 / q
        phiq = phiq + 90.0
    # переходим в "сдвинутые" координаты
    phirad = N.deg2rad(phiq)
    xsie = (x - xzero) * N.cos(phirad) + (y - yzero) * N.sin(phirad)
    ysie = (y - yzero) * N.cos(phirad) - (x - xzero) * N.sin(phirad)
    # считаем линзированный градиент
    r_ell = N.sqrt(q * xsie ** 2 + ysie ** 2 / q)
    qfact = N.sqrt(1. / q - q)
    if qfact >= eps:
        xtg = (b / qfact) * N.arctan(qfact * xsie / (r_ell + (r_ell == 0)))
        ytg = (b / qfact) * N.arctanh(qfact * ysie / (r_ell + (r_ell == 0)))
    else:
        xtg = b * xsie / (r_ell + (r_ell == 0))
        ytg = b * ysie / (r_ell + (r_ell == 0))
    # трансформируем обратно в нетрансформированные координаты
    xg = xtg * N.cos(phirad) - ytg * N.sin(phirad)
    yg = ytg * N.cos(phirad) + xtg * N.sin(phirad)
    # Return value:
    return xg, yg

