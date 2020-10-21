import socket 
import sys


def send_commands(s, conn):
    """get a comand from the user and send it to the client """
    print("control + C to kill the connection")

    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(1024)
                print(data.decode("utf-8"))
        except KeyboardInterrupt:
             print("closed")
             conn.close()
             s.close()
             sys.exit()
        except Exception as e:
             print(e)
             conn.close()
             s.close()
             sys.exit()


def server(address):
    """ initialize a socket server"""
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("sever intitialized, listening")
    except Exception as e:
        print(f"error: {e}")
        restart = input("\n Do you want to reInitialize the server y/n")
        server(address) if restart == 'y' else sys.exit() 
    conn, client_addr = s.accept()
    print(f"connection established : {client_addr}")
    send_commands(s, conn)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 19876
    server((host, port))
