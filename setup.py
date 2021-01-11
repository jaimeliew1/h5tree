# https://python-packaging.readthedocs.io
from setuptools import setup

setup(name                 = 'h5tree',
      version              = '0.1',
      description          = 'prints data sets and groups of hdf5 file as a tree.',
      #url                  =
      author               = 'Jaime Liew',
      author_email         = 'jaimeliew1@gmail.com',
      packages             = ['h5tree'],
      # install_requires     = ['click', 'jinja2', 'wetb'],
      entry_points         = {
        'console_scripts': ['h5tree=h5tree.h5tree:main']},
)
