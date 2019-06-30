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

def employment():
    return '{}'.format(
        choice(c.EMPLOYMENTS)
)

def disease():
    index = randint(0, 5)
    if index == 0:
        return color_bile()
    elif index == 1:
        return superlative_symptom()
    else:
        return adj_organ()


# for testing
if __name__ == '__main__':
    print(disease())
