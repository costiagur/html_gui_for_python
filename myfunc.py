import base64
import json
import post


def myfunc(obj,queryobj):

    postdict = queryobj._POST()
    filesdict = queryobj._FILES()

    print(obj)

    print("POST = " + str(postdict) + "\n")
    print("FILES = " + str(filesdict) + "\n")

    # reply message should be encoded to be sent back to browser ----------------------------------------------
    # encoding to base64 is used to send ansi hebrew data. it is decoded to become string and put into json.
    # json is encoded to be sent to browser.

    file64enc = base64.b64encode(filesdict['doc1'][1])
    file64dec = file64enc.decode()

    replymsg = json.dumps([filesdict['doc1'][0],file64dec]).encode('UTF-8')

    return replymsg
#