import random
import winsound

#generate a random melody

c = 523
d = 587
e = 659
f = 698
g = 784
a = 880
b = 988
c2 = 1046
scale = [c,d,e,f,g,a,b,c2]

n4 = 400 #quarter note
n2 = 800 #half note
n1 = 1600 #whole note
notes = [n1, n2, n4]

t = 0

#1 bar = 1600 length
#4 bars = 6400

print(c, n4)
winsound.Beep(c, n4) #first note C 1/4note
for i in range(15):       #loop to randomize notes
    hz = random.choice(scale)
    length = random.choice(notes)
    print(hz, length)
    winsound.Beep(hz, length)
    t = t + length
    if t >= 6400:          #attempt to keep the melody to 4 bars
        break
print(c, n2, t)    
winsound.Beep(c, n2)

