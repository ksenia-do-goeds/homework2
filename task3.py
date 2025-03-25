def intersection_of_lists():
    first_list = input("Введите первый список: ").split()
    second_list = input("Введите второй список: ").split()
    
    first_set = set(first_list)
    second_set = set(second_list)
    
    common_elements = first_set & second_set
    
    print("Общие элементы:", ' '.join(common_elements))

intersection_of_lists()
