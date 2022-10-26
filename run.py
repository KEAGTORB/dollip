import time
import os

os.system("clear")

print('''simple TOR ip changer \n   please wait...''')
os.system("service tor start")

time.sleep(5)
os.system("service tor start")
se = input("Time to change Ip in Sec *60*: ")
m = input("How many times do you want to change your ip *1000*: ")

for i in range(m):
    time.sleep(se)
    os.system("service tor reload")
    print("*Your IP has been Changed*")