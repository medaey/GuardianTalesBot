import time
from homeWorkflow import getDailyShop
from adventureWorkflow import getDailyDonjon
from guildWorkflow import getDailyGuild

dailyShop = False
dailyDongeon = False
dailyGuild = False
dailyEvent = False
dailyFarm = False

time.sleep(1)
if dailyShop != True:
    print("getDailyShop")
    getDailyShop()
    dailyShop == True

time.sleep(1)
if dailyDongeon != True:
    print("getDailyDonjon")
    getDailyDonjon()
    dailyDongeon == True

time.sleep(1)
if dailyDongeon != True:
    print("getDailyGuild")
    getDailyGuild()
    dailyDongeon == True