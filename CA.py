import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(1)
    print("Server started! Waiting for connection...")
    
    client_socket, addr = server.accept()
    print(f"Connected with {addr}")
    
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.daemon = True
    thread.start()
    
    while True:
        message = input()
        if message.lower() == 'quit':
            break
        client_socket.send(f"Server: {message}".encode('utf-8'))
    
    client_socket.close()
    server.close()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))
    print("Connected to server!")
    
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()
    
    while True:
        message = input()
        if message.lower() == 'quit':
            break
        client.send(f"Client: {message}".encode('utf-8'))
    
    client.close()

def main():
    print("===== Chat Application =====")
    choice = input("Start as (server/client): ").lower()
    
    if choice == 'server':
        start_server()
    elif choice == 'client':
        start_client()
    else:
        print("Invalid choice!")

main()