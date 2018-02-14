#/usr/bin/python3

import socket
import sys



def GetArguments():

   global ip
   global path
   global Write
   
   try:
       ip = sys.argv[1]   
   except IndexError:
     
      try:
       ip = str(input("[?]Ip >>")) 
      except KeyboardInterrupt:
        print("[!]You pressed ctr+x")
        print("[*]Exiting...")
        sys.exit()
      except EOFError:
        sys.exit()
      except Exception as e:
       print("[!]Error :",str(e))    
   except Exception as e:
     print("[!]Error :",str(e))
     
   try:
     path = sys.argv[2]
     Write = True
   except IndexError:  
     try:  
      path = str(input("[?]Path >>"))
      if path == "":      
         Write = False
      else:
        Write = True     
     except KeyboardInterrupt: 
        print("[!]You pressed ctr+x")
        print("[*]Exiting...")
        sys.exit()   
     except EOFError:   
        sys.exit()     
     except Exception as e:    
       print("[!]Error :",str(e))
       sys.exit()     
   except Exception as e:   
     print("[!]Error :",str(e))
     sys.exit()
     


def Lookup():

    global ip
    global output

    try:
      domain = socket.gethostbyaddr(ip)
      output = "~IpLookup: \n\t"+"Ip: "+ip+"\n\t"+"Domain 1: "+''.join(domain[0])+"\n\t"+"Domain 2: "+''.join(domain[1])+"\n"
      print(output)
    except Exception as e:
      print("[!]Error: ",str(e))
      sys.exit()



def WriteToFile():

    global path
    global output
    global Write
    
    try:
        if Write == True:
           file = open(path,"a")
           file.write(output)
           file.close()
        elif Write == False:
            sys.exit()
    except FileNotFoundError:
        print("[!]Path doesn't exists.")
    except Exception as e:
        print("[!]Error: ",str(e))
        sys.exit()


        
def ipLookup():

    GetArguments()
    Lookup()
    WriteToFile()
    
ipLookup()
