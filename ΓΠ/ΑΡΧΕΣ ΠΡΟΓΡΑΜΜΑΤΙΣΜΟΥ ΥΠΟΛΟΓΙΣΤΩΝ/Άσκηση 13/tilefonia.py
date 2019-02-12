# -*- coding: utf-8 -*-

#Εισαγωγή δεδομένων
pagio=20 # Πάγιο
sum=0 # Μηδενισμός μετρητή

for i in range(0,2):
        omilia=input ("Δώσε μονάδες ομιλίας (σε δευτερόλεπτα): ") #Εισαγωγή data
        sum=omilia+sum # Μετρητής

# Έλεγχοι
if sum>=0 and sum<=50000:
        xr_om=sum*0.02
elif sum>50000 and sum<=80000:
        xr_om=(50000*0.02)+(sum-50000)*0.009
else:
        xr_om=(50000*0.02)+(30000*0.009)+(sum-80000)*0.007

#Υπολογισμοί
teliko=pagio + xr_om

# Εκτύπωση αποτελεσμάτων
print ""
print "Μάστορα μίλησες ",sum," δεφτερόλεπτα (", sum/60," λεπτά) και πρέπει να πλερώ: ",teliko," εβρά."
print ""
print "Μιλάς πολύ. Σου προτείνω να μιλάς λιγότερο στο κινητό ή άλλαξε πάροχο."
# Footer
print ''
print 'Μην παραχαράσετε την ιστορία.'
print 'Ευχαριστούμε για την προτίμησή σας.'
print ''
print 'Copyleft 2019, Efstathios Iosifidis'
