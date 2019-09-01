# Django RESTful API Örneği

## İçindekiler

1. Giriş
2. Gereksinimler
3. Kurulum
4. Kaynak

## Giriş
<p>Django ile basit bir RESTful API geliştireceğiz.</p>

## Gereksinimler

<p>Django REST Framework’ü kullanarak uygulama yapmak istiyorsanız, bilgisayarınızda mutlaka python ve django paketlerinin kurulu olması gerekmektedir.</p>

### 1. Python

<p>Eğer UNIX tabanlı bir işletim sistemine sahipseniz, python 2.7 sürümü büyük ihtimalle sistemde yer almaktadır.</p>

<p>Eğer Windows işletim sistemine sahipseniz bu linkten uygun bir python sürümünü sisteminize kurmanız gerekmektedir.</p>

<p>Şu an ki en güncel sürüm 3.6.2, ben uygulamayı yaparken 3.4.3 sürümünü kullanacağım, farklı her hangi bir python sürümünü kurmanız uygulama aşamasındaki gidişatı etkilemeyecektir.</p>

### 2. Pip

<p>Python paketlerini kurmak ve yönetmek için kullandığımız bir araç. Eğer python 3 ve üzeri bir sürüm kurulu ise hazır bir şekilde pip3( python 3 ve üzeri için pip) gelmektedir.Python 2 kullanan kişiler bu aracı kullanırken komut satırına sadece pip yazmaları yeterlidir.</p>

<p>Sisteminizde pip kurulu değil ise <a href="https://pip.pypa.io/en/stable/installing/">bu linki</a> takip ederek kurulumu gerçekleştirebilirsiniz.</p>

### 3. Virtualenv

<p>Sistemde yer alan python dosyalarından bağımsız izole bir ortam oluşturarak istediğimiz eklentileri kurmamızı sağlayan araç. Pratikte kullanılmasını şiddetle tavsiye ediyorum. Bazı durumlarda birden fazla projede çalıştığınızda, farklı frameworklerin farklı versiyonlarında çalışmak durumunda kalabiliyorsunuz. İşte bu gibi durumlarda virtualenv ile oluşturduğunuz sanal ortamlar ile projelere özgü ayrı ortamlar oluşturabiliyorsunuz.</p>

<p>Pip kullanarak bu eklentiyi sistemimize aşağıdaki komut ile ekliyoruz.</p>

```
sudo pip install virtualenv
```

## Kurulum

### Virtualenv Oluşturma

<p>Bir çok kez üzerini vurguladığım üzere, projemizi işletim sistemimizde yer alan bağımsız sanal bir ortamda geliştireceğiz. Bunun için virtualenv aracı ile aşağıdaki adımları izleyerek sanal ortamımızı oluşturuyoruz.</p>

```
virtualenv –p python3 venv
```

- oluşturduğumuz ortamı aktif ediyoruz.

```
source venv/bin/activate
```

- requirements.txt dosyasını oluşturuyoruz. İçeriği şu şekilde olacak:
    
```
Django
djangorestframework
```
    
- requirements.txt içerisinde yer alan paketleri yükleme
    
```
pip install –r requirements.txt
```
    
### Yeni Bir Django Projesi Oluşturma 

<p>Django ile gerekli tüm paketleri başarılı bir şekilde yükledikten sonra artık yeni bir django projesi oluştururak, uygulamamızı yavaştan yapmaya başlayabiliriz. Oluşturduğumuz sanal ortamın aktif olduğunu ve projemizin bulunduğu klasörde olduğunuzu varsayaraktan, aşağıdaki komut ile bir django projesi oluşturuyoruz.</p>

```
django-admin startproject restuygulama .
```
<p>*Sonuna nokta koymamızın sebebi proje dosyalarımızın ek bir klasör yerine mevcut konumumuza oluşturmak istememiz.</p>

## Kaynak

    1. <a href="https://medium.com/@burakakyol07/django-ve-django-rest-framework-kullanarak-restful-api-oluşturmak-7f6e5c0a5783">Django ve Django Rest Framework Kullanarak RESTful API Oluşturmak-1</a>
    2. <a href="https://medium.com/@burakakyol07/django-ve-django-rest-framework-kullanarak-restful-api-oluşturmak-2-a3359a451661">Django ve Django Rest Framework Kullanarak RESTful API Oluşturmak-2</a>
