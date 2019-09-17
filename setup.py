from setuptools import setup, find_packages
import io
import os


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode='r', encoding='utf-8') as f:
        return f.read().splitlines()


setup(
    name='tables',
    packages=find_packages(),
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'tables = tables.__main__:main'
        ]
    },
    author='Seth Rothschild',
    author_email='seth.j.rothschild@gmail.com',
    description='Table arrangements',
    install_requires=read('requirements.txt'),
    tests_require=[
        'pytest'
    ],
    test_suite='pytest'
)
