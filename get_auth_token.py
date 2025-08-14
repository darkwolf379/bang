#!/usr/bin/env python3
"""
Helper script untuk mendapatkan auth_token dari browser
"""

import webbrowser
import time

def show_instructions():
    """Tampilkan instruksi cara mendapatkan auth_token"""
    print("🔐 Cara Mendapatkan Auth Token dari Twitter")
    print("=" * 50)
    print()
    
    print("📋 Langkah-langkah:")
    print("1. Buka browser (Chrome/Firefox/Edge)")
    print("2. Kunjungi https://twitter.com")
    print("3. Login ke akun Twitter Anda")
    print("4. Tekan F12 untuk membuka Developer Tools")
    print("5. Pilih tab 'Application' (Chrome) atau 'Storage' (Firefox)")
    print("6. Di sidebar kiri, expand 'Cookies' > 'https://twitter.com'")
    print("7. Cari cookie dengan nama 'auth_token'")
    print("8. Copy value dari auth_token tersebut")
    print("9. Paste ke file config.py")
    print()
    
    print("🎯 Tips:")
    print("- Pastikan Anda sudah login ke Twitter")
    print("- Auth token akan expired setelah beberapa waktu")
    print("- Jangan share auth token dengan siapapun")
    print("- Backup auth token di tempat yang aman")
    print()
    
    choice = input("🚀 Buka Twitter.com sekarang? (y/n): ").lower()
    
    if choice == 'y':
        print("🌐 Membuka Twitter.com...")
        webbrowser.open("https://twitter.com")
        print("✅ Twitter.com dibuka di browser!")
        print()
        print("📝 Setelah login, ikuti langkah-langkah di atas untuk mendapatkan auth_token")
    else:
        print("👌 Baik, Anda bisa membuka Twitter.com secara manual")
    
    print()
    print("💡 Setelah mendapatkan auth_token:")
    print("1. Edit file config.py")
    print("2. Ganti 'YOUR_AUTH_TOKEN_HERE' dengan auth_token Anda")
    print("3. Jalankan: python example_usage.py")

def main():
    """Main function"""
    print("🐦 Twitter Auto Script - Auth Token Helper")
    print()
    
    show_instructions()
    
    print()
    print("📞 Butuh bantuan? Cek README.md untuk informasi lengkap")

if __name__ == "__main__":
    main()