# -*- coding: utf-8 -*-


print "Βασικοί τριγωνομετρικοί υπολογισμοί"
# Συναρτήσεις
import math
def trigonometry ():
	num=float(input("Επιλέξτε μοίρες (εάν θέλετε να εισάγετε π/2 γράψτε math.pi/2):"))
	trigfunction=raw_input("Επιλέξτε τύπο sin (ημίτονο), cos (συνημίτονο), tan (εφαπτομένη):")
	if trigfunction=="sin":
		print (math.sin(num))
	elif trigfunction=="cos":
		print (math.cos(num))
	elif trigfunction=="tan":
		print (math.tan(num))
	else:
		print "Δεν δώσατε σωστό τριγωνομετρικό αριθμό"
# Εισαγωγή δεδομένων
trigonometry ()


# Footer
print ''
print 'Ιασο κόκλα'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
