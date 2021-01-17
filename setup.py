from setuptools import setup
from setuptools import find_packages
from glob import glob
from os.path import basename
from os.path import splitext

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='template-python',
    version='0.0.1',
    license='MIT',
    description='Project template for python',
    author='Yuya Honda',
    url='https://github.com/yuyahnd/template-python.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
