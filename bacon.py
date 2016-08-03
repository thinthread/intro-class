choice1 = 1

def eat(choice1):
	if choice1 == 1:
		return "EAT IT!"



print "Should you eat that bacon?"

def main():
	global choice1
	choice1 = raw_input("Do you want to feel like angels are froclicking on your tastebuds? 1- Yes 2- No 3- Yes, But I'm AFRAID bacon will KILL ME!")

	if choice1 == "1":
		eat(1) 
	elif choice1 == "2":
		print "You've clearly never tasted bacon."
		eat(1)
	else:
		print "Yes, but I'm afraid bacon will kill me!"
		choice2 = raw_input("Are your a coward?? 1- I AM NOT! 2- Yes, I am a coward")
			if choice2 == "1":
				print "THEN" + eat



if __name__ == '__main__': 
		main()

# # my_list = [1, 2, "kitten", 4, "five"]
# # print my_list[2]
# # print my_list[3]
# # print my_list[1]
# # print my_list[-1]
# # print my_list[4]
# # # print my_list[:]
# # print my_list[len(my_list)-1]
# print my_list[len(my_list)-1]



