#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else None
            element_2 = my_list_2[i] if i < len(my_list_2) else None

            if element_1 is None or element_2 is None:
                raise IndexError
            division_result = element_1 / element_2
            result.append(division_result)

        except TypeError as e:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError as e:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
