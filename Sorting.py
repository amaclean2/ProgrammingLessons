import random

dataSet = []
for x in range(1000) :
	dataSet.append(random.randint(1, 1000))

def findGreatestInSet(set) :
	greatest = 0
	for a in set :
		if a > greatest :
			greatest = a

	return greatest

def findLeastInSet(set) :
	least = set[0]
	for a in set :
		if a < least :
			least = a

	return least

def findMiddle(set) :
	least = findLeastInSet(set)
	greatest = findGreatestInSet(set)

	return ((greatest - least) / 2) + least

def lowerBucket(set) :
	middle = findMiddle(set)
	lowerBucket = []
	for a in set :
		if a <= middle :
			lowerBucket.append(a)

	return lowerBucket

def higherBucket(set) :
	middle = findMiddle(set)
	higherBucket = []
	for a in set :
		if a > middle :
			higherBucket.append(a)

	return higherBucket

def join(setOne, setTwo) :
	setOne.extend(setTwo)
	return setOne

def sort(set) :

	test = set[0]
	allTheSame = 'true'

	for i in set :
		if i != test :
			allTheSame = 'false'

	if allTheSame == 'true' :
		return set

	bottom = lowerBucket(set)
	top = higherBucket(set)

	if len(bottom) > 1 :
		bottom = sort(lowerBucket(set))
	if len(top) > 1:
		top = sort(higherBucket(set))

	return join(bottom, top)

def findMostRecurring(set) :
	recurrence = 1
	toRecur = 0
	recurrences = []

	for i in set : 
		if i == toRecur :
			recurrence += 1

		else :
			newObject = {}
			newObject[toRecur] = recurrence

			recurrences.append({ 'value': toRecur, 'times': recurrence })
			recurrence = 1
			toRecur = i

	print recurrences
	# print str(highestNumber) + " recurrend " + str(highestRecurrence) + " times"


#findMostRecurring(sort(dataSet))