import random

NUMBER_OF_TRIALS=1000000
numberofhits=0

for i in range(NUMBER_OF_TRIALS):
    x=random.random()*2-1
    y=random.random()*2-1
    if x*x+y*y<=1:
        numberofhits+=1

pi=4*numberofhits/NUMBER_OF_TRIALS
print("pi is:",pi)