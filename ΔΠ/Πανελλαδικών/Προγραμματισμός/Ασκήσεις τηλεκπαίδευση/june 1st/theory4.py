# -*- coding: cp1253 -*-
'''
������� �� �������� ����� ������������ Python:
for x in range (A, M, B):
    print x 
 
��� ������� ��� ��� �������� �����������, �� ������� ���
�������� ��� ��� ����� ��� A, M, B, ���� ���� �� ����������
����� ������������ �� ��������� ����� :
�.  ���� ��������� ��� 1 ����� ��� 80 (������� �����)
�.  ���� ��������� ��� 50 ����� ��� 20 (�������� �����)  
�.  ���� ��������� ��������� ��� 81 ����� ��� 151 (�������
�����) 
�.  ���� ��������� ��� -50 ����� ��� -5 (������� �����) 
�.  ���� �������� ��������� ��� ����� ���������� ��� 200 ���
������������ ��� 7 (������� �����). 
'''

print '�\n'
for x in range (1, 81, 1):
    print x 

print '�\n'
for x in range (50, 19, -1):
    print x 

print '�\n'
for x in range (81, 152, 2):
    print x 

print '�\n'
for x in range (-50, -4, 1):
    print x 

print '�\n'
for x in range (0, 200, 7):
    print x 
