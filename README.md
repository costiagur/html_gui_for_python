# HTML_gui_for_python
The project is a framework for coding UI using the regular HTML5 instruments. Browser contacts python local webserver and the operation is performed by python. 
Data are passed from browser to python using multipart POST requests. User can pass both data and files to python server. The same can be returned back to the browser.

## Python modules are: 
1. main.py serves as main. It shouldn't be changed.
2. webserv.py which holdes the code related to the webserver operation. It shouldn't be changed.
3. post.py which parses multipart post requests and returns methos _POST() and _FILES() alike PHP $_POST[] and $_FILE[]. These are dictionaries, where _POST() provides dictionary of key (the variable name provided in post request) and value. _FILES() provides dictionary with keys, like the former, and values are a list of file names and files. It shouldn't be changed.
4. common.py which holds functions and keywords common to other files in the project. It should not be changed.
5. myfunc.py - Developer's custom function. The process that the app is supposed to do.

## Javascript files:
- uiclient.js - Is produced on start with a vacant port. It includes window.addEventListener('beforeunload') to send the close request to server. Don't change it.
- myfunc.js - includes developer's custom methods.

## HTML file:
index.html - User's custom gui, with connections to js files.

## Method of connection:
- Browser connects python http server on initial free port between 50000 and 59999. When the browser is closed it sends a last request "close". The Server receives it and quits python.

## Arguments:
- main.py can be started with command line arguments written like (html element id):value (html element id):value and so on. Javascript will try to find elements with such ids and set their values to respective values from arguments line.
