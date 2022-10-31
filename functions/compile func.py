python_code = "a,b=3,4\nprint(f'a + b = {a+b}')"

python_obj = compile(python_code, 'testing', 'exec')
exec(python_obj)

"""
OUTPUT: 
a + b = 7
"""
