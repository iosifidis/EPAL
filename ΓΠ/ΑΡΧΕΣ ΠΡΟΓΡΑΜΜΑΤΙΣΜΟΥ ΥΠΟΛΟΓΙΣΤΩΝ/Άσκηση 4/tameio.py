# δεδομένα 1
timi=float(input('Τιμή προϊόντος/κιλού:'))
posotita=float(input('Ποσότητα/βάρος προϊόντος:'))

# επεξεργασία - υπολογισμοί
synolo=timi * posotita
fpa= synolo * 24/100
posopliromis= synolo + fpa

#εμφάνιση τελικού ποσού μαζί με ΦΠΑ
print 'τελικό ποσό μαζί με ΦΠΑ:',round( posopliromis,2)

# δεδομένα 2
pliromi=float(input('Πληρωμή:'))

# υπολογισμός - ρέστα
resta = pliromi - posopliromis
# εμφάνιση ρέστα
print 'Ρέστα:',round(resta,2)
