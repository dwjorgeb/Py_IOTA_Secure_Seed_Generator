# Author: Jorge Batista @ Route Technologies [jorge.batista@route.technology]
# Secure IOTA seed Generator, using Python 3.6+
# Should work on all systems

import secrets
import string


def main():
    print('IOTA Secure Seed Generator by Route Technologies [http://route.technology]')
    print('Any question or suggestion let me know: jorge.batista@route.technology')
    sequence = string.ascii_uppercase + "9"
    print('Generating secure seed based on these chars: [{0}]'.format(sequence))
    seed = ''.join((secrets.choice(sequence) for i in range(81)))
    print('\nYour seed is: \n{}'.format(seed))


if __name__ == '__main__':
    main()
