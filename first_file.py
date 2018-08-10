import socket
import os 
import sys
import platform


print  ("Name:" +socket.gethostname()) 

print ("System Platform: "+sys.platform)
print ("Machine: " +platform.machine())

print ("Platform: "+platform.platform())
print ("Pocessor: " +platform.processor())
print ("System OS: "+platform.system())
print ("Release: " +platform.release())

