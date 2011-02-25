import os

try:
    from setuptools import setup, find_packages, Command
    from setuptools.command.test import test
    from setuptools.command.install import install
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Command
    from setuptools.command.test import test
    from setuptools.command.install import install

requirements = map(str.strip, open('requirements.txt').readlines())

setup(
    name='chai',
    version='0.0.1',
    author="Vitaly Babiy, Aaron Westendorf",
    author_email="vbabiy@agoragames.com, aaron@agoragames.com",
    packages = find_packages() ,
    py_modules = ['chai'],
    install_requires = requirements,
    license="MIT License",
    long_description=open('README.txt').read(),
    keywords=['python', 'test', 'mock'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ]
)