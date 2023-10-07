from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    # name
    name='nu_tune',

    # current version
    #   MAJOR VERSION:  00
    #   MINOR VERSION:  01
    #   Maintenance:    00
    version='00.01.00',

    # descriptions
    description='MCTS tuning for neutrino generators.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='',

    # my info
    author='Nicholas Carrara',
    author_email='ncarrara.physics@gmail.com',

    # where to find the source
    url='https://github.com/infophysics/nu_tune',

    # requirements
    install_reqs = [],

    # packages
    # package_dir={'':'nu_tune'},
    packages=find_packages(
        # 'nu_tune',
        exclude=['tests'],
    ),
    include_package_data=True,

    # classifiers
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Experimental Physics',
        'License :: GNU',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>3.7',

    # possible entry point
    entry_points={
        'console_scripts': [
            'nu_tune = nu_tune.programs.run_nu_tune:run'
        ],
    },
)
