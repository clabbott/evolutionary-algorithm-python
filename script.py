from classes import Environment

# Global parameters 
CYCLE_COUNT = 0
MAX_CYCLES = 5
DEBUG = True

env = Environment()


# BEGIN CYCLE 
while CYCLE_COUNT!=MAX_CYCLES:
    if DEBUG:
        print("BOC" , CYCLE_COUNT)

    if DEBUG:
        print("Environment debug:",env.i, env.f())

    if DEBUG:
        print("EOC" , CYCLE_COUNT)
    CYCLE_COUNT+=1
