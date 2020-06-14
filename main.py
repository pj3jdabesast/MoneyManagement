textFile = open("Savings.txt", "a")

how_many_payments = int(input("How many payments are mandatory for the month? (ex. Groceries, Rent, Cable Bill, Electricity Bill, etc.)\n"))

budget = int(input("What is your monthly budget\n"))
moneySpent = []

x = 0
while x <= (how_many_payments - 1):
 
  task = int(input("How much money will you spend on payment " + str(x + 1) + "?\n"))
  
  moneySpent.append(task)
  if budget > task:
    x += 1
  else:
    print("you have exceeded your budget")
    break


sum = 0
for m in moneySpent:
  sum = sum + m

remainder = (int(budget) - sum)
if budget > sum:
	textFile.write(str(remainder) + " dollars to spend\n")
	print("You saved " + str(remainder) + " Dollars this month!")
elif budget == sum:
	print("You spent all your money. Not even a penny remaining.")
else:
	print("You are in debt.\n")

textFile.close()




