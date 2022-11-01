"""
x = 'a,b=1,2\nprint("a + b = ", a+b)'
eval()
this does not work, it should be passed to code obj
also, it cannot interact with local object 
"""

x = 'print("hello")'
eval(x)

src = x = 'a,b=1,2\nprint("a + b = ", a+b)'
code_obj = compile(src, 'testing', 'exec')
eval(code_obj)
