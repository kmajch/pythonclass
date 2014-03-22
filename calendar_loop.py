Last login: Sat Feb  1 13:12:08 on ttys001
kristin-majchers-MacBook-Pro:~ kristinmajcher$ python
Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> >>> address = raw_input("What is your address?")
... address = raw_input("What is your address?")
  File "<stdin>", line 2
    address = raw_input("What is your address?")
          ^
SyntaxError: invalid syntax
>>> address = raw_input("What is your address?")
What is your address? !421 Chapin St NW
>>> print address
 !421 Chapin St NW
>>> nw_addresses = [ ] 
>>> ne_addresses = [ ]
>>> sw_addresses = [ ]
>>> se_addresses = [ ]
>>> address = address.split(' ")
  File "<stdin>", line 1
    address = address.split(' ")
                               ^
SyntaxError: EOL while scanning string literal
>>> address = address.split(' ')
>>> print address
['', '!421', 'Chapin', 'St', 'NW']
>>> if 'NW' in address:
... nw_addresses.append(address)
  File "<stdin>", line 2
    nw_addresses.append(address)
               ^
IndentationError: expected an indented block
>>> nw_addresses.append(address)
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> clear()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> delete()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'delete' is not defined
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> address = "1133 19th St"
>>> address = address.split(' ')
>>> print address
['1133', '19th', 'St']
>>> for number in range(len(address))
  File "<stdin>", line 1
    for number in range(len(address))
                                    ^
SyntaxError: invalid syntax
>>> for number in range(len(address)
... print range
  File "<stdin>", line 2
    print range
        ^
SyntaxError: invalid syntax
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
kristin-majchers-MacBook-Pro:~ kristinmajcher$ cd desktop
kristin-majchers-MacBook-Pro:desktop kristinmajcher$ cd pyscripts
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges.py
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Week 1
Week 2
Week 3
Week 4
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Week 1
Traceback (most recent call last):
  File "ranges2.py", line 4, in <module>
    for day in days_of_week:
NameError: name 'days_of_week' is not defined
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Week 1
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
Week 2
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
Week 3
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
Week 4
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ 
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Week 1
()
Monday
()
Tuesday
()
Wednesday
()
Thursday
()
Friday
()
Saturday
()
Sunday
()
Week 2
()
Monday
()
Tuesday
()
Wednesday
()
Thursday
()
Friday
()
Saturday
()
Sunday
()
Week 3
()
Monday
()
Tuesday
()
Wednesday
()
Thursday
()
Friday
()
Saturday
()
Sunday
()
Week 4
()
Monday
()
Tuesday
()
Wednesday
()
Thursday
()
Friday
()
Saturday
()
Sunday
()
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
  File "ranges2.py", line 9
    print "((((((((((()))))))))))""
                                  ^
SyntaxError: EOL while scanning string literal
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Week 1
((((((((((()))))))))))
Monday
((((((((((()))))))))))
Tuesday
((((((((((()))))))))))
Wednesday
((((((((((()))))))))))
Thursday
((((((((((()))))))))))
Friday
((((((((((()))))))))))
Saturday
((((((((((()))))))))))
Sunday
((((((((((()))))))))))
Week 2
((((((((((()))))))))))
Monday
((((((((((()))))))))))
Tuesday
((((((((((()))))))))))
Wednesday
((((((((((()))))))))))
Thursday
((((((((((()))))))))))
Friday
((((((((((()))))))))))
Saturday
((((((((((()))))))))))
Sunday
((((((((((()))))))))))
Week 3
((((((((((()))))))))))
Monday
((((((((((()))))))))))
Tuesday
((((((((((()))))))))))
Wednesday
((((((((((()))))))))))
Thursday
((((((((((()))))))))))
Friday
((((((((((()))))))))))
Saturday
((((((((((()))))))))))
Sunday
((((((((((()))))))))))
Week 4
((((((((((()))))))))))
Monday
((((((((((()))))))))))
Tuesday
((((((((((()))))))))))
Wednesday
((((((((((()))))))))))
Thursday
((((((((((()))))))))))
Friday
((((((((((()))))))))))
Saturday
((((((((((()))))))))))
Sunday
((((((((((()))))))))))
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Week 1
((((((((((()))))))))))
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
((((((((((()))))))))))
Week 2
((((((((((()))))))))))
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
((((((((((()))))))))))
Week 3
((((((((((()))))))))))
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
((((((((((()))))))))))
Week 4
((((((((((()))))))))))
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
((((((((((()))))))))))
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
Traceback (most recent call last):
  File "ranges2.py", line 3, in <module>
    for month in months_in_year:
NameError: name 'months_in_year' is not defined
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
January
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
February
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
March
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
April
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
May
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
June
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
July
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
August
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
September
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
October
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
November
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
December
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
January
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
February
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
March
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
April
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
May
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
June
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
July
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
August
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
September
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
October
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
November
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
December
VVVVVVVVVVVVVVV
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
January
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
February
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
March
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
April
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
May
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
June
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
July
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
August
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
September
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
October
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
November
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
December
------------------
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
January
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
February
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
March
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
April
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
May
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
June
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
July
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
August
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
September
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
October
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
November
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
December
>>>>>>>>>>>>>>>>>>>>>
Week 1
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 2
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 3
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
Week 4
------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
  File "ranges2.py", line 5
    print \n 
            ^
SyntaxError: unexpected character after line continuation character
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
January


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
February


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
March


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
April


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
May


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
June


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
July


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
August


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
September


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
October


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
November


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
December


>>>>>>>>>>>>>>>>>>>>>
Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
January


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
February


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
March


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
April


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
May


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
June


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
July


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
August


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
September


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
October


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
November


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
December


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ python ranges2.py
January


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
February


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
March


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
April


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
May


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
June


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
July


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
August


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
September


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
October


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
November


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
December


>>>>>>>>>>>>>>>>>>>>>


Week 1


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 2


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 3


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
Week 4


------------------
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


------------------
kristin-majchers-MacBook-Pro:pyscripts kristinmajcher$ 
