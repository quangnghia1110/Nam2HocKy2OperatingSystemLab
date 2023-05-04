import socket

# Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

n = input("Nhap mot so nguyen: ")

client_socket.sendall(n.encode())

# Nhận và hiển thị kết quả từ máy chủ
data = client_socket.recv(1024)
data = data.decode()
print("Cac so nguyen to <= n: " + data)

# Đóng kết nối
client_socket.close()