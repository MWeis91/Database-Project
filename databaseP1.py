#Database design project 1
#Matthew Weis

def main():
	coachList =[]#Coaches table(a list of coach objects)
	teamList = []#Teams table(a list of team objects)

	print "The mini-DB of NBA coaches and teams"
	print "Please enter a command.  Enter 'help' for a list of commands."
	a = 1
	while a == 1:
		rawIn = raw_input()
		inLen = len(rawIn)
		rawIn = rawIn.split(" ")
		for x in rawIn:
			rawIn[rawIn.index(x)] = x.replace("+", " ")
		
		command = rawIn[0]
		print "-" * inLen
		print "\n"

		if command == 'help':
			print "add_coach ID SEASON FIRST_NAME LAST_NAME SEASON_WIN SEASON_LOSS PLAYOFF_WIN PLAYOFF_LOSS TEAM - add new coach data"
			print "add_team ID LOCATION NAME LEAGUE - add a new team"
			print "print_coaches - print a listing of all coaches"
			print "print_teams - print a listing of all teams"
			print "coaches_by_name NAME - list info of coaches with the specified name"
			print "teams_by_city CITY - list the teams in the specified city"
			print "load_coach FILENAME - bulk load of coach info from a file"
			print "load_team FILENAME - bulk load of team info from a file"
			print "best_coach SEASON - print the name of the coach with the most net wins in a specified season"
			print "search_coaches field=VALUE - print the name of the coach satisfying the specified conditions"
			print "delete_coaches field=VALUE - delete the coach satisfying the specified conditions"
			print "exit - quit the program"

		elif command == 'add_coach':
			new_coach = [ rawIn[1], rawIn[2], rawIn[3], rawIn[4], rawIn[5], rawIn[6], rawIn[7], rawIn[8], rawIn[9]]
			coachList.append(new_coach)
			print "\n"

		elif command == 'add_team':
			new_team = [rawIn[1], rawIn[2], rawIn[3], rawIn[4]]
			teamList.append(new_team)
			print "\n"

		elif command == 'load_coaches':
			coachFile = open(rawIn[1], "r")
			line = coachFile.read().split("\n")[1:]
		
			for x in line:
				x = x.rstrip().split(",")
				x = filter(None, x)#deletes empty strings from x

				for y in x:
					x[x.index(y)] = y.strip()
				
				if x:#if x is not an empty list, then continue
					del x[2]
					coachList.append(x)
			coachFile.close()

		elif command == 'load_teams':
			teamFile = open(rawIn[1], "r")
			line = teamFile.read().split("\n")[1:]
			
			for x in line:
				x = x.rstrip().split(",")
				x = filter(None, x)#deletes empty strings from x
				
				if x:#if x is not an empty list, then continue
					teamList.append(x)
			teamFile.close()

		elif command == 'print_coaches':
			for x in coachList:
				print x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]
			print "\n"

		elif command == 'print_teams':
			for x in teamList:
				print x[0], x[1], x[2], x[3]
			print "\n"

		elif command == 'coaches_by_name':
			for x in coachList:
				if x[3] == rawIn[1]:
					print x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]
			print "\n"

		elif command == 'teams_by_city':
			for x in teamList:
				if rawIn[1] == x[1]:
					print x[0], x[1], x[2], x[3]
			print "\n"

		elif command == 'best_coach':
			coachYear = []
			for x in coachList:
				if rawIn[1] == x[1]:
					coachYear.append(x)
			totalWin = -1000
			bestCoach = []
			coachFound = 0
			for x in coachYear:
				coachFound = 1
				seasonWin = int(x[4])
				seasonLoss = int(x[5])
				playoffWin = int(x[6])
				playoffLoss = int(x[7])
				netWin = (seasonWin - seasonLoss) + (playoffWin - playoffLoss)
				x.append(netWin)
				if x[9] > totalWin:
					totalWin = x[9]
					bestCoach = x
			if coachFound == 0:
				print "No coaches this year"
			if coachFound == 1:
				print bestCoach[2], bestCoach[3]
			print "\n"

		elif command == 'search_coaches':
			queries = rawIn
			del queries[0]
			queryList = []

			for x in queries:
				queries[queries.index(x)] = x.split("=")
			for x in queries:
				searchList = []
			
				if x[0] == 'Coach_ID':
					for y in coachList:
						if y[0] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'season':
					for y in coachList:
						if y[1] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'first_name':
					for y in coachList:
						if y[2] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'last_name':
					for y in coachList:
						if y[3] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'season_win':
					for y in coachList:
						if y[4] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'season_loss':
					for y in coachList:
						if y[5] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'playoff_win':
					for y in coachList:
						if y[6] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'playoff_loss':
					for y in coachList:
						if y[7] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'team':
					for y in coachList:
						if y[8] == x[1]:
							searchList.append(tuple(y))
				queryList.append(tuple(searchList))

			if queryList:
				queryList = tuple(queryList)
				finalList = list(set.intersection(*map(set, queryList)))
				for x in finalList:
					print x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]
			print '\n'

		elif command == 'delete_coaches':
			queries = rawIn
			del queries[0]
			queryList = []
			tempList = []

			for x in queries:
				queries[queries.index(x)] = x.split("=")
			for x in queries:
				searchList = []
			
				if x[0] == 'Coach_ID':
					for y in coachList:
						if y[0] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'season':
					for y in coachList:
						if y[1] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'first_name':
					for y in coachList:
						if y[2] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'last_name':
					for y in coachList:
						if y[3] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'season_win':
					for y in coachList:
						if y[4] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'season_loss':
					for y in coachList:
						if y[5] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'playoff_win':
					for y in coachList:
						if y[6] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'playoff_loss':
					for y in coachList:
						if y[7] == x[1]:
							searchList.append(tuple(y))

				elif x[0] == 'team':
					for y in coachList:
						if y[8] == x[1]:
							searchList.append(tuple(y))
				queryList.append(tuple(searchList))

			if queryList:
				queryList = tuple(queryList)
				finalList = list(set.intersection(*map(set, queryList)))
				for y in coachList:
					if tuple(y) not in finalList:
						tempList.append(y)
				coachList = tempList
			print '\n'

		elif command == 'exit':
			print "Leaving the database, goodbye!"
			a = 0
		else:
			print "Invalid command, try again!"

main()





