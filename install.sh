#!/bin/bash

# Mengupdate Termux dan menginstal dependensi
pkg update && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip

# Meng-clone repo dan memasuki direktori
git clone https://github.com/bohana212/termux-theme.git
cd termux-theme

# Menginstal dependencies
pip install -r requirements.txt

# Menjalankan skrip tema
python theme.py
