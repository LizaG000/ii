
import matplotlib
matplotlib.use('Qt5Agg')
from algetism import eaSimpleElitism
from deap import base, creator, tools
import random
import matplotlib.pyplot as plt
import numpy as np

class InputValues:
    def __init__(self, A: float, B: float, optimum:str, POPULATION_SIZE: int, P_CHROSSOVER: float,
                 P_MUTATION: float, MAX_GENERATIONS: int, HALL_OF_FAME_SIZE: int,
                 RANDOM_SEED: int, d: int):
        self.A = A
        self.B = B
        self.optimum = optimum
        self.POPULATION_SIZE = POPULATION_SIZE
        self.P_CHROSSOVER = P_CHROSSOVER
        self.P_MUTATION = P_MUTATION
        self.MAX_GENERATIONS = MAX_GENERATIONS
        self.HALL_OF_FAME_SIZE = HALL_OF_FAME_SIZE
        self.RANDOM_SEED = RANDOM_SEED
        self.d = d

def input_func():
    print("Введите значения для интервала A B через пробел: ", end="")
    A, B = map(float, input().split())
    print("Введите тип оптимума (min/max): ", end="")
    optimum = input()
    print("Введите количество популяций генетического алгоритма: ", end="")
    POPULATION_SIZE = int(input())
    print("Введите коэффицент скрещивания: ", end="")
    P_CHROSSOVER = float(input())
    print("Введите коэффицент мутации: ", end="")
    P_MUTATION = float(input())
    print("Введите максимально количество поколений: ", end="")
    MAX_GENERATIONS = int(input())
    print("Введите количество лучших особей для селекции: ", end="")
    HALL_OF_FAME_SIZE = int(input())
    print("Введите сид для рандомизации: ", end="")
    RANDOM_SEED = int(input())
    print("Введите параметр d-отображения графика: ", end="")
    d = int(input())
    return InputValues(A=A, B=B, optimum=optimum, POPULATION_SIZE=POPULATION_SIZE, P_CHROSSOVER=P_CHROSSOVER,
                      P_MUTATION=P_MUTATION, MAX_GENERATIONS=MAX_GENERATIONS,
                      HALL_OF_FAME_SIZE=HALL_OF_FAME_SIZE, RANDOM_SEED=RANDOM_SEED, d=d)




def reenter_func(input_values):
    print("Вы хотите использовать уже введенные параметры? (yes/no): ", end="")
    answer = input()
    while answer != "yes" and answer != "no":
        print("Пожалуйста введите \"yes\" или \"no\": ", end="")
        answer = input()
    if answer == "yes":
        return (input_values)
    return input_func()

def genetic_algoritm(input_values, _func):
    A = input_values.A
    B = input_values.B
    optimum = input_values.optimum
    POPULATION_SIZE = input_values.POPULATION_SIZE
    P_CHROSSOVER = input_values.P_CHROSSOVER
    P_MUTATION = input_values.P_MUTATION
    MAX_GENERATIONS = input_values.MAX_GENERATIONS
    HALL_OF_FAME_SIZE = input_values.HALL_OF_FAME_SIZE
    RANDOM_SEED = input_values.RANDOM_SEED
    d = input_values.d
    LENGTH_CHROM = 1
    ETA = 20

    def show(ax, xgrid, f, population):
        fitness_values = [himmelblau(ind) for ind in population]
        if optimum == "min":
            min_fitness = min(fitness_values)
        else:
            max_fitness = max(fitness_values)
        ax.clear()
        ax.plot(xgrid, f, label='f(x)', color='blue')
        for i, ind in enumerate(population):
            if optimum == "min" and fitness_values[i] > min_fitness[0] + 5:
                ax.scatter(ind[0], fitness_values[i], color='red', s=50, zorder=0)  # Подсвечиваем красным
            elif optimum == "max" and fitness_values[i] < max_fitness[0] - 5:
                ax.scatter(ind[0], fitness_values[i], color='red', s=50, zorder=0)  # Подсвечиваем красным
            else:
                ax.scatter(ind[0], fitness_values[i], color='green', s=50, zorder=0)  # Обычный цвет

        ax.legend(loc='upper left')
        plt.draw()
        plt.gcf().canvas.flush_events()
        plt.pause(1)

    x_ = np.arange(A-d, B+d, 0.1)
    f_ = _func(x_)
    plt.ion()
    plt.show()
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 5)
    ax.set_xlim(A-d, B+d)


    # создаем пространство для селекций
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    random.seed(RANDOM_SEED)
    if optimum == "min":
        if hasattr(creator, "FitnessMin"):
            del creator.FitnessMin
            del creator.Individual
        # класс для значений приспособлености особей
        creator.create("FitnessMin", base.Fitness, weights=(-1.0, ))
        # класс для представления самой особи
        creator.create("Individual", list, fitness=creator.FitnessMin)
    else:
        if hasattr(creator, "FitnessMax"):
            del creator.FitnessMax
            del creator.Individual
        # класс для значений приспособлености особей
        creator.create("FitnessMax", base.Fitness, weights=(1.0, ))
        # класс для представления самой особи
        creator.create("Individual", list, fitness=creator.FitnessMax)


    def randomPoint(a, b):
        return [round(random.uniform(a, b), 2)]

    toolbox = base.Toolbox()
    # регестрация генератора точек в диапозоне от A до B
    toolbox.register("randomPoint", randomPoint, A, B)
    # создание индивидов
    toolbox.register("individualCreator", tools.initIterate, creator.Individual, toolbox.randomPoint)
    # создание популяции
    toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

    population = toolbox.populationCreator(n=POPULATION_SIZE)

    # вычисляем значение ЦФ
    def himmelblau(individual):
        x = individual[0]
        f = _func(x)
        return f,

    # расчитывается приспособленность особей
    toolbox.register("evaluate", himmelblau)
    # выборка на основе турнира
    toolbox.register("select", tools.selTournament, tournsize=3)
    # функция скрещивания
    toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=A, up=B, eta=ETA)
    # функция для мутации
    toolbox.register("mutate", tools.mutPolynomialBounded, low=A, up=B, eta=ETA, indpb=1.0/LENGTH_CHROM)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    if optimum == "min":
        stats.register("min", np.min)
    else:
        stats.register("max", np.max)

    stats.register("avg", np.mean)

    population, logbook = eaSimpleElitism(population, toolbox,
                                          cxpb=P_CHROSSOVER,
                                          mutpb=P_MUTATION,
                                          ngen=MAX_GENERATIONS,
                                          halloffame=hof,
                                          stats=stats,
                                          callback=(show, (ax, x_, f_, population)),
                                          verbose=True)
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")
    best = hof.items[0]
    print(best)

