from FirstProject import *
import webbrowser, os
import subprocess

# webbrowser.open('file://' + os.path.realpath('FirstInstructions.html'))
subprocess.call('./openMe.sh')

newSet = [1, 2, 3, 4]

def rightTotal(set) :
	total = 0
	for i in set :
		total += i

	return total

print 'Correct' if total(newSet) == rightTotal(newSet) else 'Wrong'