#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# The modules required
import sys
import socket
import struct

'''
This is a template that can be used in order to get started. 
It takes 3 commandline arguments and calls function send_and_receive_tcp.
in haapa7 you can execute this file with the command: 
python3 CourseWorkTemplate.py <ip> <port> <message> 

Functions send_and_receive_tcp contains some comments.
If you implement what the comments ask for you should be able to create 
a functioning TCP part of the course work with little hassle.  

''' 

# python CourseWorkTemplate.py xxx.xxx.xx.xxx 10000 "HELLO"
 
def send_and_receive_tcp(address, port, message):
    print("You gave arguments: {} {} {}".format(address, port, message))
    # create TCP socket
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    # connect socket to given address and port
    s.connect((address, port))
    # python3 sendall() requires bytes like object. encode the message with str.encode() command
    message = message + "\r\n"
    print("Sent: " + message)
    message = message.encode()
    # send given message to socket
    s.sendall(message)
    # receive data from socket
    data = s.recv(1024)
    # data you received is in bytes format. turn it to string with .decode() command
    data = data.decode()
    # print received data
    print("Received: " + data)
    # close the socket
    s.close()
    # Get your CID and UDP port from the message
    message, cid, udp = data.strip("\r\n").split(" ")
    # Continue to UDP messaging. You might want to give the function some other parameters like the above mentioned cid and port.
    send_and_receive_udp(address, int(udp), cid)
    return
 
 
def send_and_receive_udp(address, port, cid):
    '''
    Implement UDP part here.
    '''
    print("This is the UDP part. Implement it yourself.")

    # create UDP socket
    s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    # Format and pack message
    message = "Hello from " + cid + "\n"
    packet = struct.pack("!8s??HH128s", cid.encode(), True, False, 0, len(message), message.encode().ljust(128))
    print("Sent: " + message)
    # send given message to given address and port using the socket.
    s.sendto(packet, (address, port))

    
    # Loop the following
    while True:
        # receive data from socket
        data,addr = s.recvfrom(1024)
        # Data you receive is in bytes format. Turn it to string with .decode() command
        data = data.decode()
        # Strip cid and unnecessary data from received message and print
        data = data[14:].strip('\x00')
        print("Received: " + data)
        # if received data contains the word 'Bye' break the loop
        if 'Bye' in data:
            break
        # Split data into list and reverse it
        message = data.split(" ")
        message.reverse()
        # Join list back into string
        message = " ".join(message)
        print("Sent: " + message)
        # Pack message
        packet = struct.pack("!8s??HH128s", cid.encode(), True, False, 0, len(message), message.encode().ljust(128))
        # Send packet to server
        s.sendto(packet, (address, port))
    
    # close the socket
    s.close()
    return
 
 
def main():
    USAGE = 'usage: %s <server address> <server port> <message>' % sys.argv[0]
 
    try:
        # Get the server address, port and message from command line arguments
        server_address = str(sys.argv[1])
        server_tcpport = int(sys.argv[2])
        message = str(sys.argv[3])
    except IndexError:
        print("Index Error")
    except ValueError:
        print("Value Error")
    # Print usage instructions and exit if we didn't get proper arguments
        sys.exit(USAGE)
 
    send_and_receive_tcp(server_address, server_tcpport, message)
 
 
if __name__ == '__main__':
    # Call the main function when this script is executed
    main()
