'''
Use Python to compute days between start and stop date.

Start and stop dates are given in three different string formats:
1. '01-02-2013' (month, day and year separated by '-')
2. '12312013' (month, day and year separeted by null space)
3. '15-Jan-1994' (day, month and year separated by '-')

In all formats (1, 2 and 3):
day and year are given as zero-padded decimal numbers.

In formats 1 and 2:
month is given as zero-padded decimal numbers.

In format 3:
month is given as abbreviated month name.

The start_date and stop_date strings are converted to date object.

The number of days between the dates is computed by takeing the difference 
between two date objects.

'''


from datetime import datetime as dt 
import calendar

def countDays(date_start, date_stop, date_format):
	"""
	Count the number of days between two dates
	"""
	dt_start = dt.strptime(date_start, date_format)
	dt_stop = dt.strptime(date_stop, date_format)
	delta = dt_stop - dt_start
	return delta.days

def formatDate(a_date):
	'''
	date_formats:
	[1] "%m-%d-%Y" 
	[2] "%m%d%Y" 
	[3] "%d-%b-%Y" 
 	Convert to date format [2] to date format [3]
	'''
	m = a_date[:2]
	d = a_date[2:4]
	y = a_date[-4:]
	return str(m)+'-'+str(calendar.month_abbr[int(m)])+'-'+str(y)



####a) date format: Month-Day-Year
date_start = '01-02-2013'  
date_stop = '07-28-2015'

# change date format to MonthDayYear
date_start = date_start.replace("-", "")
date_stop = date_stop.replace("-", "")

days_in_between = countDays(date_start, date_stop, "%m%d%Y")
print("There are "+str(days_in_between)+" days between "+str(formatDate(date_start))+" and "+str(formatDate(date_stop))+".")
 

####b) date format: MonthDayYear
date_start = '12312013'  
date_stop = '05282015' 

days_in_between = countDays(date_start, date_stop, "%m%d%Y" )
print("There are "+str(days_in_between)+" days between "+str(formatDate(date_start))+" and "+str(formatDate(date_stop))+".")


####c) date format: Day-Month-Year
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

days_in_between = countDays(date_start, date_stop, "%d-%b-%Y")
print("There are "+str(days_in_between)+" days between "+str(date_start)+" and "+str(date_stop)+".")
