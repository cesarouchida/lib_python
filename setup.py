from setuptools import setup, find_packages

setup(
    name='libconexaobd',
    version='0.0.1',
    url='',
    author='cesar',
    author_email='cesarouchida@gmail.com',
    description='testes',
    long_description='testes',
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    packages=find_packages(include=["libconexaobd", "libconexaobd.*"]),
    python_requires=">=3.7"
)
