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
    lst = n.split(" ")
    int_lst = [int(x) for x in lst]
    #Tính toán nghiệm của phương trình
    int_lst.sort()
    str_lst = [str(x) for x in int_lst]
    str_list = " ".join(str_lst)
    str_list = str(str_list)
    # Gửi kết quả về client
    client_socket.sendall(str_list.encode())

    # Đóng kết nối
    client_socket.close()
    #server_socket.close()