import winsound
import math
solfege_steps = [-9,-7,-5,-4,-2,0,2]

def main ():
    a_frequency = 440
    for step in solfege_steps:
        winsound.Beep(int((2**(step/12))*a_frequency),1000)

if __name__ == '__main__':
    main()
