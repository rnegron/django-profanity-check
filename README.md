## django-profanity-check

<p align="center">

[![Build Status](https://travis-ci.org/rnegron/django-profanity-check.svg?branch=master)](https://travis-ci.org/rnegron/django-profanity-check)
[![codecov](https://codecov.io/gh/rnegron/django-profanity-check/branch/master/graph/badge.svg?token=4pA3WXfFpz)](https://codecov.io/gh/rnegron/django-profanity-check)
[![pypi version](https://img.shields.io/pypi/v/django-profanity-check.svg)](https://pypi.org/project/django-profanity-check/)
[![Packaged with poetry](https://img.shields.io/badge/package_manager-poetry-blue.svg)](https://poetry.eustace.io/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

</p>

A Django template filter that wraps around [profanity-check](https://github.com/vzhou842/profanity-check).

**Note**: `numpy`, `scipy`, and `scikit-learn` are all dependencies of `profanity-check`.

## Usage

1. Install with `pip`.

   ```
   pip install django-profanity-check
   ```

1. Add `profanity` to your `INSTALLED_APPS`.

   ```python
   # settings.py

   INSTALLED_APPS = [ ..., 'profanity', ...]

   ```

1. Use it in a template!

   ```python-django
   {# ... #}

   {% load profanity %}

   {# ... #}

   {% with sentence='Hey, fuck you!' %}
      {{ sentence | censor }} {# Will result in: 'Hey, **** you!' #}
   {% endwith %}

   ```

## Todo

- [ ] Allow custom replacement characters
- [ ] Allow custom replacement character length
- [ ] Template tests

## Credits

Victor Zhou's [profanity-check](https://github.com/vzhou842/profanity-check) Python package does all the heavy lifting.

Inspired by [django-profanity-filter](https://github.com/ReconCubed/django-profanity-filter).
