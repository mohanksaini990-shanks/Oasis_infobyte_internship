unit = input('Is the temp in celcius or fahrenheit (c/f):')
temp = float(input('temp:'))
if unit =='c':
    temp = (9*temp)/5 + 32
    print(f'Temp:{temp} {unit}')
elif unit =='f':
    temp =(temp - 32)*5/9
    print(f'Temp{temp} {unit}')
else :
    print(f'not valid unit ')    