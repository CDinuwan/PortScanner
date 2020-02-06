#!/usr/bin/env python3

import socket
import os
import sys
import subprocess

if __name__ == "__main__":

    try:
        
        print("┏━┓┏━┓┏━┓╺┳╸   ┏━┓┏━╸┏━┓┏┓╻┏┓╻┏━╸┏━┓")
        print("┣━┛┃ ┃┣┳┛ ┃    ┗━┓┃  ┣━┫┃┗┫┃┗┫┣╸ ┣┳┛")
        print("╹  ┗━┛╹┗╸ ╹    ┗━┛┗━╸╹ ╹╹ ╹╹ ╹┗━╸╹┗╸")
        print("		    created by-CDinuwan")
        s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(5)
        
        print(" 1.Select port in List : \n 2.Select custom port : \n 3.Upgrade Linux \n 4.Update Linux \n")
        selection=input("Enter Your Selection : \n")

        if selection=="1":
            print(" 1.Port 20-File Transfer Protocol(FTP) /n 2.Port-21-Dile Transfer Protocol(FTP) \n 3.Port-22-Secure Shell(SSH) \n 4.Port-23-Telnet \n 5.Port 25-Simple Mail Transfer Protocol(SMTP) \n 6.Port 53-Domain Name System(DNS) \n 7.Port 67-Dynamic Host Configuration Protocol(DHCP) \n 8.Port 68-Dynamic Host Configuration Protocol(DHCP)")
            print(" 9.Port 80-Hypertext Transfer Protocol(HTTP) \n 10.Port 110-Post Office Protocol(POP3) \n 11.Port 119-Network News Transfer Protocol(NNTP) \n 12.Port 123-Network Time Protocol(NTP) \n 13.Port 143-Internet Message Access Protocol(IMAP) \n 14.Port 161-Simple Network Management Protocol(SNMP) \n 15.Port 194-Internet Relay Chat(IRC) \n 16.Port 443-HTTP Secure(HTTPS) \n")

            
            port_num=input("Select port from list :")
            host=input("Enter the IP Address: ")

            if port_num=="1":
                if s.connect_ex((host,20)):
                    print("The port is closed")
                else:
                    print("The port is open")

            elif port_num=="2":
                if s.connect_ex((host,21)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="3":
                if s.connect_ex((host,22)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="4":
                if s.connect_ex((host,23)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="5":    
                if s.connect_ex((host,25)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="6":
                if s.connect_ex((host,53)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="7":
                if s.connect_ex((host,67)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="8":
                if s.connect_ex((host,68)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="9":
                if s.connect_ex((host,80)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="10":
                if s.connect_ex((host,110)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="11":
                if s.connect_ex((host,119)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="12":
                if s.connect_ex((host,123)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="13":
                if s.connect_ex((host,143)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="14":
                if s.connect_ex((host,161)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="15":
                if s.connect_ex((host,194)):
                    print("The port is closed")
                else:
                    print("The port is open")
                
            elif port_num=="16":
                if s.connect_ex((host,443)):
                    print("The port is closed")
                else:
                    print("The port is open")
                

        elif selection=="2":
        
            host=input("Enter the IP Address: ")
            port_num=int(input("Select port :"))

            if s.connect_ex((host,port_num)):
                print("The port is closed")
            else:
                print("The port is open")
        
        elif selection=="3":
            process = subprocess.call("sudo apt upgrade")

        elif selection=="4":
            process = subprocess.call("sudo apt upgrade")
        
        else:
            print("Invalid Selection")
    except ValueError as err:
        print(err)        
    except:
        print("This program didn't work correctly in you device or check your inputs")
