from bokeh.plotting import figure, output_file, show
from numpy import genfromtxt
import numpy as np


def acci_por_dept():
    años = []
    guate = []
    for i in range(len(data)):
        años = np.append(años,data[i][0])
    #print(lista)
    for i in range(len(años)):
        guate = np.append(guate,data[i][1])
    #print(guate)
    return años, guate

def graficar(yvalues, xvalues):
    output_file = ('AccidentesGuatemala')
    fig = figure()
    fig.line(xvalues, yvalues, line_width = 2)
    
    show(fig)
    return  


if __name__ == "__main__":
    data = genfromtxt('AccidentesPorDepartamento.csv', delimiter=',', skip_header=1)
    #print(data)
    y_vals = acci_por_dept()[1]
    x_vals = acci_por_dept()[0]
    graficar(y_vals, x_vals)