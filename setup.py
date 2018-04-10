"""A setuptools-based script for installing BugWrangler."""
from setuptools import find_packages, setup

setup(
    name='BugWrangler',
    author='Og Maciel',
    author_email='omaciel@redhat.com',
    version='0.0.1',
    packages=find_packages(include=['bugwrangler', 'bugwrangler.*']),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'Click',
        'python-bugzilla',
        'rows',
    ],
    entry_points='''
        [console_scripts]
        bugwrangler=bugwrangler:cli
    ''',
    include_package_data=True,
    license='GPLv3',
    description=('Performs queries and actions against Red '
                 'Hat\'s Bugzilla.'),
    package_data={'': ['LICENSE']},
    url='https://github.com/SatelliteQE/bugwrangler',
)
