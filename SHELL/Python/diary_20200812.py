Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> f
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f
NameError: name 'f' is not defined
f
>>> 
>>> f
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f
NameError: name 'f' is not defined
f
>>> 
>>> ff
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ff
NameError: name 'ff' is not defined
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> a = 10
>>> print(a)
10
>>> print(a.real)
10
>>> print(a.
