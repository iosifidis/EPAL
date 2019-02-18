# -*- coding: cp1253 -*-

from random import *
 
number = randint(1, 100)

running = True
times=0

while running:
    guess = int(input('Εισάγετε έναν ακέραιο αριθμό από το 1 έως το 100: '))

    if guess == number:
        print'Συγχαρητήρια, τον μαντέψατε.'
        running = False 
    elif guess < number:
        print'Όχι, είναι λίγο μεγαλύτερος.'
    else:
        print'Όχι, είναι λίγο μικρότερος.'
    times=times+1
else:
    print'Ο αριθμός ήταν ο ',number,' και το μαντέψατε μετά από ',times,' φορές.'
    # Μπορείτε να προσθέσετε ότι άλλο θέλετε εδώ

# Footer
print ''
print 'Μην παραχαράσετε την ιστορία.'
print 'Ευχαριστούμε για την προτίμησή σας.'
print ''
print 'Copyleft 2019, Efstathios Iosifidis'
