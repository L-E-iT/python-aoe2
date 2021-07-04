from setuptools import find_packages, setup

setup(
    name='pythonaoe2',
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    version='0.2.1',
    url="https://github.com/L-E-iT/python-aoe2",
    project_urls={
        "Bug Tracker": "https://github.com/L-E-iT/python-aoe2/issues",
    },
    description='Using Python to interact with the AOE2 API',
    author='Brian Elliott',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1','requests','responses'],
    test_suite='test',
)