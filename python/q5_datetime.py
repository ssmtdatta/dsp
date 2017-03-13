'''
Use Python to compute days between start and stop date.

Start and stop dates are given in three different string formats:
1. '01-02-2013' (month, day and year separated by -)
2. '12312013' (month, day and year separeted by null space)
3. '15-Jan-1994' (day, month and year separated by -.)

In all formats (1, 2 and 3):
day and year are given as zero-padded decimal numbers.

In formats 1 and 2:
months are given as zero-padded decimal numbers.

In format 3:
month as locale’s abbreviated name.

The start_date and stop_date strings are converted to date object.
The the number of days between the dates is computed by takeing the difference 
between two date objects.

'''


from datetime import datetime as dt 

date_format_1 = "%m-%d-%Y" 
date_format_2 = "%d-%b-%Y" 

def countDays(date_start, date_stop, date_format):
	dt_start = dt.strptime(date_start, date_format)
	dt_stop = dt.strptime(date_stop, date_format)
	delta = dt_stop - dt_start
	return delta.days

def formatDate(a_date):
	'''
	Convert to format 1 as described at the top
	'''
	m = a_date[:2]
	d = a_date[2:4]
	y = a_date[-4:]
	return str(m)+'-'+str(d)+'-'+str(y)



####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

days_in_between = countDays(date_start, date_stop, date_format_1)
print(days_in_between)
 

####b)  
date_start = '12312013'  
date_stop = '05282015' 

date_start = formatDate(date_start)
date_stop = formatDate(date_stop)

days_in_between = countDays(date_start, date_stop, date_format_1)
print(days_in_between)


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

days_in_between = countDays(date_start, date_stop, date_format_2)
print(days_in_between)
