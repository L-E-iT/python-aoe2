from setuptools import find_packages, setup

setup(
    name='pythonaoe2',
    packages=find_packages(include=['pythonaoe2']),
    version='0.1.2',
    description='Using Python to interact with the AOE2 API',
    author='Brian Elliott',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1','requests','responses'],
    test_suite='test',
)