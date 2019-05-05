## django-profanity-check

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
