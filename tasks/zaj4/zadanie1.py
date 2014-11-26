# -*- coding: utf-8 -*-

import numpy as np


def linear_func(x, a, b):
    return a*x+b

print(linear_func(np.arange(5,10,1),3,1))

def chisquared(xy, a, b):
    """

    Funkcja liczy sumę Chi^2 między wartościami zmierzonej funkcji a funkcją 
    liniową o wzorze a*x + b.

    Sumę chi^2 definiujemy jako:

    Chi^2 = Sum(( (y - f(x))/sigma_y)^2)

    gdzie f(x) to w naszym przypadku funkcja liniowa


    :param np.ndarray xy: Tablica o rozmiarze N x 3, w pierwszej kolumnie
        zawarte są wartości zmiennej a w drugiej wartości y.
    :param float a:
    :param float b:
    :return:
    """
    f_x=linear_func(xy[:,0],a,b)
    chi_2 = sum(( (xy[:,1] - f_x)/xy[:,2])**2)
    return chi_2
    
print(chisquared(np.ones((10,3)),5,2))
def least_sq(xy):
    """
    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.

    A = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    B = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: Jak w chisquared, uwaga: sigma_y nie jest potrzebne.
    :return: Krotka
    """
    N=len(xy[:,0])
    Delta = N*np.sum(xy[:,0]**2) - (np.sum(xy[:,0])**2)
    A = (np.sum(xy[:,0]**2)*np.sum(xy[:,1])-np.sum(xy[:,0])*np.sum(xy[:,1]*xy[:,0]))/Delta
    B = (N*np.sum(xy[:,1]*xy[:,0])-np.sum(xy[:,0])*np.sum(xy[:,1]))/Delta
    return (A,B)
print(least_sq(np.ones((10,3))))