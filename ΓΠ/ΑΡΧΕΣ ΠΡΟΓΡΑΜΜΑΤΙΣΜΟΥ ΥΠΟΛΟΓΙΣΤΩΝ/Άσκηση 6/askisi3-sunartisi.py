# -*- coding: cp1253 -*-

import math

# ������ ���� X
x=int(input('����� ������ x:'))

# �������� �������������
if x<=0:
    print 3*(x**2)+1
elif 0<x and x<=3:
    print 2*x+1
else:
    print math.sqrt(46+x)

print ''
print ''
print '��� ������ ������������� �� ��������� ��� ����� ������������. ������������ ��� ��� ��������� ���.'
print ''
print 'Copyleft 2018, Efstathios Iosifidis'

