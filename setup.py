from distutils.core import setup

V = '0.1'

setup(
    name = 'join-iterables',
    packages = ['join_iterables'],

    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    version = V,
    license='MIT',
    description='Joins iterables in a streaming fashion while respects repetitions',
    url = 'https://github.com/andyil/join-iterables',
    download_url = f'https://github.com/andyil/join-iterables/archive/{V}.tar.gz',
    keywords = ['python', 'data', 'iterable', 'iterables', 'itertools', 'more-itertools', 'join'],
    install_requires=['more-itertools'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)