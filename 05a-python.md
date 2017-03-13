# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A Python **list** is a sequence of literals written within a square bracket separated by comma. Element of a list can be accessed by their indices (the first list element has an index of zero, the second and index of 1, the third 2, and so on). Elements can be added to or removed from a list. List elements can be re-ordered (e.g. sort in ascending or descending order, or alphabetically). A list element can be changed to a different value without affecting the others. 

>> A Python **tuple** is a group of literals written within a parenthesis separated by comma. Tuples must preserve the order and value of the literals as they were created. One cannot change the values of tuple elements or re-order them, which means tuples are immutable. Like lists, tuple elements can be accessed by their index numbers. Two or more tuples can be joined to create a new tuple, but the order of tuples (as they are joined) is preserved. The new tuple is considered a single tuple. 

>> A Python **dictionary** is a paired data structure, where the pairs are *key-value* pairs. The keys can be thought of elements of a list. Each key has a value. 

This is synonymous to a dictionary of words and their meanings or definitions (hence the name dictionary). In a dictionary, there are words. Each word has a meaning or definition. In a python, a *key* is a word, and its definition a *value*. 

An element of a Python dictionary is accessed by the key. When a key is called, the value associated with the key is returned.

The elements of a list, dictionary of a tuple can be any Python data structure such as integer, float, string, list, tuple, dictionary, etc.

The following table shows a few basic comparisons between lists, tuples and dictionaries.



              | Data Structure
------------- | -------------
List          | ``` Pythona_list = ['name', 'Pixie', 'age', 11]
--------------|---------------
Tuple         | a_tuple = ('name', 'Pixie', 'age', 11)
--------------|---------------
Dictionary    |D = {'name':'Pixie', 'age': 11}
--------------|----------------------



---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists are comprised of literals in a sequence. Lists can contain identical literals. Python **sets** contain unique values. A set can be thought of a subset of a list with the duplicates removed. 

>> Example:

* List: [1, 2,'list', 999, 'set', 'tuple', 0, 0, 'tuple']

* Set: {0, 1, 2, 999, 'tuple', 'list', 'set'}

>> The follwing code was used to create a list and a set from the list.

```python
# Define a list:
the_list = [1, 2, "list", 999, "set", "tuple", 0, 0, "tuple"]

# Convert the list to a set:
the_set = set(the_list)

# Print the set:
print(the_set)
```

The performance between lists and dictionaries depends of the operation perfomed. For instance, sets are significantly faster when it comes to determining if an element is present in the set, but are slower than lists when it comes to iterating over their contents.



---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python supports the creation of anonymous functions (i.e. functions without a particular name). The anonymous function is defined as 'lambda'. 

A regular function in Python (defined as `def function_name`) 

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





