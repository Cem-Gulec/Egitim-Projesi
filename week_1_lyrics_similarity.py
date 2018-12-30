# # Tyche LC Eğitim Projesi

# Bu eğitim süresince internetten veri çekerek başlayıp şarkılar arası benzerliği şarkı sözlerine göre belirleyen bir tavsiye sisteminin oluşturulması hedeflenmektedir.

# Ders - 1 | 11.12.2018

# Bu derste selenium ve beautifulsoup kütüphaneleri kullanılarak "https://www.sarkisozleri.bbs.tr" adresinden şarkı sözleri çekilmiştir.

# BeautifulSoup kütüphanesini web sitesinin ağaç yapısı içerisinde gezinmek ve istediğimiz element veya elementlere ulaşmak için kullanıyoruz. 
# 
# Detaylı bilgi için: 
#     https://medium.com/python/python-beautifulsoup-mod%C3%BCl%C3%BC-77030b4846a4


from bs4 import BeautifulSoup as bs 


# Selenium kütüphanesini web sitesinde kod üzerinden işlem yaparak veri çekmek için kullanıyoruz. BeautifulSoup veriyi çektinten sonra kullanıyoruz. 
# 
# Detaylı bilgi için:
#     https://selenium-python.readthedocs.io/
#     https://medium.com/python/python-selenium-mod%C3%BCl%C3%BC-kullan%C4%B1m%C4%B1-ders-1-36983185164c


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import webelement


# Burada selenium'un sayfasından indirdiğimiz tarayıcı sürücüsünü (browser driver) çalıştırıyoruz.


driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")


# Burada ise javascript veya ajax ile sonradan gelen veriler için sayfanın beklemesini istediğimizi söylüyoruz.


driver.implicitly_wait(30) 


# Bu döngüde sayfada bulunan şarkı sözlerinin linklerini çekiyoruz. 


for i in range(1, 367):
    # şarkı sözü sayfaları url kısmında sayısal olarak arttığı için -i- değerini her arttırdığımızda
    # yeni bir sayfaya geçmiş oluyoruz.
    url = "https://www.sarkisozleri.bbs.tr/" + str(i)
    # çalıştırdığımız tarayıcı sürücsünün (browser driver) istediğimiz url'e getirmesini söylüyoruz.
    driver.get(url)
    # sayfa açıldıktan sonra sayfa kaynağını yani ham veriyi beautifulsoup kütüphanesine vererek
    # ağaç yapısı başka bir tabirle soup nesnesi olarak alıyoruz.
    soup = bs(driver.page_source, "lxml")
    # sayfada bulunan linkleri taşıyıcı -div- etiketlerini çekiyoruz.
    divs = soup.select("div.row div")
    # burada döngü kullanarak her bir div'den linki alıp dosyaya yazıyoruz.
    for div in divs:
        try:
            with open("urls.txt", "a+", encoding="utf-8") as f:
                f.write("https://www.sarkisozleri.bbs.tr" + div.select("div div a")[0].attrs["href"] + "\n")
        except Exception as e:
            continue


# Yukarıdaki kod uzun sürüyor ve diğer aşama yukarıdaki kod bitmeden çalışmaması gerekiyor. Bu yöntemi biz belirliyoruz, istersek her bir linki aldıktan sonra o linkteki şarkı sözüne gidip yazabilirdik. Ancak biz şarkı sözlerine ait tüm linkleri aldıktan sonra o linkleri kullanarak şarkı sözlerini sonradan toplamayı tercih ettik.

# -------------------------------------------------------------------------------------------------------------------------

# Burada dosyaya yazdığımız url'leri okuyoruz.

with open("urls.txt", "r", encoding="utf-8") as f:
    urls = [url.replace("\n", " ") for url in f.readlines()]


# Burada her bir linkin sayfasına gidip oradaki şarkı sözünü ve şarkı hakkındaki betimleyici bilgiyi alarak json formatında dosyaya yazdırıyoruz. JSON hakkında: http://www.ugurkizmaz.com/YazilimMakale-1878-JSON--JavaScript-Object-Notation--Nedir--Nasil-ve-Nerede-Kullanilir-.aspx


# bu kısım json formatını koruyabilmek için gerekli.
# önce dosyayı açıyoruz, sonra köşeli parantez açıyoruz
# her bir şarkıyı kaydettikten sonra virgül koyuyoruz,
# en sonda ise sondaki virgülü silip, köşeli parantezi 
# kapatıyoruz. Bu sayede json formatını korumuş oluyoruz.
with open("lyrics.json", "w+", encoding="utf-8") as f:
    f.write("[\n")
# her bir şarkı sözü linki için olan for döngüsü
for url in urls:
    # sürücüye şarkı linkini getiriyoruz
    driver.get(url)
    # sayfa kaynağını beautifulsoup kütüphanesine veriyoruz
    soup = bs(driver.page_source, "lxml")
    # soup değişkenin kullanarak, şarkı sözünü metin şeklinde alıyoruz
    text = soup.select("#sarki-sozleri div.col-md-6")[0].getText().strip().replace("\n", " ")
    # sanatçı ve şarkı ismini alıyoruz
    info = soup.select("div.page-header h1")[0].getText().replace("\n", " ").strip()
    # json haline çeviyoruz
    json_lyric = {"info": info, "text": text}
    # dosyaya yazıyoruz
    with open("lyrics.json", "a+", encoding="utf-8") as f:
        f.write(json.dumps(json_lyric) + ",\n")
# bütün işlem bittikten sonra, dosyayı sondaki virgül olmadan
# okuyoruz. Sonra köşeli parantez ekleyerek tekrar yazıyoruz.
with open("lyrics.json", "r", encoding="utf-8") as f:
    tmp = f.read()[:-1]
with open("lyrcis.json", "w+", encoding="utf-8") as f:
    f.write(tmp + "]")