from scapy.all import rdpcap, Raw
from PIL import Image

def solve_pcap(pcap_filename, output_image):
    print(f"[*] Membaca file {pcap_filename}...")
    packets = rdpcap(pcap_filename)
    
    # 1. Parsing Metadata dari Paket Pertama
    meta_data = packets[0][Raw].load.decode('utf-8', errors='ignore')
    parts = meta_data.split('|')
    width = int(parts[1].split('=')[1])
    height = int(parts[2].split('=')[1])
    print(f"[*] Metadata ditemukan: Resolusi {width}x{height}")
    
    # Siapkan kanvas kosong
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    
    # 2. Menyusun ulang raw bytes menjadi piksel
    print("[*] Merangkai ulang piksel...")
    row_idx = 0
    # Skip paket pertama (index 0) karena itu metadata
    for pkt in packets[1:]: 
        if Raw in pkt:
            raw_bytes = pkt[Raw].load
            
            # Format: R, G, B berurutan
            for x in range(width):
                r = raw_bytes[x * 3]
                g = raw_bytes[(x * 3) + 1]
                b = raw_bytes[(x * 3) + 2]
                pixels[x, row_idx] = (r, g, b)
                
            row_idx += 1
            # Berhenti jika tinggi gambar sudah tercapai
            if row_idx >= height: 
                break
                
    img.save(output_image)
    print(f"[+] Selesai! Flag berhasil direkonstruksi ke {output_image}")
    img.show()

if __name__ == "__main__":
    solve_pcap("displayport_dump.pcap", "flag_solved.png")
