#!/usr/bin/env python3
# run as
# $> python3 -m tests.test_reference_points


import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from mpl_toolkits.mplot3d import Axes3D
import unsga3.reference_points as ref_pt


def test_reference_point_generation():
    """
    Testing function that plots reference points in 3D.
    """
    dimensions = 3
    increments = 15  # includes zero. Hence, p from Das & Dennis paper is this -1.
    reference_points = ref_pt.build_reference_points(dimensions, increments)
    print(reference_points)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs=reference_points[:, 0], ys=reference_points[:, 1], zs=reference_points[:, 2])
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim([0.0, 1.2])
    ax.set_ylim([0.0, 1.2])
    ax.set_zlim([0.0, 1.2])
    plt.show()


if __name__ == '__main__':
    test_reference_point_generation()