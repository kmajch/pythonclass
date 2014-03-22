#Third python class, learning how to open a list of states and use a "for" loop to add "Hello" before all of the states.

with open("states.txt", "r") as states_file:
		states = states_file.read().split('\n')

#print states

for state in states:
	print "Hello", state 
