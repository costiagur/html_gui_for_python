# html_gui_for_python
HTML5 GUI for python app 
The project aims to create HTML5 GUI for running Pyhon code. Developer can create his own HTML5 page locally as GUI while the processes will be done by python. The python file of this project will connect between them. Python code is running http server from http.server.BaseHTTPRequestHandler class. Request from the GUI is sent as POST or GET request. do_POST function: Parses POST requests. Produces querystr dict which includes request's names as key and value holds tuple of filenames and file or text sent. 
Types: ordinary inputs are strings, files are bytes. 
To send reply to the GUI insert your reply into replymsg variable. The project includes example with base64 encoding. There is a placeholder to write you own code in the do_POST function.
I used AJAX to send and recieve requests from the server. The project includes an example of html and javascript files of GUI.

do_GET function: Parses GET requests. Produces urldict dict which includes request's names as key and values as values. Doesn't receive files. To send reply to the GUI insert your reply into replymsg variable.
