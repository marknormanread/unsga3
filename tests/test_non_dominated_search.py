#!/usr/bin/env python3
# run as
# $> python3 -m tests.test_non_dominated_search

from unsga3.non_dominated_sort import non_dominated_sort as non_dominated_sort
from unsga3.unsga3 import ParetoFitness as ParetoFitness
from unsga3.unsga3 import Candidate as Candidate
import numpy
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


def test_non_dominated_search_1D():
    objectives = 1
    population_size = 5
    population = []
    for c in range(population_size):
        fit = ParetoFitness(numpy.random.uniform(size=objectives))
        print('fit: ' + str(fit))
        cand = Candidate(solution=[])
        cand.training_fitness = fit
        cand.activate_training_fitness()
        population.append(cand)

    print('population:')
    for p in population:
        print(p)
    fronts = non_dominated_sort(population)

    print('fronts:')
    for i, f in enumerate(fronts):
        print('front #' + str(i))
        for c in f:
            print('  ' + str(c))


def test_non_dominated_search_2D():
    objectives = 2
    population_size = 100
    population = []
    for c in range(population_size):
        fit = ParetoFitness(numpy.random.uniform(size=objectives))
        print('fit: ' + str(fit))
        cand = Candidate(solution=[])
        cand.training_fitness = fit
        cand.activate_training_fitness()
        population.append(cand)

    print('population:')
    for p in population:
        print(p)
    fronts = non_dominated_sort(population)

    print('fronts:')
    for i, f in enumerate(fronts):
        print('front #' + str(i))
        for c in f:
            print('  ' + str(c))

    plt.clf()
    cols = ['k', 'r', 'g', 'b', 'y']
    for fi, f in enumerate(fronts):
        xs = [c.fitness[0] for c in f]
        ys = [c.fitness[1] for c in f]
        plt.plot(xs, ys, c=cols[fi % len(cols)])
        plt.scatter(xs, ys, c=cols[fi % len(cols)])
    plt.show()


def test_non_dominated_search_3D():
    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})

    objectives = 3
    population_size = 100
    population = []
    for c in range(population_size):
        fit = ParetoFitness(numpy.random.uniform(size=objectives))
        print('fit: ' + str(fit))
        cand = Candidate(solution=[])
        cand.training_fitness = fit
        cand.activate_training_fitness()
        population.append(cand)

    print('population:')
    for p in population:
        print(p)
    fronts = non_dominated_sort(population)

    print('fronts:')
    for i, f in enumerate(fronts):
        print('front #' + str(i))
        for c in f:
            print('  ' + str(c))

    cols = ['k', 'r', 'g', 'b', 'y']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for fi, f in enumerate(fronts):
        xs = [c.fitness[0] for c in f]
        ys = [c.fitness[1] for c in f]
        zs = [c.fitness[2] for c in f]
        ax.scatter(xs=xs, ys=ys, zs=zs, c=cols[fi % len(cols)], s=50.)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim([0.0, 1.2])
    ax.set_ylim([0.0, 1.2])
    ax.set_zlim([0.0, 1.2])
    plt.show()


def test_non_dominated_search_4D():
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})

    objectives = 6
    population_size = 1000
    population = []
    for c in range(population_size):
        fit = ParetoFitness(numpy.random.uniform(size=objectives))
        print('fit: ' + str(fit))
        cand = Candidate(solution=[])
        cand.training_fitness = fit
        cand.activate_training_fitness()
        population.append(cand)

    print('population:')
    for p in population:
        print(p)
    fronts = non_dominated_sort(population)

    print('fronts:')
    for i, f in enumerate(fronts):
        print('front #' + str(i))
        for c in f:
            print('  ' + str(c))


if __name__ == '__main__':
    test_non_dominated_search_1D()
    test_non_dominated_search_2D()
    test_non_dominated_search_3D()
    test_non_dominated_search_4D()
