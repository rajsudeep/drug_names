from random import choice, randint
import constants as c


def adj_organ():
    return '{} {}'.format(
        choice(c.ADJECTIVES),
        choice(c.BODY_PARTS)
    )


def color_bile():
    return 'an excess of {} bile'.format(
        choice(c.COLORS).lower()
    )


def superlative_symptom():
    return '{} {}'.format(
        choice(c.SUPERLATIVES),
        choice(c.SYMPTOMS)
    )

def hot_noun():
    return 'HEY YOU {}\n'.format(
        choice(c.NOUNS)
    )


def disease():
        return hot_noun()


# for testing
if __name__ == '__main__':
    print(disease())
