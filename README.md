Definition box HTTP server
=============

This is a 5 mins solution to have up and running an HTTP server to get static files.

The primary goal of this tiny project is provide a quick solution to access to Swagger definition files directly from Maven in order to generate Spring-compliant apis and models (for further details take a look at poc-swagger-plugin).


Usage
-----

The HTTP server is based on python 3.x (http.server); to start the server type:

  python3 httpd.py

To stop the server press CTRL+c (keyboard interrupt)
