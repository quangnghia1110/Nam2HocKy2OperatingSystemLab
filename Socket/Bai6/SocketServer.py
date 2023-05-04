import socket
import math

def IsPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

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
    n = int(n)
    #Tính toán nghiệm của phương trình
    lst = []
    for i in range(1, n+1):
        if IsPrime(i):
            lst.append(str(i))
            print(i, end = " ")
    str_list = " ".join(lst)
    str_list = str(str_list)
    # Gửi kết quả về client
    client_socket.sendall(str_list.encode())

    # Đóng kết nối
    client_socket.close()
    #server_socket.close()