#!/usr/bin/env python3
"""
# from root project directory (unsga3) run as:
# $> python3 -m tests.test_launch

See bottom of file for which tests to run.
"""
import unsga3
import unsga3.non_dominated_sort
import numpy.random
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from mpl_toolkits.mplot3d import Axes3D


def fitness_function_factory(dimensionality, validation=False, offset=0.5):
    """
    Returns a function to generate fitnesses.
    :param dimensionality: number of objectives being simulated
    :param validation: whether or not to return validation fitness values
    :param offset: added to fitness values generated, used to ensure that fitness normalisation is working correctly.
    :return:
    """
    def uniform_fitness_generator(population, generation):
        """
        Assigns fitnesses for the supplied list of candidates
        :param population: list of unsga3.Candidate objects
        :param generation: generation number of optimisation process
        :return:
        """
        # assign unique ids to each candidate.
        for c, cand in enumerate(population):
            cand.databank['id'] = 'g{:d}_c{:d}'.format(generation, c)
        training_fitnesses = [numpy.random.uniform(size=dimensionality) + offset for _ in population]
        if validation:
            validation_fitnesses = [numpy.random.uniform(size=dimensionality) + offset for _ in population]
        else:
            validation_fitnesses = None
        return training_fitnesses, validation_fitnesses

    return uniform_fitness_generator


class GenerationalInspector:
    def __init__(self, attr):
        """
        :param attr: String, name of which UNSGA3 attribute to inspect. E.g. "fitness_normalised", "fitness",
        "target_fitness" or "validation_fitness" (if used)
        """
        self.generational_fronts = []
        self.generational_ranks = []
        self.generational_ids = []  # unique IDs are given to each candidate
        self.attr = attr
        self.optimiser = None

    def inspect(self, unsga3):
        """
        Passed to the UNSGA3 object.
        :param unsga3:
        :return:
        """
        if self.optimiser is None:
            self.optimiser = unsga3
        print("running generational inspection")
        fitnesses = []
        ranks = []
        ids = []
        print('  inspector: found {:d} population candidates in generation {:d}'.format(len(unsga3.current_population),
                                                                                      unsga3.current_generation))
        for cand in unsga3.current_population:
            print('    cand: ' + str(cand))
            ids.append(cand.databank['id'])
            fitnesses.append(getattr(cand, self.attr))
            ranks.append(cand.non_dominated_rank)
        self.generational_ids.append(ids)
        # temporary variable, zip up fitnesses and ranks so that they are shorted simultaneously
        z = [(f, r) for f, r in zip(fitnesses, ranks)]
        z.sort()  # sort according to fitnesses (defaults sorting on second items if first are identical)
        fitnesses = [zi[0] for zi in z]
        ranks = [zi[1] for zi in z]
        self.generational_fronts.append(fitnesses)
        self.generational_ranks.append(ranks)
        print("  exiting inspector\n")

    def report_generational_ids(self):
        for gen in self.generational_ids:
            print(gen)

    def plot_all_generations_2d(self):
        plt.clf()
        cols = ['k', 'r', 'g', 'b', 'y']
        for fi, f in enumerate(self.generational_fronts):
            xs = [c[0] for c in f]
            ys = [c[1] for c in f]
            plt.scatter(xs, ys, c=cols[fi % len(cols)], s=200)
        # plot the reference directions too
        for rd in self.optimiser.reference_directions:
            plt.plot((0, rd[0]), (0, rd[1]), c='grey')
        plt.show()

    def plot_single_generation_fronts(self, generations=[]):
        """
        Plots the population at a given generation. Candidates are coloured by their front ID (ie, Pareto front = 0 =
        black).
        :param generations: which generations to plot, if None plot all
        :return:
        """
        if not generations:
            generations = list(range(len(self.generational_ranks)))
        if not isinstance(generations, (tuple, list)):
            generations = [generations]
        num_objectives = len(self.generational_fronts[0][0])
        if num_objectives == 2:
            self.plot_single_generation_fronts_2d(generations)
        if num_objectives == 3:
            self.plot_single_generation_fronts_3d(generations)
        else:
            raise Exception("no plotting mechanism has been created for problems with {:d} objectives"
                            .format(num_objectives))

    def plot_single_generation_fronts_2d(self, generations=()):
        """
        Plots the population at a given generation. Candidates are coloured by their front ID (ie, Pareto front = 0 =
        black).
        :param generations: which generations to plot, if None plot all
        :return:
        """
        cols = ['k', 'r', 'g', 'b', 'y']
        for generation in generations:
            plt.clf()
            plt.title('generation {:d}'.format(generation))
            xs = [c[0] for c in self.generational_fronts[generation]]
            ys = [c[1] for c in self.generational_fronts[generation]]

            for x, y, r in zip(xs, ys, self.generational_ranks[generation]):
                # cycle through colours if there are more fronts than colours defined
                plt.scatter(x, y, c=cols[r % len(cols)], s=200)
            # plot the reference directions too
            for rd in self.optimiser.reference_directions:
                plt.plot((0, rd[0]), (0, rd[1]), c='grey')
            plt.show()

    def plot_single_generation_fronts_3d(self, generations=()):
        cols = ['k', 'y', 'g', 'b', 'r']
        for generation in generations:
            front = self.generational_fronts[generation]
            xs = [c[0] for c in front]
            ys = [c[1] for c in front]
            zs = [c[2] for c in front]
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            print(self.generational_ranks[generation])
            for x, y, z, r in zip(xs, ys, zs, self.generational_ranks[generation]):
                c = cols[r % len(cols)]
                ax.scatter(xs=xs, ys=ys, zs=zs, c=c, s=100)
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
            ax.set_xlim([0.0, 1.2])
            ax.set_ylim([0.0, 1.2])
            ax.set_zlim([0.0, 1.2])
            plt.show()


def test_independent_nondomination(fitnesses, op):
    popn = [unsga3.unsga3.Candidate(()) for f in fitnesses]
    for cand, fit in zip(popn, fitnesses):
        cand.fitness = fit
    fronts = unsga3.non_dominated_sort.non_dominated_sort(popn)
    ranks = [cand.non_dominated_rank for cand in fronts[0]]
    print(ranks)
    plt.clf()
    cols = ['k', 'r', 'g', 'b', 'y']
    for fi, f in enumerate(fronts):
        xs = [c.fitness[0] for c in f]
        ys = [c.fitness[1] for c in f]
        plt.plot(xs, ys, c=cols[fi % len(cols)])
        plt.scatter(xs, ys, c=cols[fi % len(cols)])
    for rd in op.reference_directions:
        plt.plot((0, rd[0]), (0, rd[1]), c='grey')
    plt.show()


def test_single_generations_2d():
    solution_dimensions = (unsga3.SolutionDimension(min_val=0., max_val=1., granularity=0.1),
                           unsga3.SolutionDimension(min_val=2, max_val=10, granularity=1),
                           unsga3.SolutionDimension(min_val=0., max_val=5.))
    num_objectives = 2
    inspector = GenerationalInspector(attr="training_fitness")
    op = unsga3.UNSGA3(solution_dimensions=solution_dimensions,
                       fitness_evaluator=fitness_function_factory(num_objectives, offset=0.0),
                       num_objectives=num_objectives,
                       max_generations=30,
                       population_size=None,
                       reference_point_increments=5,
                       generatonal_inspector_function=inspector.inspect)
    op.run()
    inspector.plot_single_generation_fronts(generations=[-1])


def test_single_generations_3d():
    solution_dimensions = (unsga3.SolutionDimension(min_val=0., max_val=1., granularity=0.1),
                           unsga3.SolutionDimension(min_val=2, max_val=10, granularity=1),
                           unsga3.SolutionDimension(min_val=0., max_val=5.))
    num_objectives = 3
    inspector = GenerationalInspector(attr="training_fitness")
    op = unsga3.UNSGA3(solution_dimensions=solution_dimensions,
                       fitness_evaluator=fitness_function_factory(num_objectives, offset=0.0),
                       num_objectives=num_objectives,
                       max_generations=3,
                       population_size=None,
                       reference_point_increments=5,
                       generatonal_inspector_function=inspector.inspect)
    op.run()
    inspector.plot_single_generation_fronts(generations=[])


def test_all_generations_2d():
    problem_dimensions = (unsga3.SolutionDimension(min_val=0., max_val=1., granularity=0.1),
                          unsga3.SolutionDimension(min_val=2, max_val=10, granularity=1),
                          unsga3.SolutionDimension(min_val=0., max_val=5.))
    num_objectives = 2
    inspector = GenerationalInspector(attr="training_fitness")
    op = unsga3.UNSGA3(solution_dimensions=problem_dimensions,
                       fitness_evaluator=fitness_function_factory(num_objectives, offset=0.0),
                       num_objectives=num_objectives,
                       max_generations=30,
                       population_size=None,
                       reference_point_increments=5,
                       generatonal_inspector_function=inspector.inspect)
    candidates = op.run()
    inspector.report_generational_ids()
    inspector.plot_all_generations_2d()


def test_ParetoFitness():
    """ Confirm that an empty ParetoFitness objects - ParetoFitness(()) - evaluates to False. """
    p = unsga3.unsga3.ParetoFitness(())
    if p:
        print('evaluates to True')
    else:
        print('evaluates to False')


if __name__ == '__main__':
    # test_single_generations_2d()
    test_single_generations_3d()
    # test_ParetoFitness()
    # test_all_generations()

