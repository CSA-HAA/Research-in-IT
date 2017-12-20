import socket, sys
from threading import Thread

open('ports.txt', 'w').close()

ip = "172.17.2."
end = 99
IPs = []
for i in range(155):
    end+=1
    IPs.append(ip + str(end))

## Enter Host to scan
for i in IPs:

    threads = []
    timeout = 0.5

    # Inputs & simple error handling
    try:
        host = i
        hostIP = socket.gethostbyname(host)
        with open("ports.txt" ,"a") as f:
            f.write(i+'\n')
    except:
        print("User input error! Please re-enter information in proper format")
        sys.exit()


    print("Scanning Target: ", hostIP)

    # Scanning and open port display
    def scanner(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout)
        result = sock.connect_ex((hostIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
            with open("ports.txt", "a") as f:
                f.write("Port {}: Open".format(port) + '\n')
        sock.close()


    # Setup threading and calling the scan
    for i in [22, 25, 80]:
        thread = Thread(target=scanner, args=(i,))
        threads.append(thread)
        thread.start()

    [x.join() for x in threads]