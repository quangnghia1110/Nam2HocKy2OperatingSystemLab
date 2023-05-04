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
    chuoi = conn.recv(1024).decode()
    arr = chuoi.split("\n")
    s1 = arr[0]
    s2 = arr[1]
    content = ""
    for i in arr[2:]:
        content += i + "\n"

    # receive the file data
    try:
        save_filename = "serverreplace.txt"
        s = open(save_filename, 'w')
        content = content.replace(s1, s2)
        s.write(content)
        #Gui du lieu trong file toi client
        conn.sendall("Da sua xong".encode())
        s.close()
        print("File has been received successfully")
    #Khong tim thay file
    except FileExistsError:
        conn.send("Khong tim thay file")
    # Đóng kết nối
    conn.close()