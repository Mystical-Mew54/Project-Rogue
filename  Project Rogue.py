#This is the start of basic character creation

from turtle import done

#This is the function for spending stat points
def stat_dist(current_total, stat_points):

	if current_total == 0:
		print("> You have [" + str(stat_points) + "] to spend")
		print("> How many points do you wish to use?")
		add_remove = int(input("> "))

		#This is for if the player trys to add more or less points than they have
		while add_remove > 5 or add_remove <= 0:
			print("> Error: Invalid number")
			print("> You have [" + str(stat_points) + "] to spend")
			add_remove = int(input(">  "))

	#This is for if the selected stat already has
	#at least 1 point in it
	elif current_total >= 1:
		print("> [1] Add points")
		print("> [2] Remove points")
		add_or_remove = int(input("> "))

		while add_or_remove < 1 or add_or_remove > 2:
			print("> Error: Invalid number")
			print("> [1] Add points")
			print("> [2] Remove points")
			add_or_remove = int(input("> "))

		#This is for if the player wants to add points from their stat total while having
		#1 point or more already
		if add_or_remove == 1:
			print("> You have [" + str(stat_points) + "] to spend")
			print("> How many points do you wish to use?")
			add_remove = int(input("> "))

		#This is for if the player wants to remove points from their stat total while having
		#1 point or more already
		elif add_or_remove == 2:
			print("> How many points do you want to remove?")
			add_remove = int(input("> "))

			while add_remove > current_total:
				print("> Error: You cannot spend more than you have")
				print("> How many points do you want to remove?")
				add_remove = int(input("> "))

			add_remove = 0 - add_remove

	return add_remove

#This is the function for creating a character
def create_chr():
	creating_character = True

	#The 5 basic stats
	stat_lck = 0
	stat_str = 0
	stat_int = 0
	stat_cha = 0
	stat_per = 0

	stat_points = 5

	name = input("> Name: ")
	print("> -------")

	#This is the code for the player creating their stats
	while creating_character==True:

		#debug variable
		add_remove = 1

		print("> [1] Strength: " + str(stat_str))
		print("> [2] Perception: " + str(stat_per))
		print("> [3] Intellegence: " + str(stat_int))
		print("> [4] Charisma: " + str(stat_cha))
		print("> [5] Luck: " + str(stat_lck))

		while True:
			try:
				print("> You have [" + str(stat_points) + "] to spend. Pick a stat (1-5) to spend points in")
				current_stat = int(input(">  "))
				break_value = True

			except ValueError:
				print("> Error: Nice try, buckaroo")
				break_value = False

			if break_value == True:
				break




		if current_stat == 1:
			final_add_remove = stat_dist(stat_str, stat_points)
			stat_str = stat_str + final_add_remove
			stat_points = stat_points - final_add_remove


		elif current_stat == 2:
			final_add_remove = stat_dist(stat_per, stat_points)
			stat_per = stat_per + final_add_remove
			stat_points = stat_points - final_add_remove

		elif current_stat == 3:
			final_add_remove = stat_dist(stat_int, stat_points)
			stat_int = stat_int + final_add_remove
			stat_points = stat_points - final_add_remove

		elif current_stat == 4:
			final_add_remove = stat_dist(stat_cha, stat_points)
			stat_cha = stat_cha + final_add_remove
			stat_points = stat_points - final_add_remove

		elif current_stat == 5:
			final_add_remove = stat_dist(stat_lck, stat_points)
			stat_lck = stat_lck + final_add_remove
			stat_points = stat_points - final_add_remove


		if stat_points <= 0:
			done_yet = input("> Are you finished? [Y/N] ")

			done_yet = done_yet.upper()
			if done_yet == "Y" or done_yet == "YES":
				creating_character = False


print("> Project Rogue, Version not even Beta")
print("> Press [ENTER] to start")
buffer = input("> ")
print("> -----------------------")

create_chr()

print("> Loading UI. . . . . . . .")
