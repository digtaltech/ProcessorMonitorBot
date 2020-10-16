import socket
import threading
import os
import json


bind_ip = ''
bind_port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections


def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    if (format(request) == "1"):
        server = 0
        server = os.system('tasklist | find "SenetServerUpdate.exe"')
        if (server == 0 or 1):
            gpu_mining = os.system('tasklist | find "EthDcrMiner64.exe"')
            gpu_status = 0
            if (gpu_mining == 0):
                try:
                    request = {"id": 0, "jsonrpc": "2.0", "method": "miner_getstat1"}
                    with socket.create_connection(('localhost', 3333)) as sock:
                        sock.sendall(json.dumps(request).encode())
                        sock.sendall(os.linesep.encode())
                        sock.shutdown(socket.SHUT_WR)  # no more writing
                        with sock.makefile('r', encoding='utf-8') as file:
                            response = json.load(file)
                    gpu_status = int(response['result'][3])/1000
                except BaseException:
                    gpu_status = 0


            f1 = os.popen('tasklist | find "SenetServerUpdate.exe"').read()
            proc_count1 = len(f1.splitlines())

            f2 = os.popen('tasklist | find "xmrig.exe"').read()
            proc_count2 = len(f2.splitlines())

            f3 = os.popen('tasklist | find "EthDcrMiner64.exe"').read()
            proc_count3 = len(f3.splitlines())

            client_socket.send(('On [S:' + str(proc_count1) + ' C:' + str(
                proc_count2) + ' V:' + str(proc_count3) + '] - ' + 'Hashrate: ' + str(gpu_status)).encode('utf-8'))
            
        else:
            client_socket.send(('Off').encode('utf-8'))

    if (format(request) == "2"):
        mining = 1
        mining = os.system('tasklist | find "xmrig.exe"')
        if (mining == 0):
            client_socket.send(('Mining').encode('utf-8'))
        else:
            client_socket.send(('IDLE').encode('utf-8'))

    if (format(request) == "3"):
        server = os.system('tasklist | find "SenetServerUpdate.exe"')
        if (server == 0):
            killServer = os.system('taskkill /f /IM SenetServerUpdate.exe')
            startServer = os.system('C:\Senet\SenetServerUpdate.exe')
        else:
            startServer = os.system('C:\Senet\SenetServerUpdate.exe')

        client_socket.send(('Reload').encode('utf-8'))

    if (format(request) == "4"):
        os.system('taskkill /f /IM SenetServerUpdate.exe')
        os.system('taskkill /f /IM xmrig.exe')
        os.system('taskkill /f /IM EthDcrMiner64.exe')

        client_socket.send(('Kill Service').encode('utf-8'))
    # client_socket.send(('ASC').encode())
    client_socket.close()


while True:
    client_sock, address = server.accept()
    client_handler = threading.Thread(
        target=handle_client_connection,
        # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        args=(client_sock,)
    )
    client_handler.start()

# senet = 1;
# senet = os.system('tasklist | find "SenetServerUpdate.exe"')
# if (senet == 0):
#     f = os.popen('tasklist | find "SenetServerUpdate.exe"').read()
#     proc_count = len(f.splitlines())
#     if (proc_count > 1):
#         os.system('taskkill /f /IM SenetServerUpdate.exe')
#         os.system('taskkill /f /IM xmrig.exe')
#         os.system('taskkill /f /IM nbminer.exe')
#         os.system('SenetServerUpdate.exe')
# elif (senet == 1):
#     os.system('SenetServerUpdate.exe')
