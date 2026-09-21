import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# ==========================================
# 1. KUMPULKAN BARANG BUKTI (EVIDENCE)
# ==========================================
# Didapat dari: /data/user/0/com.malware.ctf/shared_prefs/DiscordNitroModPrefs.xml
USER_INPUT = "B5HJ67H8"

# Didapat dari: Reverse Engineering libctf.so
SECRET_SALT = "PETIR{in1_buk4n_fl4gny4}"

# Didapat dari: /data/system/users/0/settings_secure.xml
ANDROID_ID = "103add7c1337aad1"

# ==========================================
# 2. REKONSTRUKSI KUNCI (KEY GENERATION)
# ==========================================
# Gabungkan sesuai logika C++ JNI
key_material = USER_INPUT + SECRET_SALT + ANDROID_ID

# Hash pakai MD5 sesuai logika Java untuk dapet 16-byte AES Key
md = hashlib.md5()
md.update(key_material.encode('utf-8'))
aes_key = md.digest()

# ==========================================
# 3. FUNGSI DEKRIPSI UTAMA
# ==========================================
def decrypt_petir(filepath):
    filename = os.path.basename(filepath)

    if not filename.endswith(".PETIR"):
        return

    # --- A. Kembalikan Nama File Asli (Base64 Decode) ---
    b64_name = filename.replace(".PETIR", "")
    # Fix padding "=" karena Python strict soal Base64 URL_SAFE
    b64_name += "=" * ((4 - len(b64_name) % 4) % 4)

    try:
        original_name = base64.urlsafe_b64decode(b64_name).decode('utf-8')
    except Exception as e:
        print(f"[-] Gagal decode nama {filename}: {e}")
        return

    # --- B. Baca File dan Buang Magic Header ---
    with open(filepath, 'rb') as f:
        file_content = f.read()

    # Cek apakah beneran ada header "PETIR" di awal file
    if not file_content.startswith(b"PETIR"):
        print(f"[-] Magic Header tidak valid pada file {filename}!")
        return

    # Ambil sisa byte setelah tulisan "PETIR" (5 byte)
    ciphertext = file_content[5:]

    # --- C. Dekripsi AES-CBC ---
    iv = b'\x00' * 16 # IV Kosong (16 byte 0) sesuai di Java
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    try:
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError:
        print(f"[-] Gagal dekripsi {original_name}. Kunci salah (Cek USER_INPUT) atau file korup!")
        return

    # --- D. Simpan Hasil Dekripsi ---
    output_path = os.path.join(os.path.dirname(filepath), original_name)
    with open(output_path, 'wb') as f:
        f.write(plaintext)

    print(f"[+] BOOM! Berhasil di-decrypt: {filename} -> {original_name}")

# ==========================================
# 4. EKSEKUSI SOLVER
# ==========================================
if __name__ == "__main__":
    # Taruh script ini di folder yang sama dengan file-file .PETIR
    target_dir = "."

    print("[*] Memulai Decryptor .PETIR...")
    for file in os.listdir(target_dir):
        if file.endswith(".PETIR"):
            decrypt_petir(os.path.join(target_dir, file))