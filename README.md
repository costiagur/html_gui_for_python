# html_gui_for_python
HTML5 GUI for python app 
The project creates HTML5 UI for an app written in Pyhon. Developer can create an HTML5 (HTML, CSS, Javascript) page locally as GUI while the processes will be done by Python.
Python creates a local web server that connects HTML5 user interface with python backoffice code. 
Python modules are: servhttp.py which should serve as main. it imports webserver.py which does POST or GET request parsing, myfunc.py that holds users custom code and backholder.py, which includes TKinter frame that prevents webserver from closing. By closing tkinter window, user closes also the main code.
Myfunc module includes myfunc function in which user adds tis won code. Parsed POST request is passed to the function as dictionary called querydict.
Connection port is set randomly between 50000 and 60000, in case several servers will be run on the same computer. Post number is passed to javascript simply by updating uiclient.js file.
Types: ordinary inputs are strings, files are bytes.
