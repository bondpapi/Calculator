from setuptools import setup, find_packages  # type: ignore

setup(
    name='calculator',
    version='1.0.0',
    description='A simple calculator class for performing basic arithmetic operations',
    author='Michael Bond',
    author_email='bondpapi@yahoo.com',
    url='https://github.com/bondpapi/calculator',
    packages=find_packages(),
    install_requires=[],  # No external depencies
    extras_require={'dev': ['pytest'],},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
    ],
    python_requires='>=3.6',
)
