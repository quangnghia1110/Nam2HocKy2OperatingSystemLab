import socket

# Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

# Nhập 3 số a,b,c từ người dùng
a = input("Nhập số a: ")
b = input("Nhập số b: ")
c = input("Nhập số c: ")

# Gửi các số a, b, c đến server
client_socket.sendall(str.encode("\n".join([str(a), str(b), str(c)])))
#client_socket.sendall(str(a).encode())
#client_socket.sendall(str(b).encode())
#client_socket.sendall(str(c).encode())

# Nhận và hiển thị kết quả từ máy chủ
data = client_socket.recv(1024).decode()
print("Kết quả: " + data)

# Đóng kết nối
client_socket.close()