import base64
import json


def myfunc(obj,querydict):

    print(obj)

    replymsg = base64.b64encode(querydict['doc1'][1])
                    #insert your reply into this variable. it should not be bytes. Else remove encode() below

    filedict = dict()

    filedict['filename'] = querydict['doc1'][0]
    filedict['filetext'] = replymsg.decode()

    msg = json.dumps(filedict)

    return msg
#