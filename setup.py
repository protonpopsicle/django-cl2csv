#!/usr/bin/env python

from distutils.core import setup

setup(name='django-cl2csv',
      version='1.01',
      description='CL2CSV (Change List to CSV) is a Django app (pluggable) that makes change lists (in the admin) exportable.',
      author='Scott Meisburger',
      author_email='smeisburger@gmail.com',
      url='https://github.com/protonpopsicle/django-cl2csv',
      packages=['cl2csv'],
     )
