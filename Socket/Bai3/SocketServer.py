import socket

# Khởi tạo socket và kết nối
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5000))
sock.listen(1)
print("Server is listening...")

while True:
    # Chấp nhận kết nối từ client
    conn, addr = sock.accept()
    print(f'Connected by {addr}')

    # receive the file name
    content = conn.recv(1024).decode()

    # receive the file data
    try:
        save_filename = "serverrecieved"
        s = open(save_filename, 'w')
        s.write(content)
        #Gui du lieu trong file toi client
        conn.sendall(content.encode())
        s.close()
        print("File has been received successfully")
    #Khong tim thay file
    except FileExistsError:
        conn.send("Khong luu duoc file")
    # Đóng kết nối
    conn.close()