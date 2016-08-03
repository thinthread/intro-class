shopping_list = ["tires", "battery","wipers","oil"]
item = "new item"

def add(item):
	if item in shopping_list:
		print "You want more?"
		print shopping_list
	else:
		shopping_list.append(item)
		return shopping_list

def alph(shopping_list):
	shopping_list.sort()
	print shopping_list

def remove(item):
	shopping_list.pop()
	print shopping_list

def main():
	item = raw_input("What would you like to purchase?")
	add(item)
	choice = raw_input("Would you like to continue shopping? 1-No 2-Yes 3-Sort your cart 4- Check your cart 5- Remove last item")
	if choice == "1":
		print shopping_list
	elif choice == "2":
		item = raw_input("What would you like to purchase?")
		add(item)
	elif choice == "3":
		alph(shopping_list)	
	elif choice == "4":
		print shopping_list
	elif choice == "5":
		remove(item)
	else:
		print "Please make a valide choice"
	# alph (shopping_list)
	# remove (item)

if __name__ == '__main__': 
		main()
