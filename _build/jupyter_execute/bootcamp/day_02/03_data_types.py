#!/usr/bin/env python
# coding: utf-8

# # PYTHON Data operations 101
# 
# ## Basic Data operations
# 
# The different data types we just discussed in detail are the basic building blocks of any Python operation. 
# As I mentioned earlier, objects are copies of a template called a class. 
# Each class has a different set of methods associated with the specific operations allowed on its data type.
# 

# ### Basic Arithmetic operations on integers (whole numbers)
# 
# - As we already saw, Python has various "types" of numbers (numeric literals).
# - It also has many different operators. 
# - Arithmetic Operators perform various arithmetic calculations on these.
# 

# In[1]:


x,y = 5,4
print(f"{f'+ Addition :':<45}{f'{x} + {y} = {x+y}'}")
print(f"{f'* Multiplication :':<45}{f'{x} * {y} = {x*y}'}")
print(f"{f'/ Division :':<45}{f'{x} / {y} = {x/y}'}")
print(f"{f'- Substraction :':<45}{f'{x} - {y} = {x-y}'}")
print(f"{f'% Modulus :':<45}{f'{x} % {y} = {x%y}'}")
print(f"{f'// Floor Division :':<45}{f'{x} / {y} = {x//y}'}")
print(f"{f'** Exponent :':<45}{f'{x}^{y} = {x**y}'}")
print(f"{f'() Use parentheses to specify order :':<45}{f'{x} * ( {x}/{y} - {y} ) = {x*(x/y-y)}'}")


# `````{admonition} Challenge
# Obtain 21 using the four numbers 1, 5, 6, 7 and any arithmetic operations ( +, -, *, / ).
# ````{dropdown} Solution 
# ```{code-block} python 
# 6 / (1 - 5/7)
# ```
# ````
# `````

# ### Basic Arithmetic operations on complex numbers
# 
# - Python complex numbers are of type complex.
# - Every complex number contains one real part and one imaginary part.
# - We define imaginary numbers using the letter `j`
# 

# In[2]:


x,y = 1+1j, 2-2j
print(f"Real Parts (x = {x.real}, y = {y.real}) | Imaginary Parts = (x = {x.imag}, y = {y.imag})") 


#  `````{admonition} Challenge
# Using python solve the following equation $(-7 + 7i) - (-7 - 3i) + (-7 - 8i) = ?$
# ````{dropdown} Solution 
# ```{code-block} python 
# (-7 + 7j) - (-7 - 3j) + (-7 - 8j) 
# ```
# ````
# `````

# ### Basic Arithmetic operations on strings (SAY WHAT!?)
# 
# - In general, you cannot perform mathematical operations on strings, even if the strings look like numbers.
# - However, some arithmetic operators do work on strings and open up some nice options. Let's explore this. 
# 

# In[3]:


x,y = 'cere','bellum'
print(f"+ Addition :                             {x}+{y}={x+y}") 
print(f"* Multiplication :                       {x}*{3}={x*3}") 
print(f"Combinations :                           {x}*{3}+{y}={x*3+y}")
print(f"() Use parentheses to specify order:     {x}+(({x}+{y})*{2})={x+((x+y)*2)}")


# ### Basic Numeric Comparison Operators
# 
# - Comparison operators are used to comparing two values
# 

# In[4]:


x,y = 5,4
print(f" isEqual(==)          {x}=={y} is {x==y}")
print(f" notEqual(!=)         {x}!={y} is {x!=y}")
print(f" isGreater(>)         {x}>{y}  is {x>y}")
print(f" isSmaller(<)         {x}<{y}  is {x<y}")
print(f" isGreaterOrEqual(>=) {x}>={y} is {x>=y}")
print(f" isSmallerOrEqual(<=) {x}<={y} is {x<=y}")


# ### Basic Numeric Assignment Operators
# 
# - Assignment operators are used to assigning values to variables
# 

# In[5]:


y = 3
x = y ;print(f" x = y   \t| y is assigned to x\t| x={y}")
x = 19 ;print(f" x = y  \t| 17 is assigned to x\t| x={x}")
x += y ;print(f" x += y \t| y is added to x\t| x={x}")
x -= y ;print(f" x -= y \t| y subtracted from x\t| x={x}")
x *= y ;print(f" x *= y \t| x multiplied by y\t| x={x}")
x /= y ;print(f" x /= y \t| x divided by y\t| x={x}")
x %= y ;print(f" x %= y \t| x%y is assigned to x\t| x={x}")
x **= y;print(f" x **= y\t| x**y is Added to x\t| x={x}")
x //= y;print(f" x //= y\t| x//y is assigned to x\t| x={x}")


# ### Basic Logical Operators
# 
# - Logical operators in Python are used for conditional statements are true or false. 
# - Logical operators in Python are **and**, **or** and **not**. 
# - For logical operators, the following condition are applied.
# - AND operator returns True if both the operands (right side and left side) are True
# - OR operator returns True if either of the operand (right side or left side) is True
# - NOT operator returns True if the operand is False

# In[6]:


x,y = True,False
print(f" When x is {x} and y is {y}")
print(f" {'='*35}")
print(f" x and y                 is {x and y}")
print(f" x or y                  is {x or y}")
print(f" not x and y             is {not x or y}")
print(f" x and not y             is {x or not y}")
print(f" {'~'*35}\n")
x,y = 10,20
print(f" When x is {x} and y is {y}")
print(f" {'='*35}")
print(f" x<y<y**2 and not y<x    is {x<y<y**2 and not y<x }")


# ### Basic Comparison operations on strings
# 
# - String objects can be compared as well 

# In[7]:


x,y = 'small','small'
print(f" isEqual(==)          {x} == {y} = {x==y}")
print(f" notEqual(!=)         {x.upper()} != {y} = {x.upper()!=y}")
x,y = 'small','SMALL'
print(f" {'='*43}")
print(f" isEqual(==)          {x} == {y} = {x==y}") 
print(f" notEqual(!=)         {x} != {y.lower()} = {x!=y.lower()}")


# ### Lets expand on strings 
# 
# - Every string in Python is an object containing a sequence of characters. 
# - Each letter in a string has a distinct index corresponding to its specific order. 
# - Indices start in 0 and end in the length of the string-1
# - Spaces count as a character
# - Both single and double quotes can be used to define a string

# In[8]:


a,b = 'test', "test"
print(f" Both tests are the same i.e. a=\'{a}\' and b=\'{b}\' and a==b is {a==b}") 


# #### Why do we need both single `'` and double `"` quotes? 
# 
# This simplifies using either single or double quotes within a phrase
# Consider the following code: 

# In[9]:


some_phrash = "Did you know that 'cultivar' is synonymous with 'clone'?"
print(f"British style\t: {some_phrash}")
same_phrash = 'Did you know that "cultivar" is synonymous with "clone"?'
print(f"American style \t: {same_phrash}")


# ### What about using both  single `'` and double `"` quotes?
# What do we do when we want both single `'` and double `"` quotes in the same string?  
# 
# 
# `````{admonition} Challenge
# Try to print the following sentence using python  
# "'The Green Hills of Earth' is one of my favourite stories," my teacher said.
# ````{dropdown} Solution
# - Luckily we have Escape Sequences in Python 
# - An escape sequence is defined using a backslash (\\) followed by any protected word.
# ```{code-block} python 
# mixed_quote_phrash = '" \'The Green Hills of Earth\' is one of my favourite stories," my teacher said.'
# print(f"We can escape the single: \n{mixed_quote_phrash}")
# mixed_quote_phrash = "\" 'The Green Hills of Earth' is one of my favourite stories,\" my teacher said."
# print(f"Or the double: \n{mixed_quote_phrash}")
# ```
# ````
# `````
# 

# ### Escaping the Escape Sequences
# - If we need to add a backslash, we will simply use a double \\\ 
# - This will print out only one backslash
# 
# #### useful Escape sequence characters (ESC)
# 
# | ESC | Description |
# | :-- | :-- | 
# | \\\ | Prints Backslash | 
# | \\'  | Prints single-quote | 
# | \\"  | Prints double quote |
# | \\n  | Print line break | 
# | \\t  | print tab | 
# | \\uxxxx | Use 16-bit hex Unicode char | 
# | \\Uxxxxxxxx | Use 32-bit hex Unicode char | 
# | | |

# ### Everything in Python is an object
# 
# - String class is an object as well.
# - Every time you create a string, it comes with many methods
# - After initializing a string object, all the possible methods can be accessed using dot notation
# - These are all functions that are useful under different situations
# 

# `````{admonition} Challenge
# Use the right introspection function to print all the methods a string object has
# ````{dropdown} Solution
# - `dir` returns list of methods and attributes associated with that object.
# ```{code-block} python 
# dir('')
# ```
# ````
# `````

# ### What’s the Meaning of double leading and trailing underscores In Python?

# ### Some string transformation examples
# 

# In[10]:


print((" upper is a method used to convert a string to uppercase").upper())
print((" center pads a string from both sides to fill k chars ").center(80,'~'))
print((" we can chain both together ").upper().center(80,'~'))
print((" But there are many options (e.g. title) ").title().center(80,'~'))


# ### More than style 
# 
# - By definition, we would expect string functions to be associated with style
# - But there are also more general ones 
# - For example the `endswith` command is a useful way to test the type of a filename 
# 
# 

# In[11]:


print(("some_file_name.zip").endswith("zip"))


# `````{admonition} Challenge
# Try to find a way to count the number of times the word 'her' is used in this short story by [N. West Moss](http://fiftywordstories.com/2021/04/12/n-west-moss-a-man-not-her-husband/).
# 
# > *A man (not her husband) had loved her last summer. He never said so, never kissed her, so maybe he hadn’t, but the wondering lit her up like a firefly. His absence weighed a thousand pounds and made her ears ring. Having almost certainly been loved still made her dance.*
# 
# ````{dropdown} Solution
# ```{code-block} python 
# story = "A man (not her husband) had loved her last summer. He never said so, never kissed her, so maybe he hadn’t, but the wondering lit her up like a firefly. His absence weighed a thousand pounds and made her ears ring. Having almost certainly been loved still made her dance." 
# print(f'The word her is used {story.count("her")} times')
# ```
# ````
# `````

# `````{admonition} Challenge
# Now find a way to identify the index of the first occurrence of the word 'her' in the story.
# 
# > *A man (not her husband) had loved her last summer. He never said so, never kissed her, so maybe he hadn’t, but the wondering lit her up like a firefly. His absence weighed a thousand pounds and made her ears ring. Having almost certainly been loved still made her dance.*
# 
# ````{dropdown} Solution
# ```{code-block} python 
# print(f'The word her first appears in the {story.find("her")} position')
# ```
# ````
# `````

# ### Let's focus on indexing for a moment 
# 
# - Every string is a sequence of characters 
# - This is an excellent opportunity to cover how indexing works
# - The len() function will count all of the string characters (including spaces and punctuation)

# In[12]:


some_string = "Some times we want to find how long is a string"
print(f'{some_string}  = {len(some_string)}')


# ### But how can we navigate in this sequence? 
# - To go to a specific index in a string, we use brackets `[ ]`
# - Remember that indexing starts at 0 for Python
# - Consider the following:

# In[13]:


print(f"Access start index using [0]\t\t\t= {some_string[0].upper()} \nAccess end index using  [-1] \t\t\t= {some_string[-1].upper()} \nUse the colon [start:end] to perform slicing \t= {some_string[38:40].upper()} \nGet everything UPTO [:end] \t\t\t= {some_string[:4].upper()} \nGet everything FROM TO [start:end-2] \t\t= {some_string[38:-2].upper()}" )


# ### Slicing and skipping 
# - It is possible to use index and slice notation to get a sequence using a step size
# 

# In[14]:


print(f"Print everything [:]\t\t= {some_string[:].upper()} \nPrint every second word [::2] \t= {some_string[::2].upper()} \nEverything in reverse [::-1]\t= {some_string[::-1].upper()}" )


# ### Strings are immutable
# 
# - Remember, immutable means that you cannot change the object itself
# - This means that we cannot change a single letter in the string 
# 
# 
# `````{admonition} Example
# Let's try this explicitly - try to run this sta
# ```{code-block} python 
# some_string[4]='a'
# ```
# 
# `````
# 

# ### We can also use split to break a long string
# 
# - The split() and rsplit() methods splits string from the left or right at the specified separator and returns a list of strings.
# 

# In[15]:


print("some times we would like to split long text".split())
print("It,can,use any,kind of, delimiter".split(','))
print("You,can,also,define,how,many,splits".split(',',3))
print("As,well,as,direction,of,splits".rsplit(',',2))


# ### Strings can be concatenated 
# - We already saw that we could combine different strings together 
# - But this is not very easy to understand

# In[16]:


a,b,c,d = 'some','times', 'we', 'would'
print(a+b+d*2+c)


# - For those paying attention to the code, you can see that I am constantly combining strings with variables 
# - This operation is called string formatting, and it is useful to know the different ways in which it can be used 
# 
# ## String Formatting
# 
# - From python 3.6 string formatting is done using f-strings, these simplify this process and make the code easier to understand  
# - For those interested (and for completeness) [here is a link explaining the older methods](https://realpython.com/python-string-formatting/)

# ### f-strings examples

# In[17]:


some_str = "Malarkey"
print(f"Do you know what {some_str} means?\n") 
# using !r will keep the string
print(f"{some_str!r} refers to talk that is particularly foolish") 


# ### Anatomy of an f-string command
# 
# - Any string starting with the letter `f` or `F` (case doesn't matter) will be interpreted as an f-string

# In[18]:


f'String' == F'String'


# - An f-string is composed of at least one of two potential components:
#   - A string 
#   - A replacement field contained between two curly brackets  

# In[19]:


f'{"String"}' == f'String'


# - The replacement field has two potential components contained between the two curly brackets
#   - f_expression   
#   - format_spec

# #### f-string and numbers
# 

# |Expression   |	Format    | Syntax                    | Output              | 	Description      |
# |:---       |:---   |:---                       | :---       |:---------------------|
# |22/7	     | .2f |f'{22/7:.2f}'	            | 3.14	              |2 decimal places        |
# |(1+1/5)**5  | .3f |f'{(1+1/5)**5:+.3f}'	    |+2.488	              |3 decimal places with sign |
# |(-.5)**0.75 | .1f |f'{(-.5)**0.75:+.1f}'	    |-0.4+0.4j	          |1 decimal places with sign |
# |44/7	     | .0f |f'{44/7:.0f}'     	    |6                    |No decimal places     |
# |12	        | 0>3 |f'{12:0>3}'                |012                  |Pad number with zeros (left padding, width 3) |
# |1e6	    | , |f'{1e6:,}'	                |1,000,000.0          |Float format with comma separator |
# |1e9	    | , |f'{int(1e9):,}'	        |1,000,000,000        |Int format with comma separator |
# |5/9	    | .2% |f'{5/9:.2%}'	            |25.00%	              |Format percentage |
# |25**5	    | .2e |f'{25**5:.2e}'             |9.77e+06           |Exponent notation |

# #### f-strings dates and time
# 
# - Dates are also simpler to define (however, I am cheating here as I am using some Python package)
# 
# 

# In[20]:


from datetime import date
from datetime import time
some_date = date(year=2020, month=5, day=26)
some_time = time(hour=13, minute=30,second=10)
print(f"{some_date:%B %d, %Y} {some_time:%H:%M:%S}") 


# #### f-string can do numeric notations
# - For example Hexadecimal often used to describe RGB colors  

# In[21]:


R, G, B = 0, 153, 255
print(f'The color cyan-blue can be written as #{R:x}{G:x}{B:x} in hex form')


# - Also binary numbers  

# In[22]:


print(f'The number 254 is {254:b} in binary ')


# ### Let's do some exercises 
# - Try to change the question mark using expressions and the variables x and y in the right side of the equation to produce the following output
# 
# ~~~ python 
# x,y = -12,2 # given numbers
# ? = -6.0 
# ? = -10
# ? = -14
# ? = 0
# ? = 144.0
# ? = 0.0+3.5j 
# ? = 96.0
# ~~~

# ## Links to expand your understanding 
# 
# For those interested in learning more...
# 
# - [Python String Tutorial](https://www.datacamp.com/community/tutorials/python-string-tutorial)
# - [Python For Data Science - A Cheat Sheet For Beginners](https://www.datacamp.com/community/tutorials/python-data-science-cheat-sheet-basics)
# 
