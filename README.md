🛣️ LOCAL AI ASİSTAN YOL HARİTASI

1.SAĞLIK SEKMESİ

AŞAMA 1: Tamamlananlar (Temel Atma)
✅ Modern ve esnek arayüz tasarımı (Dashboard).
✅ Llama 3 API köprüsü (Flask backend).
✅ Sohbet kutusunun yapay zeka ile konuşturulması.
✅ Beslenme kutusunun AI destekli makro (JSON) hesaplaması.

AŞAMA 2: Dinamik Veri Entegrasyonu (Şu an buradayız)
Sorun: Ekranda gördüğün "VKİ 20.0, 180g Karbonhidrat, Day 20 PMS" gibi yazılar HTML içine bizim yazdığımız sahte (hardcoded) metinler.
Ne Yapılacak?

    Dinamik UI Rendering: Sayfa açıldığında bu veriler HTML'den değil, oluşturduğumuz o database.json dosyasından okunup ekrana basılacak.

    Kişisel Bilgi Güncelleme: Sol üstteki "Kişisel Bilgiler" kutusundaki Yaş, Boy, Kilo değerlerini modal üzerinden girilebilir ve kaydedilebilir hale getireceğiz. (Sen Boy/Kilo girdiğinde, AI bunu okuyup VKİ'ni hesaplayacak).

    Makro Hedeflerini Belirleme: Senin kilona ve hedefine göre Günlük alman gereken Protein/Karb/Yağ sınırlarını (örn: /150g, /200g hedeflerini) AI belirleyecek ve arayüzdeki barlar buna göre dolacak.

AŞAMA 3: Sağ Panel (Antrenman ve Analiz) Mantığı
Sorun: Sağdaki "Bugünün Planı" ve "Uyarılar" kutusu sabit. Menisküsün olmasa bile orada "Menisküs uyarısı" yazıyor.
Ne Yapılacak?

    Dinamik Antrenman Uyarıları: Sağ üstteki sarı "Dr. AI Alerts" kutusu her gün güncellenecek. AI, senin o günkü Döngü (Cycle) fazına ve hastalıklarına bakıp sana özel 2 maddelik uyarı metni oluşturacak.

    Akıllı Görev Listesi (Checklist): Antrenman programını AI belirleyecek. DOMS yazdıysan bacak hareketlerini sistem otomatik kilitleyecek (disabled yapacak). Yapılan checkbox'ların durumu kaydedilecek.

    Haftalık Durum Bildir: O mor butona bastığında AI sana bir modal açıp "Şınav sayın arttı mı?" diyecek. Aldığı cevapları puanlayıp o alttaki mükemmel çizgi/sütun grafiklerini matematiksel olarak güncelleyecek.

AŞAMA 4: Döngü ve Uyku (Zaman Mekanizmaları)
Sorun: Döngü 20. günde sabit duruyor.
Ne Yapılacak?

    Tarih Motoru: Bilgisayarın tarihine bağlanacağız. Sen döngünün 1. gününü gireceksin, sistem her gün o dairesel grafiği otomatik döndürecek ve 28 günlük döngüde nerede olduğunu hesaplayacak.