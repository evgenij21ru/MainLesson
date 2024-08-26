int_1= int(input('Введите 1-ое число:'))
int_2= int(input('Введите 2-ое число:'))
int_3 = int(input('Введите 3-е число:'))
if int_1==int_2==int_3 :
    print('3')
elif int_1==int_2 or int_1==int_3 or int_2==int_3:
    print('2')
else:
    print('0')