import socket

# Khởi tạo socket và kết nối
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen()
print("Server is listening...")

while True:
    # Chấp nhận kết nối từ client
    server_socket, addr = server_socket.accept()
    print(f'Connected by {addr}')

    # Nhận dữ liệu từ client
    n = int(server_socket.recv(1024).decode())

    # Tìm các ước số của n
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    factors_str = ', '.join(str(x) for x in factors)

    # Gửi kết quả về client
    server_socket.sendall(factors_str.encode())

    # Đóng kết nối
    server_socket.close()