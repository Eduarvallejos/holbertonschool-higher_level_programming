#!/usr/bin/python3

import dis
with open("hide_4.pyc", "rb") as f:
    code = f.read()

code_obj = compile(code, "hide_4.pyc", "exec")

names = [name for name in code_obj.co_names if not name.startswith("__")]
print(names)
