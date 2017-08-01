import sys
import math
import wave
import array

DURATION = 1
FREQUENCY = 440
VOLUME = 100
SAMPLERATE = 44100
DATASIZE = 2
CHANNEL = 2
RANGE = (2 << 14) - 1


solfege_steps = [-9,-7,-5,-4,-2,0,2]

if __name__ == '__main__':

    data = array.array('h')
    for step in solfege_steps:
      freq_num = (2**(step/12))*FREQUENCY
      freq_int = int(freq_num)
      fpr = int(SAMPLERATE / freq_int)
      samples_length = SAMPLERATE * DURATION * CHANNEL

      for i in range(samples_length):
          sample = RANGE * float(VOLUME) / 100
          sample *= math.sin(math.pi * 2 * (i % fpr) / fpr)
          data.append(int(sample))

    f = wave.open('solfege.wav', 'w')
    f.setparams((CHANNEL, DATASIZE, SAMPLERATE, samples_length, "NONE", "Uncompressed"))
    f.writeframes(data.tostring())
    f.close()
