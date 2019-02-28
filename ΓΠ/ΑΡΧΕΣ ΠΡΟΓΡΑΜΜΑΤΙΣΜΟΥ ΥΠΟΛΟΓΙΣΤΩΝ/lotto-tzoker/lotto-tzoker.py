# -*- coding: utf-8 -*-


import random

print "Για αριθμούς επιλέξτε:"
print ""
print "1. ΛΟΤΤΟ"
print ""
print "2. ΤΖΟΚΕΡ"
print ""
print "0. Έξοδος"
print ""
prog=int(input("Εισάγετε επιλογή: "))
print ""
while prog!=0:

    if prog==1:
        lotto1 = random.randint(1, 49)
        lotto2 = random.randint(1, 49)
        lotto3 = random.randint(1, 49)
        lotto4 = random.randint(1, 49)
        lotto5 = random.randint(1, 49)
        lotto6 = random.randint(1, 49)
        if lotto1!=lotto2 and lotto1!=lotto3 and lotto1!=lotto4 and lotto1!=lotto5 and lotto1!=lotto6 and lotto2!=lotto3 and lotto2!=lotto4 and lotto2!=lotto5 and lotto2!=lotto6 and lotto3!=lotto4 and lotto3!=lotto5 and lotto3!=lotto6 and lotto4!=lotto5 and lotto4!=lotto6 and lotto5!=lotto6:
            print "Θα σας πω τι αριθμούς να παίξετε στο ΛΟΤΤΟ"
            print ""
            print "Παίξε τους 6 αριθμούς :",lotto1,lotto2,lotto3,lotto4,lotto5,lotto6
            print ""
            prog=int(input("Εισάγετε επιλογή: "))
            print ""
        
    elif prog==2:
        number1 = random.randint(1, 45)
        number2 = random.randint(1, 45)
        number3 = random.randint(1, 45)
        number4 = random.randint(1, 45)
        number5 = random.randint(1, 45)
        tzoker = random.randint(1, 20)
        if number1!=number2 and number1!=number3 and number1!=number4 and number1!=number5 and number2!=number3 and number2!=number4 and number2!=number5  and number3!=number4 and number3!=number5:
            print "Θα σας πω τι αριθμούς να παίξετε στο Τζόκερ"
            print ""
            print "Παίξε τους 5 αριθμούς :",number1,number2,number3,number4,number5
            print "Και ως τζόκερ το :",tzoker
            print ""
            prog=int(input("Εισάγετε επιλογή: "))
            print ""

    else:
        print ""
        prog=int(input("Τι δεν καταλαβαίνεις; Είπαμε 0 για να βγεις, 1 για ΛΟΤΤΟ και 2 για Τζόκερ: "))
    
# Footer
print ''
print 'Μην παραχαράσετε την ιστορία.'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
