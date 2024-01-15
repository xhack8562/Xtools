======================================================================================================================================
# Gunakan python 3
List module yang diperlukan :
pip install requests
pip install colorama
pip install bs4
pip install paramiko
pip install mysql-connector 
======================================================================================================================================
# Penjelasan Tools Utama ?
[+] 1. Scan Config & Ftp = untuk melakukan scanning pada list domain yang anda, terdapat dua output yaitu :
	configfound.txt berisi website yang memiliki kerentan information diosclousure database (wp/laravel atau native)
	sftpfoung.txt berisi kerentan information diosclousure ftp/sftp/ssh akses.

	untuk path silakan masukan path config.txt yang berapada di folder path "path/config.txt" anda bisa costum pathnya
	sendiri

[+] 2. Split Ftp = untuk mengambil data username,password dan host ftp dari hasil  scanning diatas dan untuk dijalankan di no 3

[+] 3. Cek Ftp = tools ini untuk melakukan pengecekan ftp/ssh/sftp valid, data diambil dari hasil split no 2, ketika dijalankan
	 silakan masukan "output/listforftp.txt" hasil data yang valid akan di simpan di /ouput/ dengan nama file ftpOk.txt

[+] 4. Clean Domain = tools ini untuk melakukan cleaning path domain, contoh domain.com/path/.env maka akan menjadi domain.com
	jika domain sudah clean maka anda bisa menggunakan sql checker di no 5

[+] 5. Sql Checker = untuk melakan scanning phpmyadmin ataupun adminer baik path ataupun subdomain, data diambil dari hasil
	clean domain (selanjutnya anda lakukan manual login dengan membuka phpmyadmin/adminer dan ambil pass/user dari configfound.txt)
	hasil dari sql cehcker berupa file sqlpath.txt

[+] 6. ExtractorDB = tools ini digunakan untuk mengambil data db,user,pass,host dari hasil no 1 yaitu configfound.txt hasilnya di
	simpan dengan nama listforremote.txt di folder output untuk selanjutnya di cek koneksi sql remotenya nanti di no 8

[+] 7. Change Host To IP = sama dengan diatas, namun bedanya disini semua host akan di ubah menjadi ip (karena terkadang ada
	host "localhot" maka akan diubah menjadi ip data yang di proses diambil dari no 6 yaitu "listforremote.txt" hasilnya 
	listforremoteip.txt

[+] 8. RemoteSql Checker = nah sekarang setelah no 6 dan 7 dilakukan maka anda jalankan no 8 ini untuk melekukan pengecekan apakah
	database bisa di remote atau tidak, hasil yang bisa di remote di simpan di output dengan nama remotesqlok.txt

[+] 9. ExtracDB For CpCrack = tool ini untuk mengambil data user|pass dari no 6 ExtractorDB, masukan output/listforremote.txt 
	ketika anda jalankan, hasilnya akan di simpan di folder output dengan nama dbforcp.txt untuk selanjutnya di jalankan di cpcrack

[+] 10. Cpcrack From DB = tools ini untuk mencoba user|pass cpanel menggunakan data database, masukan data dari hasil no 9 yaitu 
	dbforcp.txt yang ada pada folder output >> "output/dbforcp.txt" hasil cpanel yang valid di simpan dengan nama CpanelFound.txt
======================================================================================================================================
# Penjelasan Tools Tambahan ?
[+] 11. Domain To Ip = untuk mengubah domain menjadi ip, hasil di simpan di output dengan nama ip.txt
[+] 12. Spliter Cred = untuk memfilter data aws, twilio, smtp, dll dari hasil scanning config (configfound.txt) perlu di ingat hanya 
	filter urlnya tidak regex jadi silakan buka saja url resultnya
[+] 13. FileManger Scanner = untuk mencari filemanager kcfinder, jquery, laravel filemanager dan jqueryfilemanager resulst di simpan
	dengan nama "fmvuln.txt" di folder ouput (masukan path dari fodler path sudah ada beberapa anda bisa costm sendiri) pastikan juga
	list domainnya domain.com tidak menggunakan http:// atau https:// 
[+] 14. Twilio Checker = untuk mengecek mass validasi twilio sekaligus mengecek balance, format list sid:token hasilnya di simpan
	pada folder output dengan nama twilio.txt
[+] 15. Paypal Checker V1 = untuk mengecek validasi api paypal contoh format client_id:client_secret ada dua ouput yaitu 
	ppvalidkey.txt = artinya key valid namun tidak punya akses mengecek saldo (ada kemungkinan bisa mengirim)
	ppvalidbalance.txt = artinya key valid dan juga bisa melihat saldo (ada kemungkinan bisa mengirim)
======================================================================================================================================
# Thanks for buy 
List domain free  265.236.179 dari https://domains-monitor.com/
link : https://drive.google.com/drive/folders/1owXYNlNRHMmuoCevnHuIMz4ffUrs4Mfo?usp=share_link
New Akun domains monitor : claudiaevelyn772@gmail.com|Marianasweb3344
======================================================================================================================================
# Ada error langsung dm ajah via facebook
https://www.facebook.com/endang.phtml/ atau endangalfarisi10@gmail.com
======================================================================================================================================

