import time
import os

def pomodoro_clock():
    study_time = int(input("Enter study time (in minutes): "))
    break_time = 5
    while True:
        os.system('cls') 
        print("Study for the next " + str(study_time) + " minutes.")
        time.sleep(study_time*60)
        os.system('cls') 
        print("Break for the next " + str(break_time) + " minutes.")
        time.sleep(break_time*60)
        os.system('cls') 
        print("Time to start studying again!")
        time.sleep(2)

if __name__ == '__main__':
    pomodoro_clock()
