from time import *
import random as r

#finding the Error

def mistake(partest,usertest):
        error = 0
        for i in range(len(partest)):
                try:
                        if partest[i] != usertest[i]:
                                error = error + 1
                except:
                        error = error + 1
        return error

#Finding the typing speed

def speed_time(time_s,time_e,userinput):
        time_delay = time_e - time_s
        time_R = round(time_delay,2)
        speed = len(userinput)/time_R
        return round(speed)


while True:
        ck  = input("Are you ready-- YES/NO : ")
        if ck == "YES":

             test = ['My name is ubaid Ali and I am from kiratpur district bijnor',"I have done Btech from Bijnor with the specializaton in Computer SCience",
                      "My hobbies are Watching sci-fi Movies and Singing"]
             test1 = r.choice(test)
             print("       ******Typing speed******")
             print(test1)
             print()
             print()
             time_1 = time()
             testinput = input(" Enter : ")
             time_2 = time()

             print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")
             print('Error : ', mistake(test1,testinput))

        elif ck == "NO":
                print("thank you ::")

        else:
                print("wrong input::")
