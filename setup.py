from setuptools import setup

setup(name='journal_dates',
      packages=[''],
      version='0.1',
      description='Prints a monthly journal template',
      url='http://github.com/bzamecnik/journal_dates',
      author='Bohumir Zamecnik',
      author_email='bohumir.zamecnik@gmail.com',
      license='MIT',
      install_requires=['arrow'],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'journal_dates=journal_dates:main',
        ],
      })
