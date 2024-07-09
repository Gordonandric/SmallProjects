# Gordon
# Programming
# 23 Oct 9
# I'm Amazing Bonus
# Create a list of 5 bad and good varible names and state why them are good or bad

illegallist = [" 3bee, good morning, -name, true, am-god "]
legallist = ["good, Ag3, Bob_Job, potato_tomato, AMAZING"]
goodlist = ["Name, Age, Favorite_Fruit, Buyer, Total_cost"]
badlist = ["notallowedifbobtriestorun, lOl, brb, stor_def_of_word_in_list_called_list3, defs_of_good_words_and_bad_word "]

print("\n\nIllegal Variables")
print(illegallist)
print("\n3bee is illegal because a variable cannot start with a number")
print("\ngood morning is illegal because you cannot have a space in a variable")
print("\n-name and am-god are illegal because you cannot use a - in a variable")
print("\ntrue is illegal because you cannot use pythons keywords as variables")

import time
time.sleep(2)

print("\n\nLegal variables")
print(legallist)
print("\ngood is legal since it follows all of pythons rules")
print("\nAg3 is legal since the number is not the first character")
print("\nBob_Job and potato_tomato are legal since _ is legal to be used in variables")
print("\nAMAZING is allowed since it starts with a letter even caps are allowed")

time.sleep(2)

print("\n\nGood variables")
print(goodlist)
print("\nName, age, Favorite_fruit, Buyer and Total_cost are all good variables because they are all legel,not too long, and they indicate their use.")

time.sleep(2)

print("\n\nBad variables")
print(badlist)
print("\nnotallowedifbobtriestorun, stor_def_of_word_in_list_called_list3, defs_of_good_words_and_bad_word are all legal but bad variable names because they are too long and dont indicate a clear use")
print("\nlOl and brb are both legal but bad variable names because they both are abrevations which means they represent something but they dont state a clear meaning.")

input("\n\nPress the enter key to exit.")