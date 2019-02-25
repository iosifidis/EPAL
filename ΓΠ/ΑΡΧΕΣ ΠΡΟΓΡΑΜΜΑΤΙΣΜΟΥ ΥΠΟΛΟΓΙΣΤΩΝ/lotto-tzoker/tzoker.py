# -*- coding: utf-8 -*-

import random

number1 = random.randint(1, 45)
number2 = random.randint(1, 45)
number3 = random.randint(1, 45)
number4 = random.randint(1, 45)
number5 = random.randint(1, 45)
tzoker = random.randint(1, 20)

while True:
    if number1!=number2 and number1!=number3 and number1!=number4 and number1!=number5 and number2!=number3 and number2!=number4 and number2!=number5  and number3!=number4 and number3!=number5:
        break

print "Θα σας πω τι αριθμούς να παίξετε στο Τζόκερ"
print ""
print "Παίξε τους 5 αριθμούς :",number1,number2,number3,number4,number5
print "Και ως τζόκερ το :",tzoker

# Footer
print ''
print 'Μην παραχαράσετε την ιστορία.'
print 'Ευχαριστούμε για την προτίμησή σας.'
print ''
print 'Copyleft 2019, Efstathios Iosifidis'
