import socket

# Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

message = input("Nhan gi -> ")  # take input

while message.lower().strip() != 'thoat':
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal
    message = input("Nhan gi-> ")  # take input

# Đóng kết nối
client_socket.close()