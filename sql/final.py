import sqlite3

def query_max():
	con = sqlite3.connect('survey.db')
	cur = con.cursor()
	cur.execute('select person, max(reading) from survey group by person')
	data = cur.fetchall()
	for line in data:
		print line

def query_max_python():
	con = sqlite3.connect('survey.db')
	cur = con.cursor()
	cur.execute('select person, reading from survey')
	data = cur.fetchall()

	print '-' * 50	
	person_list = {}
	for line in data:
		person, reading = line
		if person not in person_list:
			person_list[person] = []
		person_list[person].append(reading)

	for person in person_list:
		print person, max(person_list[person])

def main():
	query_max()
	query_max_python()

if __name__ == '__main__':
	main()

