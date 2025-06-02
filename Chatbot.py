#Chatbot
import random
import time
chatHobbies = ["sleeping in my bed","drawing","running","cycling","reading","gaming","painting"]
print("Welcome to Yeavyea Chatbot!")
name = input ("What is your name?")
print("Hello", name,"nice to meet you!")
time.sleep(1)
hobbie = input ("What is your favorite thing to do?")
time.sleep(2)
print("That sounds great, I really love", random.choice(chatHobbies))
day = input("Have you had a good day?")
day = day.lower()
if day == "yes":
    print("Good to hear that, me2!")
else:
    print("Oh, I'm so sorry to hear that, hope it's better tomorrow.")
print("Really enjoyed the chat, speak to you again soon.")
