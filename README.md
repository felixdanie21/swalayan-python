# Aplikasi Website Swalayan

Repository ini dibuat untuk mempercepat pembuatan aplikasi website swalayan.

## Rules

- Branch master tidak boleh diubah2, kerjanya menggunakan branch lain.
- Setiap pull atau push request akan di periksa Indra dulu.
- File2 yang boleh diubah adalah views, urls, templates dan juga file utilites.

## File settings.py

Untuk file settings.py tidak diupload karena menyesuaikan pengaturan komputer masing2 terutama konfigurasi databasenya. Code dari file settings.py dapat dilihat di file `settings.txt`

## Contoh Penulisan

```python
 # url,name url
 path('contoh_url', views.contoh_views, name='contoh_url'),
 
 # function views
 def blank(request):
     ......................
 
 # function template
 return render(request,'contoh-template.html')

 # context
 # digunakan untuk mengirim data ke template, adapun variable default:
 context = {
    'dbmenu': ambil_menu('a'), #  ambil_menu adalah fungsi, a adalah parameter yang berupa kode modul
    'parent_segment': 'kontroler_induk', # parent_segment diisi dengan kode induk menu (jika tidak ada "-")
    'segment': 'kontroler_menu',  # segment diisi dengan kode menu
 }
```

## Modul Developer

Modul developer digunakan saat tahap development saja, untuk mengakses gunakan  `/developer`

