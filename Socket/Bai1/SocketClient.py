import socket

# Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000)) 

# Nhập số n từ người dùng
n = input("Nhập số n: ")
client_socket.sendall(n.encode())

# Nhận và hiển thị kết quả từ máy chủ
data = client_socket.recv(1024).decode()
print(f'Các ước số của {n} là: {data}')

# Đóng kết nối
client_socket.close()