from random import choice, randint
import constants as c


def adjective():
    return '{}'.format(
        choice(c.ADJECTIVES)
    )


def color():
    return '{}'.format(
        choice(c.COLORS)
    )


def superlative():
    return '{}'.format(
        choice(c.SUPERLATIVES)
    )

def noun():
    return '{}'.format(
        choice(c.NOUNS)
)
