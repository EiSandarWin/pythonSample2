#week 2A 14.9.2019

print('"I can do everything Nothing Impossible"')
print("'I can do everything Nothing Impossible'")
--------------------------------------------
x="Hello World!"
print(x)
--------------------------------------
>>> 5 * 'Hello' + 'World'
'HelloHelloHelloHelloHelloWorld'
>>> x = 'Hello' + 'world'
>>>
>>> x = 'Hello' + 'world'
>>> x
'Helloworld'
>>> x = 'Hello' + ' ' + 'World'
>>> x
'Hello World'
>>> x = 'Hello' + str(1)
>>> x
'Hello1'
>>> int("3") + 3
6
>>> x = "Programming"

P  r  o  g  r  a  m  m  i  n  g
>>> x [6]
'm'
>>> x [10]
'g'
>>> x [0]
'P'
>>> x[0:6]
'Progra'
>>> x[1:5]
'rogr'
>>> x[:7]
'Program'
>>> x[7:]
'ming'
>>> x[:]
'Programming'
>>> x[8:]
'ing'
>>> x[]
  File "<stdin>", line 1
    x[]
      ^
SyntaxError: invalid syntax
>>> x[-4]
'm'
>>> x[-6]
'a'
>>> x[5:-4]
'am'
>>> x[-5:0]
''
>>> x[-4]
'm'
>>> x[-6]
'a'
>>> x[5:-4]
'am'
>>> x = "Programming"
>>> x[:3] + x[4:]
'Proramming'
>>> x[:3] * 5
'ProProProProPro'

 >>> (x[:3] + " ") * 5
'Pro Pro Pro Pro Pro '
>>> x = "Programming"
>>> x[0] ='Q'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> x
'Programming'
>>> x = "Programming"
>>> x[0:4] + 'ram'
'Program'
>>> x[0:5] + 'Python'
'ProgrPython'
>>> len(x)
11
>>> len(x[5]) + 4
5
>>> len(x[5])
1
>>> len(x[5:9]) + 4
8
>>> len(x) + 4
15
[1, 3, 5, 7, 9, 11, 13, 15]
>>> word[5]
11


x = "Programming"  # string
 word = [1, 3, 5, 7, 9, 11, 13, 15]
 word = [p, r, o, g, r, a,  m,  m, i , n, g]
 >>> word[4] - 10
 >>> word = [1, 3, 5, 7, 9, 11, 13, 15]
>>> word + word
[1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11, 13, 15]
>>> word[4:6] + word[5] + len(word[5:0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list


>>> word[:] + [2, 4, 6, 8, 10]
[1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10]
>>> a = [1, 3, 5, 7, 9]
>>> b= [2, 4, 6, 8, 10]
>>> x = a + b
>>> x
[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
>>> c = ["A", "B","C", "D", "E"]
>>> x = a + b + c
>>> x
[1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 'A', 'B', 'C', 'D', 'E']
>>> x =[a, b, c]
>>> x
[[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], ['A', 'B', 'C', 'D', 'E']]
>>> x[1:3]
[[2, 4, 6, 8, 10], ['A', 'B', 'C', 'D', 'E']]