# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A Python **list** is a sequence of literals written within a square bracket separated by comma. The elements of a list can be accessed by their indices (the first list element has an index of zero, the second an index of 1, the third 2, and so on). Elements can be added to or removed from a list. List elements can be re-ordered (e.g. sort in ascending or descending order, or alphabetically). A list element can be changed to a different value without affecting the other elements in the list. 

>> A Python **tuple** is a group of literals written within a parenthesis separated by comma. Tuples must preserve the order and value of the literals as they were created. One cannot change the values of tuple elements or re-order them, which means tuples are immutable. Like lists, tuple elements can be accessed by their index numbers. Two or more tuples can be joined to create a new tuple, but the order of initial tuples (as they are joined) is preserved. The new tuple is considered a single tuple. 

>> A Python **dictionary** is a paired data structure, where the pairs are referred to as *key-value* pairs. The keys can be thought of dictionary elements. Each key has a value of its own. 

>> This is synonymous to a dictionary of words and their meanings or definitions. In a dictionary, there are words. Each word has a meaning or definition. In a python, a *key* is a word, and its definition a *value*. 

>> An element of a Python dictionary is accessed by the name of the key. When a key is called, the value associated with the key is returned.

>> The elements of a list, a dictionary or a tuple can be any Python data structure such as integer, float, string, list, tuple, dictionary, etc. The key of a dictionary can be any immutable literals such as integer, string, tuple, etc.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists are comprised of literals in a sequence. Lists can contain identical literals. Python **sets** contain unique values. A set can be thought of a subset of a list with the duplicates removed. 

>> Example:

* **List** 
```python
[1, 2,'list', 999, 'set', 'tuple', 0, 0, 'tuple']
```

* **Set** (of the list above) 
```python
{0, 1, 2, 999, 'tuple', 'list', 'set'}
```

>> The follwing code was used to create a list and a set from the list.

```python
# Define a list:
the_list = [1, 2, "list", 999, "set", "tuple", 0, 0, "tuple"]

# Convert the list to a set:
the_set = set(the_list)

# Print the set:
print(the_set)
```

>> The performance between lists and dictionaries depends of the operation perfomed. For instance, sets are significantly faster when it comes to determining if an element is present in the set, but are slower than lists when it comes to iterating over their contents.



---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>  While functions in Python are typically defined using the `def` keyword, Python also allows us to create functions without particular names. These are called anonymous functions and are defined using the `lambda` keyword. 

>> `lambda` functions are particularly useful when we want to perform operations without explicitly defining a function or variables. 
>> `lambda` functions are sometimes compact represeatations of a `def` function.    

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a tool for transforming a list into another by performing some operation on the list elements. During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.

>> **Examples of list comprehension, lambda functions and  map &amp; filter operations are given in this**
[iPython notebook](python/list_comprehension_lambda.ipynb)


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





