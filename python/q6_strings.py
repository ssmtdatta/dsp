# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """

    if count < 10:
        string = 'Number of donuts: '+ str(count)
    else:
        string = 'Number of donuts: many'

    return string
    
    raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        return "''"
    else:
        ss = s[:2]+s[-2:]
        return ss

    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """

    s1, s2 = s[0], s[1:]
     
    s2 = s2.replace(s1, '*')
    
    return s1+s2


    raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    
    a2 = a[:2]
    b2 = b[:2]

    a_swapped = a.replace(a2, b2)
    b_swapped = b.replace(b2, a2)
    
    return a_swapped+' '+b_swapped

    raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """

    if len(s) >= 3:
    	if s[-3:] == 'ing':
    		return s+'ly'
    	else:
    		return s+'ing'
    else:
    	return s

    raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    'It's bad yet not'
    """
    str1 = 'not'
    str2 = 'bad'

    if str1 in s and str2 in s:
    	idx_str1 = s.index(str1)
    	idx_str2 = s.index(str2)

    	if idx_str2 > idx_str1: 
    		str_to_replace = s[idx_str1:idx_str2+len(str2)]
    		s_new = s.replace(str_to_replace, 'good')
    		return s_new
    	else:
    		return s
    
    else:
    	return s
    

    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    def front_back_index(s):
    	
    	len_s = len(s)
    	
    	# if the length of the string is even
    	if len_s%2 == 0:
    		front_idx = int( len(s)/2 )
    		back_idx = int( len(s)/2 )
    	# is the length of the string is odd	
    	else:
    		front_idx = int( len(s)/2 ) + 1 
    		back_idx = int( len(s)/2 ) 

    	return front_idx, back_idx

    a_front_idx, a_back_index = front_back_index(a)
    b_front_idx, b_back_index = front_back_index(b)

    new_str = a[:a_front_idx] + b[:b_front_idx] + a[-a_back_index:] + b[-b_back_index:]

    return new_str

    raise NotImplementedError


