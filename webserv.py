import http.server
import urllib
import backholder
import post

class webserv(http.server.BaseHTTPRequestHandler):

    def processing(self,queryobj,customfunc):
        
        postlist = queryobj._POST()

        if('request' in postlist.keys()):
            if postlist['request'] == 'close':
                backholder.holderclose()
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

    def do_GET(self):

        if self.client_address[0] != '127.0.0.1': #check that request comes from local computer
            return
        #

        querystr = urllib.parse.parse_qs(self.path[2:],True)
                    #first is /, second is ?. threfore everything after them
        
        #print(querystr) #querystr is dict with the request data. names as keys.

        msg = self.processing(querystr,self.custmethod) #insert your reply into this variable. it should note be bytes. Else remove encode() below

        msgb = msg.encode() #convert to bytes to be sent

        self._set_headers() #set headers of response
        
        self.wfile.write(msgb) #send bytes = write to socket

        return
    #
#