unsga3
======

.. image:: https://img.shields.io/pypi/v/unsga3.svg
    :target: https://pypi.python.org/pypi/unsga3
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

An implementation of Deb's Unified NSGA 3 algorithm. Can be used as a standard optimisation engine. Can also be used
in machine learning use case where over-fitting is monitored (i.e., where available data has been split into a
training set for training the model on, and a validation data set that is not used in training but used to
monitor for the model becoming over-fitted).

Usage
-----

WHAT DOES FITNESS GENERATION FUNCTION LOOK LIKE?
WHAT ARE INSPECTORS?

The Deb 2014 recommends using a relatively larger value for the distribution index in SBX crossover, to create
offspring closer to their parents.

If the `lhsmdu <https://github.com/sahilm89/lhsmdu>`_ package is installed, then the initial population of solutions will
be seeded using a `latin hypercube design <https://en.wikipedia.org/wiki/Latin_hypercube_sampling>`_, a technique of
fully sampling a spatial volume using few observations. If this package is not installed, then solutions will instead
be seeded by sampling from uniform random distributions for each dimension of solution space.

Installation
------------

Requirements
^^^^^^^^^^^^

Compatibility
-------------
This project was developed on a Mac using the Python 3.5 release of Anaconda (which includes many useful libraries). It
should work on any bash-compatible unix system. I have no experience of attempting to deploy this on Windows.

Licence
-------
General Public Licence V3.

Authors
-------

`unsga3` was written by `Mark N. Read <mark.norman.read@gmail.com>`_.


Background
----------

Non-Dominated Sorting Genetic Algorithm 3 (NSGA3) is an advancement over NSGA2, which has proven extremely popular
since it was first published in 2002. NSGA3 was motivated by the need to expand beyond "multi"-optimisation, in which
performance degrades when there are more than 3 objectives, into "many"-optimisation problems. The number of
solutions found on a Pareto front increases exponentially with the number of objectives. To manage this, NSGA3 makes
use of "reference directions", trajectories from the origin into (now "many" dimensional) fitness space, and
maintains a population of solutions that lie near these. Hence, the number of Pareto solutions can be restrained,
whilst still ensuring a good coverage of all possible solutions.

My use case for developing this algorithm with capacity to detect overfitting is in calibrating simulations against
available data. This is described in the two Read 2016 papers cited below.

The non-dominated sorting algorithm implemented is the efficient solution presented in Fortin 2013.

SBX and mutation implementations are based on Deb 1999.

References
----------

Deb K, Agrawal S. (1999). A Niched-Penalty Approach for Constraint Handling in Genetic Algorithms. In: Artificial Neural
Nets and Genetic Algorithms. Springer, Vienna, pp 235–243.

Das I, Dennis JE. (1998). Normal-Boundary intersection: A new method for generating the Pareto surface in non-linear
multicriteria optimization problems. Soc Ind Appl Math J Optim 8: 631–657.

Deb K, Jain H. (2014). An Evolutionary Many-Objective Optimization Algorithm Using Reference-Point-Based Nondominated
Sorting Approach , Part I : Solving Problems With Box Constraints. IEEE Trans Evol Comput 18: 577–601.

Fortin F-A, Grenier S, Parizeau M. (2013). Generalizing the improved run-time complexity algorithm for non-dominated
sorting. In: Proceedings of the 15th Annual Conference on Genetic and Evolutionary Computation. pp 615–622.

Seada H, Deb K. (2016). A Unified Evolutionary Optimization Procedure for Single, Multiple, and Many Objectives. IEEE
Trans Evol Comput 20: 358–369.

Read MN, Alden K, Rose LM, Timmis J, Read MN. (2016). Automated multi-objective calibration of biological agent-based
simulations. Journal of the Royal Society Interface 13: 20160543.

Read MN, Bailey J, Timmis J, Chtanova T. (2016). Leukocyte Motility Models Assessed through Simulation and
Multi-objective Optimization-Based Model Selection. PLOS Comput Biol 12: e1005082.