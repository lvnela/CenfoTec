#!/usr/bin/env python
# coding: utf-8

# In[7]:


the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")


# In[9]:


# -*- coding: cp1252 -*-


# In[12]:


# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."


# In[17]:


2 + 2


# In[18]:


50 - 5*6


# In[19]:


8 / 5  # division always returns a floating point number


# In[20]:


17 / 3  # classic division returns a float


# In[21]:


17 // 3  # floor division discards the fractional part


# In[22]:


17 % 3  # the % operator returns the remainder of the division


# In[23]:


5 * 3 + 2  # result * divisor + remainder


# In[24]:


5 ** 2  # 5 squared


# In[25]:


2 ** 7  # 2 to the power of 7


# In[26]:


width = 20
height = 5 * 9
width * height


# In[27]:


n  # try to access an undefined variable


# In[28]:


4 * 3.75 - 1


# In[29]:


tax = 12.5 / 100
price = 100.50
price * tax


# In[30]:


price + _


# In[31]:


round(_, 2)


# In[33]:


'spam eggs'  # single quotes


# In[34]:


'doesn\'t'  # use \' to escape the single quote...


# In[35]:


"doesn't"  # ...or use double quotes instead


# In[36]:


'"Yes," they said.'


# In[37]:


"\"Yes,\" they said."


# In[38]:


'"Isn\'t," they said.'


# In[39]:


'"Isn\'t," they said.'


# In[40]:


print('"Isn\'t," they said.')


# In[41]:


s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output


# In[42]:


print(s)  # with print(), \n produces a new line


# In[43]:


print('C:\some\name')  # here \n means newline!


# In[44]:


print(r'C:\some\name')  # note the r before the quote


# In[45]:


print("""Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# In[46]:


# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium


# In[47]:


'Py' 'thon'


# In[48]:


text = ('Put several strings within parentheses '
        'to have them joined together.')
text


# In[49]:


prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^


# In[50]:


('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^


# In[54]:


prefix = 'Py'
prefix + 'thon'


# In[55]:


word = 'Python'
word[0]  # character in position 0


# In[56]:


word[-6]


# In[57]:


word[0:2]  # characters from position 0 (included) to 2 (excluded)


# In[58]:


word[2:5]  # characters from position 2 (included) to 5 (excluded)


# In[59]:


word[:2] + word[2:]


# In[60]:


word[:4] + word[4:]


# In[61]:


word[:2]


# In[62]:


word[42]  # the word only has 6 characters


# In[63]:


word[4:42]


# In[64]:


word[42:]


# In[65]:


word[0] = 'J'


# In[66]:


word[2:] = 'py'


# In[67]:


'J' + word[1:]


# In[68]:


word[:2] + 'py'


# In[69]:


s = 'supercalifragilisticexpialidocious'
len(s)


# In[70]:


squares = [1, 4, 9, 16, 25]
squares


# In[71]:


squares[0]  # indexing returns the item


# In[72]:


squares[-1]


# In[74]:


squares[-3:]  # slicing returns a new list


# In[75]:


squares[:]


# In[76]:


squares + [36, 49, 64, 81, 100]


# In[77]:


cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!


# In[78]:


cubes[3] = 64  # replace the wrong value
cubes


# In[79]:


cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes


# In[80]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters


# In[81]:


# replace some values
letters[2:5] = ['C', 'D', 'E']
letters


# In[82]:


# now remove them
letters[2:5] = []
letters


# In[83]:


# clear the list by replacing all the elements with an empty list
letters[:] = []
letters


# In[84]:


letters = ['a', 'b', 'c', 'd']
len(letters)


# In[85]:


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x


# In[86]:


x[0]


# In[87]:


x[0][1]


# In[88]:


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


# In[89]:


i = 256*256
print('The value of i is', i)


# In[92]:


a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


# In[94]:


x = int(input("Please enter an integer: "))


# In[95]:


if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[96]:


# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[101]:


for i in range(5):
    print(i)


# In[102]:


range(5, 10)


# In[103]:


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# In[104]:


print(range(10))
range(0, 10)


# In[105]:


sum(range(4))  # 0 + 1 + 2 + 3


# In[106]:


list(range(4))


# In[107]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# In[ ]:


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


# In[ ]:


while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# In[ ]:


class MyEmptyClass:
    pass


# In[ ]:


def initlog(*args):
    pass   # Remember to implement this!


# In[1]:


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[2]:


# Now call the function we just defined:
fib(2000)


# In[4]:


fib
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
f = fib
f(100)


# In[6]:


fib(0)
print(fib(0))


# In[7]:


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result


# In[9]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[10]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[11]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[12]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[13]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[14]:


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[15]:


parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument


# In[16]:


def function(a):
    pass

function(0, a=0)


# In[17]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[18]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[37]:


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg):
    print(arg)

def kwd_only_arg(arg):
    print(arg)

def combined_example(pos_only, standard, kwd_only):
    print(pos_only, standard, kwd_only)


# In[38]:


standard_arg(2)


# In[39]:


standard_arg(arg=2)


# In[40]:


def pos_only_arg(arg):
    print(arg)


# In[41]:


pos_only_arg(1)


# In[42]:


kwd_only_arg(arg=3)


# In[43]:


combined_example(1, 2, kwd_only=3)


# In[44]:


combined_example(1, standard=2, kwd_only=3)


# In[45]:


def foo(name, **kwds):
    return 'name' in kwds


# In[49]:


def foo(name,kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})


# In[52]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[53]:


def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'


# In[54]:


list(range(3, 6))            # normal call with separate arguments


# In[55]:


args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list


# In[56]:


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# In[57]:


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)


# In[58]:


f(1)


# In[59]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


# In[60]:


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


# In[61]:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')


# In[62]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')


# In[63]:


fruits.count('tangerine')


# In[64]:


fruits.index('banana')


# In[65]:


fruits.index('banana', 4)  # Find next banana starting a position 4


# In[66]:


fruits.reverse()
fruits


# In[67]:


fruits.append('grape')
fruits


# In[68]:


fruits.sort()
fruits


# In[69]:


fruits.pop()


# In[70]:


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack


# In[71]:


stack.pop()


# In[72]:


stack


# In[73]:


stack.pop()


# In[74]:


stack.pop()


# In[75]:


stack


# In[76]:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves


# In[77]:


queue.popleft()                 # The second to arrive now leaves


# In[78]:


queue                           # Remaining queue in order of arrival


# In[79]:


squares = []
for x in range(10):
    squares.append(x**2)

squares


# In[81]:


squares = list(map(lambda x: x**2, range(10)))


# In[82]:


squares = [x**2 for x in range(10)]


# In[83]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[84]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs


# In[85]:


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]


# In[86]:


# filter the list to exclude negative numbers
[x for x in vec if x >= 0]


# In[87]:


# apply a function to all the elements
[abs(x) for x in vec]


# In[88]:


# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]


# In[89]:


# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]


# In[90]:


# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]


# In[91]:


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# In[92]:


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# In[93]:


[[row[i] for row in matrix] for i in range(4)]


# In[94]:


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed


# In[95]:


for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed


# In[96]:


list(zip(*matrix))


# In[97]:


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a


# In[98]:


del a[2:4]
a


# In[99]:


del a[:]
a


# In[100]:


del a


# In[101]:


t = 12345, 54321, 'hello!'
t[0]


# In[102]:


t


# In[103]:


# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u


# In[104]:


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v


# In[105]:


empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)


# In[106]:


len(singleton)


# In[107]:


singleton


# In[108]:


x, y, z = t


# In[109]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) 


# In[110]:


'orange' in basket                 # fast membership testing


# In[111]:


'crabgrass' in basket


# In[112]:


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a


# In[113]:


a - b   


# In[114]:


a | b                              # letters in a or b or both


# In[115]:


a | b                              # letters in a or b or both


# In[116]:


a ^ b                              # letters in a or b but not both


# In[117]:


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel


# In[118]:


tel['jack']


# In[119]:


del tel['sape']
tel['irv'] = 4127
tel


# In[120]:


list(tel)


# In[121]:


sorted(tel)


# In[122]:


'guido' in tel


# In[123]:


'jack' not in tel


# In[124]:


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]


# In[125]:


{x: x**2 for x in (2, 4, 6)}


# In[126]:


dict(sape=4139, guido=4127, jack=4098)


# In[127]:


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


# In[128]:


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[129]:


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# In[130]:


for i in reversed(range(1, 10, 2)):
    print(i)


# In[131]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


# In[132]:


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data


# In[133]:


string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null


# In[ ]:




