from random import choice

import constants as c
from drug_name import create_drug_name
from generate_disease import disease


def get_ad():
    sexy_shout = disease()
    compliment = choice(c.COMPLIMENTS)
    return '{}{}'.format(sexy_shout, compliment)


# for testing
if __name__ == '__main__':
    print(get_ad())
