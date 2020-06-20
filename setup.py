from setuptools import setup

setup(
    name='shortcwd',
    version='0.1',
    author='Barney Gale',
    author_email='barney.gale@gmail.com',
    url='https://github.com/barneygale/shortcwd',
    license='GPLv3+',
    description='Wraps `SUBST` in a context manager. Helps shorten path lengths to avoid `MAX_PATH`.',
    long_description=open('README.rst').read(),
    packages=["shortcwd"],
)