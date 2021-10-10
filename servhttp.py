import webserv
import webbrowser
#from socketserver import ThreadingMixIn
#import threading
import os
#import backholder
import http.server
import myfunc
import random
from sys import argv

HOST = '127.0.0.1'
PORT = random.randint(50000,60000)

print(argv)

querystr = ''

if len(argv) == 1:
    pass
else:
    querystr = "{" + ",".join(argv[1:]) + "}"
#

currentfolder =  os.path.dirname(os.path.realpath(__file__))

with open(currentfolder + "/uiclient.js", mode="r", encoding="UTF-8") as jsfile:
    existingjs = jsfile.readlines() #read all lines from uiclient,js file
#

with open(currentfolder + "/uiclient.js", mode="w", encoding="UTF-8") as jsfile: #insert ui.host in JS file with random PORT num
    for jsline in existingjs:
        if jsline.find("ui.host = 'http://localhost") != -1: #file existing ui.host line and replace it
            jsfile.write("ui.host = 'http://localhost:%i'\n" %(PORT))
        #
        elif jsline.find("ui.queryobj =") != -1:
            jsfile.write("ui.queryobj = " + querystr + "\n")
        #
        else:
            jsfile.write(jsline) #all other lines write what was there
        #
    #
#


htmlfilepath = "file://" + currentfolder + "/index.html"

#class ThreadedHTTPServer(ThreadingMixIn, http.server.HTTPServer):
#    pass
#

webbrowser.open(htmlfilepath) #open html file of the UI

webserv.webserv.custmethod = myfunc.myfunc #provide my custom function to POST of webserver

#serv = ThreadedHTTPServer((HOST,PORT),webserv.webserv) #threading HTTPserver
serv = http.server.HTTPServer((HOST,PORT),webserv.webserv)

#server_thread = threading.Thread(target=serv.serve_forever) #preparing thread because tkinter can't run in the same thread with httpserver
#server_thread.start()
serv.serve_forever()

#backholder.holderrun("MyUI") #Run Tkinter to hold the server in the background

#serv.shutdown()
