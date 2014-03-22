days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months_in_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months_in_year:
	print month
	print "\n"
	print ">>>>>>>>>>>>>>>>>>>>>"
	print "\n"

	for week in range (1,5):
			print "Week {0}".format(week)
			print "\n"
			print "------------------"

			for day in days_of_week:
				print day
			print "\n"
			print "------------------"
