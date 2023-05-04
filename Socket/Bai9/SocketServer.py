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

    #data = client_socket.recv(1024)
    #n = data.decode()
    chuoi, yc = [i for i in client_socket.recv(1024).decode('utf-8').split('\n')]
    if 'INSERT' in yc:
        lst = yc.split()
        ycbt = lst[0]
        insert = lst[1:]
        insert = " ".join(insert)
    if 'DELETE' in yc:
        lst = yc.split()
        ycbt = lst[0]
        a = int(lst[1])
        b = int(lst[2])
    #Tính toán nghiệm của phương trình
    if yc == "UPPER":
        chuoi = chuoi.upper()
    elif yc == "LOWER":
        chuoi = chuoi.lower()
    elif ycbt == "INSERT":
        chuoi += insert
    elif ycbt == "DELETE":
        temp = chuoi[:a-1]
        temp += chuoi[b:]
        chuoi = temp

    # Gửi kết quả về client
    client_socket.sendall(chuoi.encode())

    # Đóng kết nối
    client_socket.close()
    #server_socket.close()