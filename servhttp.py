import webserv
import webbrowser
import os
from sys import argv
import random

HOST = '127.0.0.1'
iniPORT = 50000
newPORT = random.randint(50000,60000)
CODESTR = "shirlimirli"
runningport = iniPORT
isrepliyed = 0

print(argv)

if len(argv) == 1:
    querystr = ''
else:
    querystr = "{" + ",".join(argv[1:]) + "}"
#

currentfolder =  os.path.dirname(os.path.realpath(__file__))

htmlfilepath = "file://" + currentfolder + "/index.html"

webbrowser.open(htmlfilepath) #open html file of the UI

serv = webserv.HttpServer((HOST,iniPORT),webserv.Handler,CODESTR,newPORT)

while isrepliyed == 0:
    isrepliyed = serv.run_once()
    print(isrepliyed)
#

serv.close()
serv = webserv.HttpServer((HOST,newPORT),webserv.Handler,'',newPORT)
serv.run_continuously()

