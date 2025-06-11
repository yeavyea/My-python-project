import random
#my first subprogram (procedure)
def Poavchou():
    print("She likes to shopping.")
    print("She lives in Siem Reap.")
    print("She loves fries.")
#call my subprogram
Poavchou()
Poavchou()
Poavchou()

#my second subprogram (function)
def average(x, y):
    return (x + y) / 2
    
#call my subprogram
print(average(5, 5))

#procedure
def Yeavyea():
    print("Yeavyea loves sleeping!")
Yeavyea()
Yeavyea()
Yeavyea()
Yeavyea()
Yeavyea()
Yeavyea()
Yeavyea()
Yeavyea()
Yeavyea()
Yeavyea()

#function
def sum(x ,y):
    return(x + y)
print(sum(2, 3))

def randomstudent():
    list = ["Yeavyea","Poavchou","William","Sereibot"]
    print(random.choice(list))
    
randomstudent()

def percentagecalculation(percentage, value):
    return (percentage * value) / 100
    
print(percentagecalculation(30, 70))
