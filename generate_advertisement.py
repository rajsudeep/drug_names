from random import choice

import constants as c
from generate_disease import adjective
from generate_disease import noun
from generate_disease import color


def get_ad():
    phrase = choice(c.TEST_PHRASES).format(adjective(), noun(), color(), noun())

    return '{}'.format(phrase)


# for testing
if __name__ == '__main__':
    print(get_ad())
