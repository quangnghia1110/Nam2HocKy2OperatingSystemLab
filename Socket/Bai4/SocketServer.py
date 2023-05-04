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

    data = client_socket.recv(1024)
    n = data.decode()

    res = len(n)
    rev = n[::-1]


    # Gửi kết quả về client
    #client_socket.sendall(res.encode())
    client_socket.sendall(str.encode("\n".join([str(res), str(rev)])))
    # Đóng kết nối
    client_socket.close()
    #server_socket.close()