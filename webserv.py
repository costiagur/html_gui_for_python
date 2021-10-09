import http.server
#import backholder
import post
from sys import exit

class webserv(http.server.BaseHTTPRequestHandler):

    def processing(self,queryobj,customfunc):
        
        postlist = queryobj._POST()

        if('request' in postlist.keys()):
            if postlist['request'] == 'close':
                #backholder.holderclose()
                exit()
            #
        #
        
        return customfunc(queryobj)
    #

    def custmethod(self):
        pass
    #

    def _set_headers(self):
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

        replymsg = self.processing(queryobj,self.custmethod)

        self._set_headers() #set headers of response
        
        self.wfile.write(replymsg) #send bytes = write to socket

        return
    #
#