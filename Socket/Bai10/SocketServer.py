import socket
import math

# Khởi tạo socket và kết nối
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)
print("Server is listening...")

while True:
    # Chấp nhận kết nối từ client
    client_socket, address = server_socket.accept()
    print(f'Connected by {address}')
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = client_socket.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from client user: " + str(data))
        data = input(' -> ')
        client_socket.sendall(data.encode())  # send data to the client

    # Đóng kết nối
    client_socket.close()
    #server_socket.close()