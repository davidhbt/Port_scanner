import nmap
import pyfiglet

scanner = nmap.PortScanner()

#banner
print('*' * 50)
print(pyfiglet.figlet_format("port scanner")) 
print('made by https://github.com/davidhbt, www.linkedin.com/in/david-habte-a7043a263')
print('*' * 50)


# Define target IP address or hostname
target = input("ip or host name: ")


print('fyp shitty internet = slow scan')
print(f'scanning {target}..........')
print('*' * 50)

#running a scan
scanner.scan(target)


for host in scanner.all_hosts():
    print("Host IP: ", host)
    print("State: ", scanner[host].state())
    for proto in scanner[host].all_protocols():
        print("Protocol in use: ", proto)
        ports = scanner[host][proto].keys()
        print('*' * 50)
        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])