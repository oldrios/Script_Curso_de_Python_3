from random import random
from time import sleep

journey = []


def begin_the_journey():
    willpower = True
    while willpower is True:
        problem = random()
        print("\nWell, well it's seems that you have a problem here.\n")
        if problem not in journey:
            print("Don't be afraid!\nPrepare yourself and Resolve!")
            progress = '|'
            for n in range(10):
                progress += '|'
                print(progress, end='')
                sleep(0.5)
            solution = input('\nFound a solution? [y/n]: ')
            if solution.lower() == 'y':
                journey.append(problem)
                print('Problem resolved, acquired knowleged!\n'
                      'Celebrate! Continue to the next step\n')
                continue
            else:
                print('\nTry again!')
                sleep(2)
                continue
        else:
            print('Celebrate! Continue to the next step')


begin_the_journey()