#!/usr/bin/python
# -*- coding: utf-8 -*-

mo=0.06
sms=0.15
net=0.4
fpa=0.24
pagio=12
omilia=input ("Δώσε μονάδες ομιλίας: ")
minimata=input ("Δώσε αριθμό μηνυμάτων: ")
internet=input ("Δώσε αριθμό GB: ")
xr_om=omilia*mo
xr_sms=sms*minimata
xr_net=internet*net
sinolo=xr_om + xr_sms + xr_net
xr_fpa=sinolo * fpa
teliko=pagio + sinolo + xr_fpa
print "Το ΦΠΑ είναι: ",xr_fpa
print "Το τελικό ποσό πληρωμής είναι: ",teliko
