from setuptools import setup, find_packages

setup(
    name='lichen',
    version='0.1',
    description="Tick-based online AI game",
    url='http://github.com/lucian1900/lichen',

    packages=find_packages(),
    install_requires=[
        'django'
        #'Twisted',
        #'txRedis',
    ])
