# 🚁 Drone Filo Optimizasyonu: Çok Kısıtlı Ortamlarda Dinamik Teslimat Planlaması
## 📌 Proje Özeti
Bu proje, drone’lar ile yapılan teslimatlarda uçuş yasağı bölgeleri, enerji limitleri ve teslimat öncelikleri gibi dinamik kısıtlar altında optimum rota planlaması yapılmasını amaçlamaktadır. Geliştirilen sistem, gerçek zamanlı koşullarda çalışabilecek şekilde esnek, modüler ve uyarlanabilir bir algoritma yapısı sunar.

Projede hem klasik A* algoritması hem de Genetik Algoritma (GA) gibi sezgisel yöntemler kullanılarak rota optimizasyonu gerçekleştirilmiştir. Ayrıca, CSP (Constraint Satisfaction Problem) yaklaşımı ile dinamik kısıtlar yönetilmiştir.

## 🧠 Problem Tanımı
Bir lojistik firması, farklı ağırlık ve öncelik seviyelerine sahip paketleri çok sayıda drone ile hızlı ve verimli bir şekilde ulaştırmak istemektedir. Ancak rotalama sürecinde aşağıdaki zorluklar söz konusudur:

- Enerji (batarya) kısıtları
- Uçuşa yasak bölgeler (No-Fly Zones)
- Zaman aralıkları içinde teslimat gereksinimleri
- Dinamik çevresel koşullar ve teslimat öncelikleri

Bu proje, bu karmaşık kısıtları dikkate alarak en uygun rotaları belirleyen bir algoritma geliştirmeyi hedefler.

## 🛠️ Geliştirme Ortamı

| Bileşen              | Açıklama                                |
|----------------------|------------------------------------------|
| **Programlama Dili** | Python                                   |
| **IDE / Editör**     | VS Code, PyCharm                         |
| **Kullanılan Kütüphaneler** | matplotlib, numpy, heapq, datetime, random |
| **Görselleştirme**   | Matplotlib                               |
| **Sistem Uyumluluğu**| Windows 10/11, Linux                     |


## 📦 Veri Yapıları ve Kısıtlar
### 🛰️ Drone Özellikleri
- id: Drone'un benzersiz kimlik numarası (int)
- max_weight: Maksimum taşıma kapasitesi (float)
- battery: Batarya kapasitesi (int - mAh)
- speed: Hızı (float - m/s)
- start_pos: Başlangıç konumu (x, y)

### 🎯 Teslimat Noktaları
- id: Kimlik numarası
- pos: Konum (x, y)
- weight: Paket ağırlığı
- priority: Öncelik (1-5)
- time_window: Teslimat zamanı aralığı

### 🚫 No-Fly Zone'lar
- id: Bölge kimliği
- coordinates: Çokgen şeklindeki köşe noktaları
- active_time: Bölgenin aktif olduğu zaman aralığı

### 🧮 Algoritma Bileşenleri
- Düğümler: Teslimat noktaları
- Kenarlar: Drone hareketleri
- Ağırlıklandırma: Mesafe + taşıma maliyeti + öncelik cezası

### 🌟 A* Algoritması
- Tahmin fonksiyonu: Hedefe uzaklık + no-fly zone cezası
- Kapasite dışı rotalar filtrelenir.

### 🧩 CSP (Kısıt Tatmin Problemi)
- Bir drone aynı anda bir teslimat yapabilir.
- Drone’lar no-fly zone’ları ihlal edemez.

### 🧬 Genetik Algoritma (GA)
- Başlangıç: Rastgele geçerli rotalar
- Çaprazlama: Yeni rotalar üretimi
- Mutasyon: Nokta değiştirme
- Fitness: Tamamlanan teslimat - enerji - ihlal

### 🧪 Metrikler:
- Tamamlanan teslimat yüzdesi
- Ortalama enerji tüketimi
- Algoritma çalışma süresi (Hedef: < 1 dk)

### 📈 Görselleştirme
- Matplotlib ile rotalar çizilir.
- Harita üzerinde teslimatlar ve yasak bölgeler görsel olarak gösterilir.
![senaryo1_düzenli](https://github.com/user-attachments/assets/2d47b657-9cea-464c-abf6-76d668eb1fb6)

## ⚙️ Kurulum ve Çalıştırma
1. Depoyu Klonla
```bash
git clone https://github.com/BbSayar/drone-filo-optimizasyon.git
cd drone-filo-optimizasyon
```
2. Gerekli Kütüphaneleri Kur
```bash
pip install -r requirements.txt
pip install matplotlib numpy
```
3. Uygulamayı Başlat
```bash
python src/main.py
```

## 📁 Veri Seti
Tüm örnek drone, teslimat ve no-fly zone verileri data/sample_data.txt dosyasında yer almaktadır. İsterseniz bu veri üreticisini kullanarak farklı senaryolar oluşturabilirsiniz.

## 📞 İletişim
Projeyle ilgili soru, öneri veya katkı talepleriniz için bizimle iletişime geçebilirsiniz:

👨‍💻 Geliştiriciler: Barkın Emre Sayar, Hızır Ceylan, Erol Malkoç

📧 E-posta: barkinemresayar@gmail.com, ceylanhizir53@gmail.com, erolmalkoc04@gmail.com
