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
xr_net=internet*net
if omilia>=0 and omilia<=200:
	xr_om=omilia*0.12
if omilia>200 and omilia<=400:
	xr_om=(200*0.12)+(omilia-200)*0.09
else:
	xr_om=(200*0.12)+(200*0.09)+(omilia-400)*0.06
if minimata >=0 and minimata<=50:
	xr_sms=0
else:
	xr_sms=(minimata-50)*0.15
sinolo=xr_om + xr_sms + xr_net
xr_fpa=sinolo * fpa
teliko=pagio + sinolo + xr_fpa
print "Το ΦΠΑ είναι: ",xr_fpa
print "Το τελικό ποσό πληρωμής είναι: ",teliko
