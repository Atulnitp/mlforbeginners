''' Installation script for python fromscratchtoml package'''

from setuptools import find_packages, setup

linux_testenv = [
    'pytest-cov',
    'python-coveralls',
]

setup(
    name='ml-for-beginners',
    version='0.0.1',
    description=' A machine learning library from scratch as well as using pytorch for beginners.',

    install_requires=[
        'numpy >= 1.14.2',
        'matplotlib >= 2.1.0'
    ],
    extras_require={
        'test': linux_testenv,
        'docs': linux_testenv + ['sphinx', 'sphinxcontrib-napoleon', 'travis-sphinx', 'sphinxcontrib.programoutput']
    },
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/ml-for-beginners',
    license='GPL-3.0',
    packages=find_packages(),
)
