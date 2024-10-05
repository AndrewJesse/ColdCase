from setuptools import setup, find_packages

setup(
    name='learn_pandas',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'learn_pandas=learn_pandas.__main__:main',
        ],
    },
    author='Andrew Marchese',
    author_email='aj.marchese@outlook.com',
    description='Package for calculating factorial, combinations, and binomial distribution probabilities.',
    url='https://github.com/AndrewJesse/learn_pandas',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
