#Here, we're splitting the file into a list at each line, and then individually splitting each line into a list by the commas.
#the file 

#lesson three python. states.csv is just a csv file of state abbrevs and full names

with open("states.csv", "r") as states_file:		
		states = states_file.read().split("\n")

		for index, state in enumerate(states):
				states[index] = state.split(",")

print states
