# 🎵 Audio / Video Converter 

Bu proje, **Python** kullanılarak geliştirilmiş, **grafik arayüzlü (GUI)** bir **video → audio dönüştürme** uygulamasıdır.  
Kullanıcı dostu bir arayüz sayesinde video dosyası seçilebilir, çıktı yolu belirlenebilir ve dönüştürme işlemi **ilerleme çubuğu (progress bar)** ile takip edilebilir.

---

## 🚀 Özellikler

- 🎬 Video dosyası seçme
- 🎧 Videodan ses (audio) çıkarma
- 📁 Çıkış dosyası için kayıt yeri belirleme
- 📊 Progress bar ile dönüştürme durumu
- 🖥️ Basit ve anlaşılır GUI
- ⚙️ Arka planda FFmpeg kullanımı

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3**
- **Tkinter** (GUI)
- **FFmpeg** (medya dönüştürme)
- **subprocess**
- **threading**
- **PyInstaller** (EXE oluşturmak için)

---


⚠️ Bilinen Sorunlar

Uzun videolarda dönüştürme süresi uzayabilir

FFmpeg çıktısı GUI üzerinde detaylı gösterilmemektedir




## 📷 Uygulama Arayüzü

![Uygulama Arayüzü](screenshots/app.png)

> (İstersen buraya ekran görüntüsü ekleyebilirsin)

---

## 📦 Kurulum

### 1️⃣ Depoyu klonla
```bash
git clone https://github.com/kullanici_adin/audio-video-converter.git
cd audio-video-converter




FFmpeg, proje klasörü içinde bin/ffmpeg.exe olarak bulunmaktadır

Sisteme PATH eklenmesine gerek yoktur




çalıştırma

python main.py
