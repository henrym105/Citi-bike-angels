from setuptools import setup, find_packages

setup(
    name='citi-bike-angels',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'citi-bike-angels=citi_bike_angels.__main__:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Citi Bike Angels points retrieval application',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/citi-bike-angels',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
