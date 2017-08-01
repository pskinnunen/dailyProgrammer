
try:
    import winsound
except ImportError:
    import os
    def playsound(frequency, duration):
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency, duration):
        winsound.Beep(frequency,duration)

solfege_steps = [-9,-7,-5,-4,-2,0,2]

def main ():
    a_frequency = 440
    for step in solfege_steps:
        freq_num = (2**(step/12))*a_frequency
        freq_int = int(freq_num)
        winsound.Beep(freq_int,1000)

if __name__ == '__main__':
    main()
