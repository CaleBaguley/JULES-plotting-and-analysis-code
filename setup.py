#!/usr/bin/env python

from setuptools import setup

packages = ['JULES_Plotting_and_Analysis',
            'JULES_Plotting_and_Analysis.src',
            'JULES_Plotting_and_Analysis.src.plotting',
            'JULES_Plotting_and_Analysis.src.data_conversions']

setup(name='JULES_Plotting_and_Analysis',
      version='0.1',
      description='A package to plot JULES output data',
      author='Cale Baguley',
      url='https://github.com/CaleBaguley/JULES-plotting-and-analysis-code',
      packages=packages
      )

