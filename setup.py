#!/usr/bin/env python

from setuptools import setup

setup(name='features',
      version='0.1',
      description='A collection of feature extraction/selection algorithms',
      author='Charanpal Dhanjal',
      author_email='charanpal@gmail.com',
      url='https://github.com/charanpald/features',
      install_requires=['numpy>=1.5.0', 'scipy>=0.7.1'],
      platforms=["OS Independent"],
      packages=['features', 'kernel', "features.test", "kernel.test"],
     )

