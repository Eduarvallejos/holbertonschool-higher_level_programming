#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0

            if type(element_1) != int or type(element_2) != int:
                raise TypeError("wrong type")

            if element_2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = element_1 / element_2
            result.append(division_result)

        except (TypeError, ZeroDivisionError) as e:
            print(f"{e}")
            result.append(0)
        finally:
            pass

    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
        for _ in range(list_length - max(len(my_list_1), len(my_list_2))):
            result.append(0)

    return resul
