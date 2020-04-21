import time
import winsound
print("welcome to thought buddy")
time.sleep(2)
print ("if you would like to learn more type about, if you want to proceed type proceed")
notion = input()
if notion != "proceed":
    print ("Thought buddy is a simple reminder program that reminds you to do things or can be used to send thoughts you would like later on.")
    time.sleep(4)
    print ("It is totally trustable program although it sucks at its job.")
    time.sleep(4)
    print ("Thought buddy works you typing a thought and when you want it presented to you")
    time.sleep(4)
    print ("This program was made by the github user you got it from stupid and he kinda sucks a coding sooooooooo, dont get your hopes up")
    time.sleep(5)
print ("now lets get started")
time.sleep(1)
print ("please select the first time unit in hours here is the format this program uses Hours/minutes/secounds")
time.sleep(3)
print ("please select how many hours")
hour = input()
hour = int(hour)
hours = hour * 3600
print ("now select how many minutes")
minute = input()
minute = int(minute)
minutes = minute * 60
print ("now select how many seconds")
seconds = input()
seconds = int(seconds)
total = hours + minutes + seconds
print ("now what do you want the message to be?")
message = input()
print ("when you want the timer to begain type start")
startnotion = input()
if startnotion != "start":
    print("welp thats not what i asked you to put i guess you'll have to restart")
    time.sleep(1)
    exit()
print ("started timer!")
time.sleep(total)
print(message)
winsound.Beep(32767, 1000)
time.sleep(1)
winsound.Beep(32767, 1000)
time.sleep(1)
winsound.Beep(32767, 3000)
print("Thank you for using this program, in the current version you must restart the program to set another reminder")
time.sleep(3)
print("bye!")
exit()
    



    

