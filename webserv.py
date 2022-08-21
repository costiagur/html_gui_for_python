import http.server
import common
import post
from sys import exit


class Handler(http.server.BaseHTTPRequestHandler):
    def setcodeword(self, codestr):
        self.CODESTR = codestr        
    #

    def setnewport(self,newPORT,querystr):
        self.newPORT = newPORT
        self.querystr = querystr       
    #

    def customfunc(self,funcobj):
        self.funcobj = funcobj
    #

    def processing(self,queryobj):
        try:        
            postlist = queryobj._POST()
            print(postlist)

            if('request' in postlist.keys()):
                if postlist['request'] == 'close':
                    exit()
                #
                elif postlist['request'] == self.CODESTR:
                    common.REPLIYED = 1

                    returnstr = '{"port":' + str(self.newPORT) + ', "args":' + self.querystr + '}'

                    return returnstr.encode()
            #

            return Handler.funcobj(queryobj)
        #
        except Exception as e:
            common.errormsg(title=__name__ + "_processing",message=e)
        #
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
#

class HttpServer(http.server.HTTPServer):
    def __init__(self,address_tuple,useHandler,codestr,newPORT,funcobj,querystr):
        
        self.address_tuple = address_tuple
        self.useHandler = useHandler

        super().__init__(self.address_tuple,self.useHandler)
        
        useHandler.setcodeword(useHandler,codestr)
        useHandler.setnewport(useHandler,newPORT,querystr)
        useHandler.customfunc(useHandler,funcobj)
    #

    def run_once(self):      
        try:
            self.handle_request()
        #
        except Exception as e:
            common.errormsg(title=__name__ + "_HttpServer",message=e)
        #
    #
    
    def close(self):
        self.server_close()
    #

    def run_continuously(self):
        self.serve_forever()
    #
#
