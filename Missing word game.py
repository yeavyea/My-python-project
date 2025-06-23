import time
choices = ["Mother","Boba","toys"]
print("Welcome to the missing word game\n")
def question():
    answer = input("\nWhich is the missing word?\nMother\nBoba\ntoys")
    return answer
question1 = "________ and father made up a family."
print(question1)
answer = question()
if answer == choices[0]:
    print("Brilliant, well done!")
else:
    print("Sorry, let's try another.")
time.sleep(3)

question2 = "Zillean's favorite drink is ______."
print(question2)
answer = question()
if answer == choices[1]:
    print("Amazing,totally right!")
else:
    print("Ops, maybe it's just not the right one.")
time.sleep(3)

question3 = "Children love _____, adult as well."
print(question3)
answer = question()
if answer == choices[2]:
    print("Excellent! (;")
else:
    print("Ehn, not even a matter.")
time.sleep(3)



