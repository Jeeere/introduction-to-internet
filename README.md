# introduction-to-internet
Course work for the course Introduction to Internet 2021.

A client program which can receive and send messages according the protocol specified. The program first performs a handshake with the server using TCP and then uses UDP for sending and receiving messages.

Basic outline of the program:
• Program takes server address and port as command line argument
• Program uses TCP to connect to the server, negotiates possible extra features and encryption keys with server and receives an identity token and the server's UDP port
• Program initiates UDP messaging by sending the first message
• Server sends a message with random words
• Program replies with the words in reverse order
• Server sends new messages random number of times
• Finally, the server sends a message telling the exchange is finished
