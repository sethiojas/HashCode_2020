num_books = 0
num_lib = 0
days = 0
score_books = []
lib_details = []
book_data = []
filename = 'f_libraries_of_the_world'
data = []
index_lib = []

with open(filename+'.txt', 'r') as file:
	num_books, num_lib, days = map(int, file.readline().strip().split(' '))
	score_books = list(map(int, file.readline().strip().split(' ')))
	for i in range(num_lib):
		books, signup, ship = map(int, file.readline().strip().split(' '))
		lib_details.append([books, signup, ship])

		books_in_lib = list(map(int, file.readline().strip().split(' ')))
		books_in_lib = sorted([(item, score_books[item]) for item in books_in_lib[:]], reverse = True, key = lambda x: x[1])

		book_data.append(books_in_lib)


while days > 0 and num_lib > 0:

	least_signup = []
	ls = sorted(lib_details, key = lambda x: x[1])
	for i in range(len(ls)):
		if ls[i] != [0,0,0]:
			least_signup.append(ls[i])
		if len(least_signup) == 3:
			break
	max_ship = sorted(least_signup, reverse = True, key = lambda x: x[2])[:2]
	selected = sorted(max_ship, reverse= True, key = lambda x: x[0])
	days = days - selected[0][1]
	num_lib -=1
	
	ind = lib_details.index(selected[0])
	index_lib.append(ind)


	lib_details[ind] = [0,0,0]

	n = selected[0][2]*(days-1)

	for item in data:
		for elem in book_data[ind][:]:
			if elem in item:
				book_data[ind].remove(elem)

	data.append(book_data[ind][:n])

while [] in data:
	ind = data.index([])
	data.remove([])
	index_lib.pop(ind)

with open(filename+'_output.txt', 'w') as file:
	file.write(str(len(index_lib))+'\n')
	for i in range(len(index_lib)):
		file.write(str(index_lib[i])+' '+str(len(data[i]))+ '\n')
		for item in data[i]:
			file.write(str(item[0])+' ')
		file.write('\n')

