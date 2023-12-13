# melody_generator
# Script that generates a melody based on the desired key and length, notes have random durations

import random
import time

import numpy as np
import pyaudio

# text values of the notes in each scale
C_major_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
D_major_notes = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
E_major_notes = ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
F_major_notes = ['F', 'G', 'A', 'A#', 'C', 'D', 'E']
G_major_notes = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
A_major_notes = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
B_major_notes = ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']

# frequency values for the scales
C_major = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
D_major = [293.66, 329.63, 369.99, 392.00, 440.00, 493.88, 554.37]
E_major = [329.63, 369.99, 415.30, 440.00, 493.88, 554.37, 622.25]
F_major = [349.23, 392.00, 440.00, 466.16, 523.25, 587.33, 659.26]
G_major = [392.00, 440.00, 493.88, 523.25, 587.33, 659.26, 739.99]
A_major = [440.00, 493.88, 554.37, 587.33, 659.26, 739.99, 830.61]
B_major = [493.88, 554.37, 622.25, 659.26, 739.99, 830.61, 932.33]

# create melody freq list
melody = []

# create melody notes list
melody_notes = []


def melodyGen(keyText):
    while len(melody_notes) < length:
        i = random.randint(0, len(key) - 1)
        melody.append(key[i])
        melody_notes.append(keyText[i])
'''
    print('melody frequency: ')
    print(melody)
    print('melody notes: ')
    print(melody_notes)

    return melody_notes
'''

def play_sine_wave(frequency, duration, volume=0.25):
    p = pyaudio.PyAudio()

    fs = 44100  # sampling rate, Hz, must be an integer
    
    # uncomment this line if you want a square wave instead of a sine wave
    # samples = np.sign(np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)).astype(np.float32)
    
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)).astype(np.float32)
    output_bytes = (volume * samples).tobytes()

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    start_time = time.time()
    stream.write(output_bytes)
    print("{:.2f} seconds".format(time.time() - start_time))

    stream.stop_stream()
    stream.close()

    p.terminate()


# user input validation

allowedKeys = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
while True:
    userInputKey = input("Enter key (A B C D E F G):   ")
    if len(userInputKey) == 1 and str.upper(userInputKey) in allowedKeys:
        break
    else:
        print("Invalid input. Try again.\n")

while True:
    try: 
        length = int(input("\nEnter melody length (whole number):   "))
        break
    except ValueError:
        print("Please enter an integer.\n")


if str.upper(userInputKey) == 'A':
    key = A_major
    keyText = A_major_notes
elif str.upper(userInputKey) == 'B':
    key = B_major
    keyText = B_major_notes
elif str.upper(userInputKey) == 'C':
    key = C_major
    keyText = C_major_notes
elif str.upper(userInputKey) == 'D':
    key = D_major
    keyText = D_major_notes
elif str.upper(userInputKey) == 'E':
    key = E_major
    keyText = E_major_notes
elif str.upper(userInputKey) == 'F':
    key = F_major
    keyText = F_major_notes
elif str.upper(userInputKey) == 'G':
    key = G_major
    keyText = G_major_notes

melodyGen(keyText)

duration_range = (0.15, 0.25)  # Adjust the range of durations as needed

for note, note_name in zip(melody, melody_notes):
    random_duration = random.uniform(*duration_range)
    print("")
    print(note_name)
    play_sine_wave(note, random_duration)    
    time.sleep(0)
