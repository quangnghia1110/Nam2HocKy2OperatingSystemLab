import socket

# Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

n = input("Nhap chuoi: ")
yc = input("Nhap yeu cau: ").upper()
client_socket.sendall(str.encode("\n".join([str(n), str(yc)])))

# Nhận và hiển thị kết quả từ máy chủ
data = client_socket.recv(1024)
data = data.decode()
print("Chuoi sau khi duoc xu ly: " + data)

# Đóng kết nối
client_socket.close()