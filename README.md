# Aplikasi Website Swalayan

Repository ini dibuat untuk mempercepat pengerjaan program

## Rules

- Branch master tidak boleh diubah2, kerjanya menggunakan branch lain.
- Setiap pull atau push request akan di periksa Indra dulu.
- File2 yang boleh diubah adalah views, urls, templates dan juga file utilites.

## Database

Konfigurasi database pada file settings disesuaikan database masing2.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbswalayan',
        'USER': 'root',
        'PASSWORD': 'paswmysql',
        'HOST': 'localhost',
        'PORT': '3307'
    }
}
```

## Contoh Penulisan

```python
 # url,name url
 path('contoh_url', views.contoh_views, name='contoh_url'),
 
 # function views
 def blank(request):
     ......................
 
 # function template
 return render(request,'contoh-template.html')
```

## Modul Developer

Modul developer digunakan saat tahap development saja, untuk mengakses gunakan  `/developer`

