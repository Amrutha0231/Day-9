import socket
import psutil
def check_internet_connection():
    remote_server = "www.google.com"
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((remote_server, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()
if check_internet_connection():
    print("Connection Status: Connected")
else:
    print("Connection Status: Not Connected")

def get_Host_name_IP():
	try:
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		print("Hostname : ", host_name)
		print("IP : ", host_ip)
	except:
		print("Unable to get Hostname and IP")

def available_Interfaces():
    try: 
         available_if=psutil.net_if_stats()
         print("Available Interfaces: ", available_if)
    except:
         print("Unable to get Available Interfaces.")

get_Host_name_IP() 
check_internet_connection()
available_Interfaces()
