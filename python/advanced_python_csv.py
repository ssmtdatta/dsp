import csv


input_filename = "faculty.csv"
output_filename = "emails.csv"


ff = open(output_filename, 'w')

with open(input_filename) as f:
    csv_file = csv.reader(f)
    headers = next(csv_file)
    
    ff.write("email\n")

    for line in csv_file:
    	*_, email = line
    	ff.write(email)
    	ff.write("\n")
       
f.close()
ff.close()


