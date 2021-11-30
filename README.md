# html_gui_for_python
The project is a framework for coding UI using the regular HTML5 instruments. Browser contacts python local webserver and the operation is performed by python. 
Data is passed from browser to python using multipart POST requests. User can pass both data and files to python server. The same can be returned back to the browser.

Python modules are: 
1. servhttp.py which serves as main. It holds the constants and custom function made by the developer with all its code. Now it is called "myfunc" and stored in module "myfunc". developer is free to change its name, provided that she changes its name in the servhttp.py too.
2. webserv.py which holdes the code related to the webserver operation. It shouldn't be changed.
3. post.py which parses multipart post requests and returns methos _POST() and _FILES() alike PHP $_POST[] and $_FILE[]. These are dictionaries, where _POST() provides dictionary of key (the variable name provided in post request) and value. _FILES() provides dictionary with keys, like the former, and values is a list of file name and the file.
4. myfunc.py - Developers custom function. the process that the app is supposed to do. Developer is free to change its name and the module's name, provided that he changes these names in file serhttp.py too.

Javascript file:
- uiclient.js - includes the intial port number 50000, onloadfunc method to intiate connection and window.addEventListener('beforeunload') to send the close request to server.
other methods are customizable by the developer.

Method of connection:
- The connection if performed the as this way: browser connects server on initial port 50000. It sands a code word, which may simply be the name of the application. it is used only to distinguish this call from other apps calls. When server receives the code word, it chooses a random number between 50000 and 60000 which will serve as new port. it passes this random number to the browser. Javascript code sets this number as a new port for future connections. Server too sets the new port for future connections. From now on and until the browser is closed, they talk to each other on a new port. When Browser is closed it sends a last request "close". server receives it and quits python.

Arguments:
- servhttp.py can be started with command line arguments written like (html element id):value (html element id):value and so on. Javascript will try to find elements with such ids and set their values to respective values from arguments line.
