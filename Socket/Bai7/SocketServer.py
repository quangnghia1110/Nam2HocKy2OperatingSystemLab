import socket
import pickle
import numpy as np
import math

def ToArray(shape: str, arr: str):
    r, c = [int(i) for i in shape.split(" ")]
    #chuoi = np.shape((r, c))
    arr = arr.replace("[", "")
    arr = arr.replace("]", "")
    arr = " ".join(arr.split())
    arr = [int(i) for i in arr.split(" ")]
    chuoi = np.array(arr).reshape((r, c))
    return chuoi



# # Khởi tạo socket và kết nối
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)
print("Server is listening...")

while True:
    # Chấp nhận kết nối từ client
    conn, addr = server_socket.accept()
    print(f'Connected by {addr}')

#     # Nhận dữ liệu từ client
    s1, arr_1, s2, arr_2 = conn.recv(1024).decode('utf-8').split('\n')
    a = ToArray(s1, arr_1)
    b = ToArray(s2, arr_2)
    c = np.array(np.dot(a, b))
    
    shape_1 = str(f'{c.shape[0]} {c.shape[1]}')
    arr = str(c).replace("\n", " ")

    conn.sendall(str.encode("\n".join([shape_1, arr])))
#     # Đóng kết nối
    conn.close()
