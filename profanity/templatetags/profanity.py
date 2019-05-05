from typing import List, Tuple
from django import template
from django.template.defaultfilters import stringfilter
from profanity_check import predict

register = template.Library()


def censor_word(word: str) -> str:
    return "*" * len(word)


@register.filter(is_safe=True)
@stringfilter
def censor(text: str) -> str:
    """Censors a word or sentence and returns the censored version"""

    # Split up individual words in the text
    tokens: List[str] = text.split(" ")

    # Create a mapping of 0 if the word is okay, 1 if it should be censored
    censor_mask: List[int] = predict([word for word in tokens])

    # A list of tuples with the first element being the word and the second being 0 or 1
    censor_map: List[Tuple[str, int]] = list(zip(tokens, censor_mask))

    # A list of the words that make up the censored text
    censored_text: List[str] = [
        censor_word(word) if should_censor else word
        for word, should_censor in censor_map
    ]

    return " ".join(censored_text)
