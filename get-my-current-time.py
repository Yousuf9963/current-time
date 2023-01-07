print("[&] Coded By Yousuf Shafi'i Muhammad Junior Programmer")
print("")
print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog")
print("")
print("This Program will tell you your current time")
print("")

print("Contact on Telegram: https://t.me/Juniorprogrammerboy")
print(" I hope for you good future and i am willing that you will come high effort.")
print("")

import time

t = time.localtime(time.time())
localtime = time.asctime(t)
str ="Your Current Time is:" + time.asctime(t)

print(str);
