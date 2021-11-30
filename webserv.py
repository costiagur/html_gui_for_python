import http.server
import post
from sys import exit
from myfunc import myfunc


class Handler(http.server.BaseHTTPRequestHandler):
    def setcodeword(self, codestr):
        self.CODESTR = codestr
        self.REPLIYED = 0
    #

    def setnewport(self,newPORT):
        self.newPORT = newPORT
    #

    def processing(self,queryobj):
        
        postlist = queryobj._POST()

        if('request' in postlist.keys()):
            if postlist['request'] == 'close':
                exit()
            #
            elif postlist['request'] == self.CODESTR: 
                self.REPLIYED = 1
                return str(self.newPORT).encode()
        #

        return myfunc(queryobj)
    #

    def set_headers(self):
        self.send_response(200) 
        self.send_header('Content-Type', 'text/html')
        
        self.send_header('Access-Control-Allow-Origin', 
                        self.headers['Origin']
                        ) #local file sends origin header 'null'. 
        
        self.send_header('Vary','Origin')
        self.end_headers()
    #

    def do_POST(self):

        if self.client_address[0] != '127.0.0.1': #check that request comes from local computer
            return
        #

        queryobj = post.POST(self)

        replymsg = self.processing(queryobj) #,self.custmethod)

        self.set_headers() #set headers of response
        
        self.wfile.write(replymsg) #send bytes = write to socket

        return
    #

    def isrepliyed(self):
        return self.REPLIYED
    #
#

class HttpServer(http.server.HTTPServer):
    def __init__(self,address_tuple,useHandler,codestr,newPORT):
        
        self.address_tuple = address_tuple
        self.useHandler = useHandler

        super().__init__(self.address_tuple,self.useHandler)
        
        useHandler.setcodeword(useHandler,codestr)
        useHandler.setnewport(useHandler,newPORT)
    #

    def run_once(self):      
        self.handle_request()
        return self.useHandler.isrepliyed(self.useHandler)
    #
    
    def close(self):
        self.server_close()
    #

    def run_continuously(self):
        self.serve_forever()
    #
#