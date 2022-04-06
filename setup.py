
from setuptools import setup, find_packages

setup(
    name='Scorpion-1.0',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An Easier Expereince in Python',
    long_description=open('README.txt').read(),
    install_requires=['numpy','playsound','pygame'],
    url='',
    author='Mohammed Mahmoud',
    author_email='boomz.yt@hotmail.com'
     )
