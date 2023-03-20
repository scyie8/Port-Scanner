import asyncio
import nmap

# Hedef IP adresi
target_ip = input("Hedef IP adresi: ")

# Tüm portları tarayacak şekilde aralığı belirleyin
start_port = 1
end_port = 65535

# Nmap taraması yapmak için nmap modülünü kullanın
nm = nmap.PortScanner()

# Asenkron fonksiyon oluşturun
async def scan_port(port):
    # Belirtilen portu tara
    result = nm.scan(target_ip, str(port), arguments='-sV')['scan']
    # Tarama sonucundan hizmet ve versiyon bilgilerini alın
    try:
        service = result[target_ip]['tcp'][port]['name']
        version = result[target_ip]['tcp'][port]['version']
    except:
        service = "Bilinmiyor"
        version = "Bilinmiyor"
    # Bilgileri ekrana yazdır
    print("Port {}: {} ({})".format(port, service, version))

async def main():
    tasks = []
    # Tüm portları tarayın
    for port in range(start_port, end_port+1):
        tasks.append(asyncio.ensure_future(scan_port(port)))
    # Tüm görevleri asenkron olarak çalıştırın
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
