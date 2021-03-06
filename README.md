# journal_dates

[![PyPI version](https://img.shields.io/pypi/v/journal_dates.svg)](https://pypi.python.org/pypi/journal_dates)
![Supported Python versions](https://img.shields.io/pypi/pyversions/journal_dates.svg)
![License](https://img.shields.io/pypi/l/journal_dates.svg)

A simple Python script to generate a template of journal entries for a month.

```
pip install journal_dates
```

```
# by default it prints dates for this month
$ journal_dates
Deník 2015/08

1.8.2015 (So)
2.8.2015 (Ne)
[...]
30.8.2015 (Ne)
31.8.2015 (Po)

# year and month specified
$ journal_dates 2015 9
Deník 2015/08

1.8.2015 (So)
2.8.2015 (Ne)
[...]
30.8.2015 (Ne)
31.8.2015 (Po)

# possibly also locale and date format
$ journal_dates 2015 9 --locale en_US --format 'YYYY-MM-DD'
Journal 2015/09

2015-09-01
2015-09-02
[...]
2015-09-29
2015-09-30
```

- Author: Bohumír Zámečník ([@bzamecnik](https://twitter.com/bzamecnik))
- License: MIT
