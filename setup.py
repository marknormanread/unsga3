import setuptools

setuptools.setup(
    name="unsga3",
    version="0.1.0",
    url="https://bitbucket.org/markread/unsga3",

    author="Mark N. Read",
    author_email="mark.norman.read@gmail.com",

    description="Implementation of Deb's Unified NSGA 3 algorithm. Can be used as a standard optimisation engine, but "
                "has additional functionality to detect overitting of optimised solutions in (e.g.) calibration use "
                "cases.",
    long_description=open('README.rst').read(),

    packages=['unsga3'],

    install_requires=['numpy', 'matplotlib'],
    dependency_links=['https://github.com/sahilm89/lhsmdu'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
