# Twitter Auto Script

Script otomatis untuk Twitter menggunakan API v1 dengan autentikasi cookie. Fitur: Auto Like, Tweet, Reply, dan Retweet.

## 🚀 Fitur

- ✅ **Auto Like** - Otomatis like tweet berdasarkan keyword
- ✅ **Auto Tweet** - Post tweet otomatis
- ✅ **Auto Reply** - Reply otomatis ke tweet berdasarkan keyword
- ✅ **Auto Retweet** - Retweet otomatis berdasarkan keyword
- ✅ **Search Tweets** - Cari tweet dengan keyword tertentu
- ✅ **User Timeline** - Ambil timeline user
- ✅ **Cookie Authentication** - Menggunakan auth_token dari browser
- ✅ **Safety Features** - Delay random dan rate limiting
- ✅ **Logging** - Log semua aktivitas ke file

## 📋 Persyaratan

- Python 3.7+
- Akun Twitter aktif
- auth_token dari browser

## 🛠️ Instalasi

1. **Clone atau download script ini**
```bash
git clone <repository-url>
cd twitter-auto-script
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Dapatkan auth_token dari browser**
   - Buka Twitter.com dan login
   - Tekan F12 untuk buka Developer Tools
   - Pergi ke tab **Application** (Chrome) atau **Storage** (Firefox)
   - Di sidebar kiri, expand **Cookies** > **https://twitter.com**
   - Cari cookie dengan nama **auth_token**
   - Copy value dari auth_token tersebut

4. **Edit file config.py**
```python
AUTH_TOKEN = "PASTE_AUTH_TOKEN_DISINI"
```

## 📖 Cara Penggunaan

### 1. Basic Usage

```python
from twitter_auto import TwitterAuto

# Initialize
twitter = TwitterAuto("YOUR_AUTH_TOKEN")

# Post tweet
twitter.post_tweet("Hello Twitter! 🤖")

# Like tweet
twitter.like_tweet("1234567890123456789")

# Retweet
twitter.retweet("1234567890123456789")

# Reply to tweet
twitter.reply_to_tweet("1234567890123456789", "Great post! 👍")
```

### 2. Auto Like berdasarkan Keyword

```python
# Auto like 10 tweet dengan keyword "python"
keywords = ["python", "programming", "coding"]
twitter.auto_like_by_keyword(
    keywords=keywords,
    count=10,
    delay_range=(30, 60)  # Delay 30-60 detik
)
```

### 3. Auto Retweet berdasarkan Keyword

```python
# Auto retweet 5 tweet dengan keyword "python"
keywords = ["python", "programming"]
twitter.auto_retweet_by_keyword(
    keywords=keywords,
    count=5,
    delay_range=(60, 120)  # Delay 60-120 detik
)
```

### 4. Auto Reply berdasarkan Keyword

```python
# Auto reply ke tweet dengan keyword "python"
keywords = ["python", "programming"]
replies = [
    "Great post! 👍",
    "Thanks for sharing! 🙏",
    "Interesting perspective! 🤔"
]

twitter.auto_reply_by_keyword(
    keywords=keywords,
    replies=replies,
    count=3,
    delay_range=(120, 180)  # Delay 120-180 detik
)
```

### 5. Search Tweets

```python
# Cari tweet dengan keyword
tweets = twitter.search_tweets("python programming", count=20)
for tweet in tweets:
    print(f"@{tweet['user']['screen_name']}: {tweet['text']}")
```

## 🎯 Contoh Script Lengkap

Jalankan `example_usage.py` untuk melihat contoh lengkap:

```bash
python example_usage.py
```

## ⚙️ Konfigurasi

Edit file `config.py` untuk mengatur:

- **Keywords** untuk auto like/retweet/reply
- **Delay** antara aksi
- **Jumlah** tweet yang diproses
- **Pesan reply** yang akan digunakan
- **Safety settings** untuk menghindari rate limiting

## 🔒 Safety Features

Script ini sudah dilengkapi dengan fitur keamanan:

- **Random Delay** - Delay acak antara aksi untuk menghindari deteksi bot
- **Rate Limiting** - Maksimal aksi per jam
- **Error Handling** - Handle error dengan graceful
- **Logging** - Log semua aktivitas untuk monitoring

## ⚠️ Peringatan Penting

1. **Gunakan dengan bijak** - Jangan spam atau abuse
2. **Respect rate limits** - Jangan terlalu banyak aksi dalam waktu singkat
3. **Follow Twitter ToS** - Pastikan tidak melanggar Terms of Service
4. **Monitor logs** - Cek file `twitter_auto.log` untuk monitoring
5. **Backup auth_token** - Simpan auth_token dengan aman

## 📝 Logging

Script akan membuat log file `twitter_auto.log` dengan format:

```
2024-01-01 10:00:00 - INFO - Twitter Auto initialized successfully!
2024-01-01 10:00:05 - INFO - Tweet 1234567890123456789 liked successfully
2024-01-01 10:00:10 - INFO - Waiting 45.2 seconds
```

## 🐛 Troubleshooting

### Error: "Failed to get guest token"
- Pastikan auth_token valid dan belum expired
- Coba refresh auth_token dari browser

### Error: "Request failed: 401"
- Auth_token sudah expired atau invalid
- Dapatkan auth_token baru dari browser

### Error: "Rate limit exceeded"
- Kurangi jumlah aksi atau tambah delay
- Tunggu beberapa jam sebelum mencoba lagi

### Script tidak berjalan
- Pastikan Python 3.7+ terinstall
- Install dependencies: `pip install -r requirements.txt`
- Cek auth_token sudah benar di `config.py`

## 📁 Struktur File

```
twitter-auto-script/
├── twitter_auto.py      # Main script
├── config.py           # Konfigurasi
├── example_usage.py    # Contoh penggunaan
├── requirements.txt    # Dependencies
├── README.md          # Dokumentasi
└── twitter_auto.log   # Log file (auto generated)
```

## 🤝 Kontribusi

Silakan fork dan submit pull request untuk improvement.

## 📄 License

Script ini dibuat untuk tujuan edukasi. Gunakan dengan tanggung jawab.

## ⚡ Tips Penggunaan

1. **Mulai dengan jumlah kecil** - Test dengan 2-3 tweet dulu
2. **Gunakan delay yang cukup** - Minimal 30 detik antara aksi
3. **Monitor aktivitas** - Cek log file secara berkala
4. **Backup auth_token** - Simpan di tempat yang aman
5. **Update secara berkala** - Twitter API bisa berubah

---

**Happy Tweeting! 🐦✨**