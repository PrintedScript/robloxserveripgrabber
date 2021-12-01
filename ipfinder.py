import os
from datetime import datetime
import getpass
from colorama import Fore,Back,Style
from typing import Text
logdir = "C:/Users/"+getpass.getuser()+"/AppData/Local/Roblox/logs/"

while True:
    logslist = os.listdir(logdir)

    LatestLog = ""
    LastEditTime = 0
    for logfile in logslist:
        logedittime = os.path.getmtime(logdir+logfile)
        if logedittime > LastEditTime:
            LastEditTime = logedittime
            LatestLog = logfile

    with open(logdir+LatestLog,"r",encoding="utf8") as f:
        try:
            loglines = f.readlines()
        except:
            with open(logdir+LatestLog,"r",encoding="ANSI") as h:
                try:
                    loglines = h.readlines()
                except:
                    loglines = []

    jobid = Fore.RED+"failed"+Style.RESET_ALL
    placeid = Fore.RED+"failed"+Style.RESET_ALL
    serverip = Fore.RED+"failed"+Style.RESET_ALL
    spacedip = Fore.RED+"failed"+Style.RESET_ALL

    for line in loglines:
        if "[FLog::Output] ! Joining game " in line:
            sections = line.split(" ")
            jobid = sections[5]
            placeid = sections[7]
        
        if "[FLog::Output] Connecting to" in line:
            sections = line.split(" ")
            serverip = sections[4].split("\n")[0]
            TEMP = serverip.split(":")
            spacedip = TEMP[0] + " " + TEMP[1].split("\n")[0]
    
    os.system("cls")
    print(f"""
    Github Repo: https://github.com/PrintedScript/robloxserveripgrabber/releases

    Log file directory '{logdir}{LatestLog}'
    Last edited on: {str(datetime.fromtimestamp(LastEditTime))}

    PlaceId {Fore.LIGHTCYAN_EX}{placeid}{Style.RESET_ALL} | jobid {Fore.LIGHTMAGENTA_EX}{jobid}{Style.RESET_ALL}
    Server IP: {Fore.LIGHTGREEN_EX}{serverip}{Style.RESET_ALL}
    IP and Port: {Fore.GREEN}{spacedip}{Style.RESET_ALL}

    """)
    if loglines == []:
        print(Fore.RED+"FAILED TO READ LOG FILE, please send the log file to SomethingElse#0024 so I can fix this."+"\n"+Style.RESET_ALL)

    input("    Press Enter to grab latest log")
