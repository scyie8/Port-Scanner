import socket
import multiprocessing.pool

# Hedef IP adresi ve taramak istediğimiz port aralığı
target_ip = input("Hedef IP adresi: ")
start_port = 1
end_port = 65535

# Tarama fonksiyonu
def scan_port(ip, port):
    try:
        # Soket oluşturma
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bağlantıyı zaman aşımına uğrat
        s.settimeout(0.5)
        # Portu tara
        result = s.connect_ex((ip, port))
        if result == 0:
            # Hizmet adını ve versiyon bilgisini alma
            service = socket.getservbyport(port)
            banner = ""
            s.send(b"GET / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024)
            print("Port {} açık: Hizmet={}, Versiyon={}".format(port, service, banner.decode().strip()))
        # Soketi kapat
        s.close()
    except:
        pass

# Tüm portları tara
pool = multiprocessing.pool.ThreadPool(processes=500)
for port in range(start_port, end_port+1):
    pool.apply_async(scan_port, args=(target_ip, port))
pool.close()
pool.join()
