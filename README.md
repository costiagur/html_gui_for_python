# html_gui_for_python
HTML5 GUI for python app 
The project creates HTML5 UI for an app written in Pyhon. Developer can create an HTML5 (HTML, CSS, Javascript) page locally as GUI while the processes will be done by Python.
Python creates a local web server that connects HTML5 user interface with python backoffice code. 
Python modules are: servhttp.py which should serve as main. It imports webserver.py which does POST request parsing, myfunc.py that holds users custom code and backholder.py, which includes TKinter frame that prevents webserver from closing. By closing tkinter window, user closes also the main code.
Myfunc module includes myfunc function in which user adds his own code. Parsed POST request is passed to the function as dictionary called querydict.
Connection port is set randomly between 50000 and 60000, in case several servers will be run on the same computer. Port number is passed to javascript simply by updating uiclient.js file.
Program can be started with command line arguments. this argumets are written as field id:value, e.g. id1:'my test'. 
Closing browser's tab or the browser should close Tkinter's frame.
Note that uploading and saving files can be done using Tkinter built in dialoges instead of POST uploading. It is especially useful if you want to place the saved file in a preset locations, instead of download or other default folder of the browser. 
Types: ordinary inputs are strings, files are bytes.
