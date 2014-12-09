Telephone_Directory-Client-and-Server
======================================

This repo is about the telephone directory which is at server side and client is on another side .
Client can update,modify,insert into telephone directory only via interacting with server .

Code is written in python. 
It uses XML-RPC server for connection between server and client.
And  MySQL database for storing telephone directory database.
For running this program on local machine , you need to have XAMP/WAMP/APACHE

Basic operation:
Server listens to a unique port number and when client send connection request to the server . It accepts and provide interface to the client to interact with telephone database.
