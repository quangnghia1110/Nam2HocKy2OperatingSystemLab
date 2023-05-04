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

    # Nhận dữ liệu từ client
    a, b, c = [int(i) for i in client_socket.recv(1024).decode('utf-8').split('\n')]
    #a = int(client_socket.recv(1024).decode())
    #b = int(client_socket.recv(1024).decode())
    #c = int(client_socket.recv(1024).decode())

    #Tính toán nghiệm của phương trình
    delta = b**2-4*a*c
    if delta<0:
        res="Phương trình vô nghiệm"
    elif delta==0:
        x = -b / (2*a)
        res = "Phương trình có nghiệm kép x = " + str(x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        res = "Phuong trinh co hai nghiem phan biet x1 = " + str(x1) + " va x2 = " + str(x2)


    # Gửi kết quả về client
    client_socket.sendall(res.encode())

    # Đóng kết nối
    client_socket.close()
    #server_socket.close()