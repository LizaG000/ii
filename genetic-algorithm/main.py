from min import *
import numpy as np


if __name__ == "__main__":
    print("Функция 1.")
    input_values = input_func()
    genetic_algoritm(input_values, lambda x: 2*x*np.sin(x)-x/5)
    input()
    print("Функция 2.")
    input_values = reenter_func(input_values)
    genetic_algoritm(input_values, lambda x: 3*x*np.sin(x)+x/3)
    input()
    print("Функция 3.")
    input_values = reenter_func(input_values)
    genetic_algoritm(input_values, lambda x: 2*x*np.cos(x)+x/3)
    input()