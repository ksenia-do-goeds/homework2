def raise_to_power():
    user_input = input("Введите числа через пробел: ")
    degree = int(input("Введите степень: "))
    numbers = []
    
    for element in user_input.split():
        if element.lstrip('-').isdigit():
            numbers.append(int(element) ** degree)
        else:
            numbers.append(element * degree)
            
    print("Вывод:", ' '.join(map(str, numbers)))

raise_to_power()
