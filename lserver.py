import requests
from LaptopController import lbot
from LaptopController.lbot import Laptop
import os

bot = Laptop("lconfig.cfg")


def make_reply(msg):
    msg = msg.lower()
    reply = None
    if msg == "/start":
        reply = "Welcome. Control Your Laptop through your phone"
    elif msg == "open padre":
        opadre = "C:\\Dwimperl\\perl\\site\\bin\\padre.exe"
        os.startfile(opadre)
        reply = "Padre perl will be running within a minute"
    elif msg == "close padre":
        os.system("TASKKILL /F /IM padre.exe")
        reply = "Padre perl has being closed."
    elif msg == "open eclipse":
        eclipse = "C:\\Users\\Sourav\\eclipse\\java-2019-12\\eclipse\\eclipse.exe"
        os.startfile(eclipse)
        reply = "Eclipse will be running within a minute"
    elif msg == "close eclipse":
        os.system("TASKKILL /F /IM eclipse.exe")
        reply = "Eclipse has being closed."
    elif msg == "open intellij":
        intellij = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.1.2\\bin\\idea64.exe"
        os.startfile(intellij)
        reply = "Intellij ide will be running within a minute"
    elif msg == "close intellij":
        os.system("TASKKILL /F /IM idea64.exe")
        reply = "Intellij ide has being closed."
    elif msg == "open netbeans":
        neatbean = "C:\\Users\\Sourav\\Desktop\\Final Year Project\\NetBeans 8.2\\bin\\netbeans64.exe"
        os.startfile(neatbean)
        reply = "Netbeans ide will be running within a minute"
    elif msg == "close netbeans":
        os.system("TASKKILL /F /IM netbeans64.exe")
        reply = "Netbeans ide has being closed."
    elif msg == "open chrome":
        chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome)
        reply = "Google Chrome will be running within a minute"
    elif msg == "close chrome":
        os.system("TASKKILL /F /IM chrome.exe")
        reply = "Chrome has being closed."
    elif msg == "open visual studio code":
        vscode = "C:\\Users\\Sourav\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(vscode)
        reply = "Visual studio code will be running within a minute"
    elif msg == "close visual studio code":
        os.system("TASKKILL /F /IM code.exe")
        reply = "Visual studio code has being closed."
    elif msg == "open firefox":
        firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(firefox)
        reply = "Firefox will be running within a minute"
    elif msg == "close firefox":
        os.system("TASKKILL /F /IM firefox.exe")
        reply = "Firefox has being closed."
    elif msg == "open devcpp":
        devcpp = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
        os.startfile(devcpp)
        reply = "DevCpp will be running within a minute"
    elif msg == "close devcpp":
        os.system("TASKKILL /F /IM devcpp.exe")
        reply = "DevCpp has being closed."
    elif msg == "open microsoft edge":
        msedge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(msedge)
        reply = "Microsoft Edge will be running within a minute"
    elif msg == "close microsoft edge":
        os.system("TASKKILL /F /IM msedge.exe")
        reply = "Microsoft edge has being closed."
    elif msg == "open visual studio":
        vs = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
        os.startfile(vs)
        reply = "Visual Studio will be running within a minute"
    elif msg == "close visual studio":
        os.system("TASKKILL /F /IM devenv.exe")
        reply = "Visual Studio has being closed."
    elif msg == "open pycharm":
        pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
        os.startfile(pycharm)
        reply = "Pycharm will be running within a minute"
    elif msg == "close pycharm":
        os.system("TASKKILL /F /IM pycharm64.exe")
        reply = "Pycharm has being closed."
    else:
        reply = "No such executable file exists."
    return reply


update_id = None

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = 1
            if message != 1:
                from_ = item["message"]["chat"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, from_)