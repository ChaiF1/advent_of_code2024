def parser(file):
	rules = [  ]
	for line in file:
		rule = line.strip("\n").split(' ')
		rule = list(map(int, rule))
		rules.append(rule)

	return rules


def part_one(rules):
	result = 0
	for rule in rules:
		safe = check_safety(rule)
		if safe:
			result += 1
	return result

def remove_element(list, index):
	return [list[i] for i in range(len(list)) if i != index]

def part_two(rules):
	result = 0
	for rule in rules:
		safe = check_safety(rule)
		if safe:
			result += 1
			continue

		for i in range(len(rule)):
			safe = check_safety( remove_element(rule, i) )

			if safe:
				result += 1
				break
	return result



def check_safety(rule):
	dummy = []	
	for i in range(len(rule)-1):
		dummy.append(rule[i]-rule[i+1])

	abs_dummy = list(map(abs, dummy))
	second_condition = all(0 < x < 4 for x in abs_dummy)

	if (all(x > 0 for x in dummy )) and second_condition:
		return True
	elif (all( x < 0 for x in dummy)) and second_condition:
		return True

	return False


# Every step must be of the same sign
# The difference between the steps must be between 1 and 3
# Check if the sum of both truth arrays
if __name__ == "__main__":
	file = open("data.txt", "r")
	rules = parser(file)

	print(part_two(rules))

	# Can I just brute force by checkign it once if I remove each line?