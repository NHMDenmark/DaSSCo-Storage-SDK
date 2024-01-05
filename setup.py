from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'SDK for the DaSSCo Storage API'

# Setting up
setup(
    name="dasscostorageclient",
    version=VERSION,
    author="DaSSCo",
    author_email="dassco.ku.dk",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'pydantic'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ]
)