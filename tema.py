import os
import random
import subprocess

# Fungsi untuk mendapatkan IP Address
def get_ip():
    ip = subprocess.getoutput("curl -s ifconfig.me")
    return ip

# Fungsi untuk mendapatkan info perangkat (HP, RAM)
def get_device_info():
    try:
        ram = subprocess.getoutput("free -h | grep Mem | awk '{print $2}'")
        device = subprocess.getoutput("getprop ro.product.model")
        return f"Device: {device}, RAM: {ram}"
    except:
        return "Device information not found."

# Fungsi untuk mendapatkan jumlah pengguna
def get_user_count():
    try:
        with open("/data/data/com.termux/files/home/.user_count", "r") as f:
            count = f.read()
        return count
    except:
        return "0"

# Fungsi untuk update jumlah pengguna
def update_user_count():
    try:
        with open("/data/data/com.termux/files/home/.user_count", "r") as f:
            count = int(f.read())
        count += 1
        with open("/data/data/com.termux/files/home/.user_count", "w") as f:
            f.write(str(count))
    except:
        with open("/data/data/com.termux/files/home/.user_count", "w") as f:
            f.write("1")

# Fungsi untuk menampilkan tampilan Pinguin
def show_penguin():
    penguin = """
    .--.  
   |o_o | 
   |:_/ | 
  //   \ \ 
 (|     | )
/'\_   _/`\\
\___)=(___/
    """
    return penguin

# Fungsi untuk menampilkan tampilan Hacker
def show_hacker():
    hacker = """
    ____  _      _     _      ____
   / ___|| |__  | |__ (_) ___| ___|
   \___ \| '_ \ | '_ \| |/ _ \___ \
    ___) | | | || | | | |  __/___) |
   |____/|_| |_|_| |_|_|\___|____/ 
   """
    return hacker

# Fungsi untuk menampilkan tampilan Cyber Security
def show_cyber_security():
    cyber_security = """
  ____ ____ ____ ____  ____  
 | __ | __ | __ | __ | | __| 
 | __ | __ | __ | __ | |__ | 
 |__ ||__ ||__ ||__ ||____| 
    """
    return cyber_security

# Fungsi utama untuk menampilkan tema acak
def display_theme():
    # Pilihan mode acak
    mode = random.choice([show_penguin, show_hacker, show_cyber_security])
    print(mode())

    # Menampilkan informasi pengguna
    print("\nUser Information:")
    print(f"User Count: {get_user_count()}")
    print(f"IP Address: {get_ip()}")
    print(f"Device Info: {get_device_info()}")

# Update jumlah pengguna
update_user_count()

# Jalankan tampilan
display_theme()
