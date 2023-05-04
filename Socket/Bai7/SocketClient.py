import socket
import pickle
import numpy as np

def ToArray(shape: str, arr: str):
    r, c = [int(i) for i in shape.split(" ")]
    #chuoi = np.shape((r, c))
    arr = arr.replace("[", "")
    arr = arr.replace("]", "")
    arr = " ".join(arr.split())
    arr = [int(i) for i in arr.split(" ")]
    chuoi = np.array(arr).reshape((r, c))
    return chuoi

# # Khởi tạo socket và kết nối đến máy chủ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

# # create two 3x3 matrices
matrix_a = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.int32)
matrix_b = np.array([[9,8,7],[6,5,4],[3,2,1]], dtype=np.int32)

# # send the matrix data to the server
shape_1 = str(f'{matrix_a.shape[0]} {matrix_a.shape[1]}')
arr_1 = str(matrix_a).replace("\n", " ")
shape_2 = str(f'{matrix_b.shape[0]} {matrix_b.shape[1]}')
arr_2 = str(matrix_b).replace("\n", " ")
# # receive the product matrix from the server

client_socket.sendall(str.encode("\n".join([shape_1, arr_1, shape_2, arr_2])))

data = client_socket.recv(1024)
re_shape, re = data.decode().split("\n")
result = ToArray(re_shape, re)

print(result)
# # Đóng kết nối
client_socket.close()

