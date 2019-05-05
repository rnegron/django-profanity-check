import pytest
from profanity.templatetags.profanity import censor


@pytest.mark.parametrize("word", ["fuck", "shit", "cunt", "ass"])
def test_censors_profane_words(word):
    assert censor(word) == ("*" * len(word))


@pytest.mark.parametrize("word", ["fudge", "poop", "baddie", "butt"])
def test_does_not_censor_other_words(word):
    assert censor(word) == word


@pytest.mark.parametrize(
    "sentence",
    [
        "Fuck you!",
        "You are a piece of shit",
        "Wow, what a cunt.",
        "Thanks for being an asshole",
    ],
)
def test_censors_words_in_sentences(sentence):
    assert "*" in censor(sentence)


@pytest.mark.parametrize(
    "sentence",
    [
        "Screw you!",
        "You are a bad person",
        "Wow, what a doodoo head",
        "Thanks for being a meanie",
    ],
)
def test_does_not_censor_other_words_in_sentences(sentence):
    assert sentence == censor(sentence)
