import socket

# Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

filename = input("Enter Filename: ")
f = open(filename, 'r')
content = f.read()
f.close()
client_socket.send(content.encode())

print("File has been sent successfully")

# receive the result from the receiver
result = client_socket.recv(1024).decode()
print(result)

# Đóng kết nối
client_socket.close()