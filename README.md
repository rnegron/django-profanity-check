## django-profanity-check

A Django template wrapper around [profanity-check](https://github.com/vzhou842/profanity-check).

## Usage

1. Install with `pip`.
	` pip install django-profanity-check`

1. Add it to `INSTALLED_APPS`.

	```python
	# settings.py
	
	# Note the underscore (_)
	INSTALLED_APPS = [ ..., 'profanity_check', ...]
		
	```
1. Use it in a template!

	 ```djangotemplate
	{# ... #}
	
	{% load profanity_check %}
	
	{# ... #}
	
	{% with sentence='Hey, fuck you!' %}
	    {{ sentence|censor }} {# Will result in:'Hey, **** you!' #}
	{% endwith %}

	```

## Todo

- [ ] Allow custom replacement characters
- [ ] Allow custom replacement character length
- [ ] Multi language support
    - [ ] Priority: Puerto Rican Spanish
- [ ] Template tests

## Credits
 

This app currently uses Victor Zhou's [profanity-check](https://github.com/vzhou842/profanity-check) Python package for all the heavy lifting.

Inspired by [django-profanity-filter](https://github.com/ReconCubed/django-profanity-filter).


<p align="center">
<br>
	<img height="100" src="/img/pr.png" alt="Hecho en 🇵🇷" />
</p>

