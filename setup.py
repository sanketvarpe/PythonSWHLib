from setuptools import find_packages, setup

with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='PythonSWH',
    packages=find_packages(include=['PythonSWH']),
    version='1.0.0',
    description='My first Python library',
    author='Sanket Varpe',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    python_requires=">=3.2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)