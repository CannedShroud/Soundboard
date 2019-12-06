import winsound as wp
 
playSwitch = input('Enter if you want contnuous sounds...(Y/N) --> ')
freq = int(input('Enter the desired frequency --> '))
play = False
playContinuous = False
i = 0

# for i in range(0, 100):	 
# 	winsound.Beep(freq, dur)	 
# 	freq+= 20
# 	dur+= 10

if playSwitch == 'y' or playSwitch == 'Y':
    dur = 1000 * (int(input('Enter the number of seconds you want the tone to play before repeating --> ')))
    playContinuous = True
else:
    dur = 1000 * (int(input('Enter the number of seconds you want it to play for --> ')))
    play = True

if play: 
    wp.Beep(freq, dur)
    play = False
if playContinuous: 
    while i < 1: 
        wp.Beep(freq, dur)