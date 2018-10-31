import os

app = str(os.environ["app"])

if app == "telegram":
   print("Running telegram bot")
   os.system("python rpganswerstelegram.py")
elif app == "discord":
   print("Running discord bot")
   os.system("python rpganswersdiscord.py")
