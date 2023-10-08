#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = None
    except Exception as e:
        print("Ocurrió un error:", e)
        resultado = None
    finally:
        if resultado is not None:
            print("Inside result: {}".format(resultado))
        else:
            print("Inside result: None")
        return resultado
