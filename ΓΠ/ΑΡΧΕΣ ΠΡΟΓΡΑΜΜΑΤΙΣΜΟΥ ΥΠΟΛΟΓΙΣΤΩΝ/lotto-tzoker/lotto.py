# -*- coding: utf-8 -*-

import random

number1 = random.randint(1, 49)
number2 = random.randint(1, 49)
number3 = random.randint(1, 49)
number4 = random.randint(1, 49)
number5 = random.randint(1, 49)
number6 = random.randint(1, 49)


while True:
    if number1!=number2 and number1!=number3 and number1!=number4 and number1!=number5 and number1!=number6 and number2!=number3 and number2!=number4 and number2!=number5 and number2!=number6 and number3!=number4 and number3!=number5 and number3!=number6 and number4!=number5 and number4!=number6 and number5!=number6:
        break
    
print "Θα σας πω τι αριθμούς να παίξετε στο ΛΟΤΤΟ"
print ""
print "Παίξε τους 6 αριθμούς :",number1,number2,number3,number4,number5,number6 

# Footer
print ''
print 'Μην παραχαράσετε την ιστορία.'
print 'Ευχαριστούμε για την προτίμησή σας.'
print ''
print 'Copyleft 2019, Efstathios Iosifidis'
