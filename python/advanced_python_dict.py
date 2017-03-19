import csv
from operator import itemgetter
from json import loads, dumps
from collections import OrderedDict
import re


def to_ordinary_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))


def get_title(t):
	pattern_1 = 'Associate'
	pattern_2 = 'Assistant'
	if re.search(pattern_1.lower(), t.lower()):
		return 'Associate Professor'
	if re.search(pattern_2.lower(), t.lower()):
		return 'Assiatant Professor'
	if re.search('0', t.lower()):
		return False
	else:
		return 'Professor'
		



filename = "faculty.csv"

faculty_list = []
with open(filename) as f:
    csv_file = csv.reader(f)
    headers = next(csv_file)
    
    for line in csv_file:
    	name, degree, title, email = line
    	title_short = get_title(title)
    	first_name, *_, last_name = name.split(" ")
    	line = [last_name, first_name] + [degree, title_short, email]
    	faculty_list.append(line)
f.close()
# sort faculty list by last name
sorted(faculty_list, key=itemgetter(0))


ord_dict_1 = OrderedDict()
for d_list in faculty_list:
	if d_list[0] in ord_dict_1:
		ord_dict_1[d_list[0]].append(d_list[-3:]) 
	else:
		ord_dict_1[d_list[0]] = d_list[-3:]

faculty_dict_1 = to_ordinary_dict(ord_dict_1)
#print(faculty_dict)



ord_dict_2 = OrderedDict()
for d_list in faculty_list:
	key = (d_list[1], d_list[0])
	key = str(key)
	if key in ord_dict_2:
		ord_dict_2[key].append(d_list[-3:]) 
	else:
		ord_dict_2[key] = d_list[-3:]


faculty_dict_2 = to_ordinary_dict(ord_dict_2)
#print(faculty_dict_2)


ord_dict_3 = OrderedDict()
for d_list in faculty_list:
	key = (d_list[0], d_list[1])
	key = str(key)
	if key in ord_dict_3:
		ord_dict_3[key].append(d_list[-3:]) 
	else:
		ord_dict_3[key] = d_list[-3:]

faculty_dict_3 = to_ordinary_dict(ord_dict_3)
print(faculty_dict_3)





