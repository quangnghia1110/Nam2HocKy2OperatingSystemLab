import socket

# Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

filename = input("Enter Filename: ")
f = open(filename, 'r')
content = f.read()
f.close()
s1 = input("Nhap chuoi tim: ")
s2 = input("Nhap chuoi thay the: ")
client_socket.sendall(str.encode("\n".join([str(s1), str(s2), str(content)])))
print("File has been sent successfully")

# receive the result from the receiver
result = client_socket.recv(1024).decode()
print(result)

# Đóng kết nối
client_socket.close()