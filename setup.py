import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from Cython.Build import cythonize

build_dir='build'
CWD = os.getcwd()
pyfile_list=[]
for root, dirs, files in os.walk(CWD):
    for f in files:
        if not f.startswith('__init__') and not f.startswith('setup') and f.endswith('.py'):
            pyfile_list.append(root +'/'+ f)

setup(
    name='xxxx',
    version='1.0',
    author='Kellan Fan',
    ext_modules = cythonize(pyfile_list)
)

for root, dirs, files in os.walk(build_dir):
    for f in files:
        newname=f.split('.')[0]
        os.rename(root +'/'+ f, root +'/'+ newname)
