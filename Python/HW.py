import random
input_digit='new'

while True:
    txt=''
    try: 
        if int(input_digit)>=1 and int(input_digit)<=10:
            if int(intinput_digit)==random_digit:
                txt='Вы выиграли.\nНачинаем новый раунд\n'
                random_digit=random.randint(1,10)
            elif  int(input_digit) > random_digit:
                txt="Много.\n"
            else:
                txt="Мало.\n"
    except:
        if input_digit=="exit":
            break
        if input_digit=="new":
            random_digit=random.randint(1,10)
            txt="Начинаем новый раунд\n"
    input_digit=input(txt+'Введите число от 1 до 10\nexit для выхода, или new для нового раунда\n')
