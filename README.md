# TCP/UDP Simple Calculator



Here is a demo of the program

## Overview

This is a simple calculator written in Python for CS 453 (Computer Networks) at UMass which emulates sending data with TCP and UDP (reliably or unreliably). \
On localhost, the client will send in a text file with a specific format and the server (on port 50500) will perform the simple arithmetic and send the results back to the client. 

## Specifications

* ### Client
    * Each line in the txt file must contain a triplet: OC Num1 Num2 (example: + 2 7).
    * Each number can only be integers and the OC must be one of the following: addition (+), subtraction (-), division (/), or multiplication (*).

* ### Server
    * If the OC is not one of the previous above send back an error code 620 (Invalid OC).
    * If the numbers are not integers or you are dividing by 0, send back error code 630 (Invalid operands).
    * If there is an exception, send it back as the code and the message of the exception.
    * Otherwise, send code 200 (success) and the result.

## Usage
Please run each server and client with the same prefix/suffix ie. `TCP`_Client with `TCP`_Server \
\
To use the calculator, in your terminal run the server.\
In a different terminal window, run the corresponding client with a txt file input.\
\
If you want to simulate an unreliabe connection with UDP, the parameters for the server are: \
`p` the probability of dropping a received datagram and a integer `seed` for seeding a random number generator (for consistency) \
Example: `py UDP_Server-Unreliable.py 0.5 2 `\

## Motivation
This was a means to understand how TCP and UDP works through a simple application.\

