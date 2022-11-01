"""
x = 'a,b=1,2\nprint("a + b = ", a+b)'
eval()
this does not work, it should be passe
"""

x = 'print("hello")'
eval(x)

src = x = 'a,b=1,2\nprint("a + b = ", a+b)'
code_obj = compile(src, 'testing', 'exec')
eval(code_obj)
