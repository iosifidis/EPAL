# -*- coding: cp1253 -*-
'''
�� �������� �������� ��� ������� ���� ������� ������ ��������� �� ���
����������. � ������� �������� ���� ����� ������� ������ ��� �� 1 ��� �� 500
��� � ����������� ��������� �� �������� ��� ����� ������ ���������������� ��
���� ����� ����������� (5 ����������). 
�� ������� ��������� ��� �� �������� ��� ��������� ��� ���������� �� ����: 
�. �������� ��� ����� ������ ��� ������. 
�. ���������� ����� � ��� �������� ��������� ���� ��������� �������� ���
�� 1 �� �� 500 �� ������� �����. 
�. ��������� �� ������ ��� �������� ���������� ��� �� "��������" ��� �����
������ ��������������� �� ���� ����� ����������� (5 ����������). 
�. ��������� �� ������ "������� ����� � �����������" �� ���� ���� 5
����������� ���� ���������� � ������ ������� � ����������� �� ������
"������� ����� � �������". 
'''
def diadiki(lista,key):
    first=0
    last=len(lista)-1
    found=False
    try=0
    while first<=last and not found and try<5:
        mid=(first+last)/2
        if lista[mid]==key:
            found=True
        elif lista[mid]<key:
            first=mid+1
        else:
            last=mid-1
        try=try+1
    return found

krifos=int(input("Dose arithmos eos 500:"))
A=range(1,501)
if search(A,krifos):
    print "Nikitis o H/Y"
else:
    print "Nikitis o paiktis"




