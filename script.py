from classes import Environment

# Global parameters 
CYCLE_COUNT = 0
MAX_CYCLES = 5
DEBUG = True
RANDOM = False
ENV = Environment()


# Environment Population
if not RANDOM: 
    ENV.fillSamples(12)

# BEGIN CYCLE 
while CYCLE_COUNT!=MAX_CYCLES:
    if DEBUG:
        print("BOC" , CYCLE_COUNT)

    if DEBUG:
        print("Environment debug:",ENV.popValues())
    
    if DEBUG:
        print("EOC" , CYCLE_COUNT)
        
    CYCLE_COUNT+=1
