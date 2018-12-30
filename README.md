# Egitim-Projesi

Dersler parçalar halinde branchlerde bulunuyor olacaktır.

Aşağıda virtual environment denemek isteyenler için kurulum aşaması yer alacaktır. Kullanım tamamen isteğe bağlıdır.
Virtual environment hakkında detaylı bilgi: https://yazilimportal.com/python-virtual-environment-8d50f5bae0d7

## Hadi Başlayalım!

### 1.1 Repository klonlamak
```
git clone https://github.com/TycheLearningCommunity/Egitim-Projesi.git
```

### 1.2 Branch değiştirmek
Aşağıdaki kod satırıyla tüm branch isimlerini görebiliriz.
```
cd Egitim-Projesi
```
```
git branch -a
```
Diğer bir kod satırıyla da istediğimiz branche geçmiş olacağız.
```
git checkout Ders-1
```

### 1.3 Virtual Environment aktive etmek
```
cd Ders-1
```
```
. Scripts/activate
```

### 1.4 İnaktif hale getirmek
```
deactivate
```

### 2. Gerekli kütüphanelerin kurulumu
```
pip3 install -r requirements.txt
```
