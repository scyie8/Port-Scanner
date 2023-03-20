import socket

host = input("Hedef IP adresi: ")  # kullanıcıdan IP adresi alınır

for port in range(1, 65536):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((host, port))  # bağlantıyı dene
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()  # banner mesajını al
            except:
                banner = "Bilinmeyen servis"
            print(f"Port {port}:\tAçık\t\tServis: {socket.getservbyport(port)}\tVersiyon: {banner}")
    except:
        pass

#PenzPyhm && Scy-ie8
