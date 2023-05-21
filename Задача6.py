ticket = input("Введите номер билета: ") # просим пользователя ввести номер билета
if len(ticket) != 6 or not ticket.isdigit(): # проверяем, что номер состоит из 6 цифр
    print("Некорректный номер билета")
else:
    sum_first = int(ticket[0]) + int(ticket[1]) + int(ticket[2]) # считаем сумму первых трех цифр
    sum_last = int(ticket[3]) + int(ticket[4]) + int(ticket[5]) # считаем сумму последних трех цифр
    if sum_first == sum_last:
        print("yes")
    else:
        print("no")