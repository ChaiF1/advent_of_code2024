file = open("data.txt")

def parser(file):
	list1 = [ ]
	list2 = [ ] 
	for line in file:
		data = line.strip().split("   ")
		list1.append(int(data[0]))
		list2.append(int(data[1]))

	return list1, list2


def part_one(list1, list):
	list1, list2 = parser(file)
	list1.sort()
	list2.sort()

	return sum(abs(x-y) for x, y in zip(list1, list2))

def create_histogram(list):
	histogram = { }
	for i in list:
		if i in histogram:
			histogram[i] += 1
		else:
			histogram[i] = 1
	return histogram

def part_two(list1, list2):
	counts_1 = create_histogram(list1)
	counts_2 = create_histogram(list2)

	result = 0
	for key in counts_1:
		if key in counts_2:
			result += counts_1[key]*counts_2[key]*key

	return result

if __name__ == "__main__":
	list1, list2 = parser(file)
	print(part_two(list1, list2))

