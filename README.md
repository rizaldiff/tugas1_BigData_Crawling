# tugas1_BigData_Crawling
Halo, ini adalah repository saya dalam pengerjaan Tugas 1 Pengelolaan Big Data untuk Crawling Website


Cara menggunakan container MongoDb :
1. Buka terminal, kemudian pull images MongoDb dengan syntax Docker pull mongo:latest
2. Tunggu beberapa saat hingga download selesai
3. buat file direktori baru dengan syntax mkdir mongodb-tugas1
4. masuk ke direktori tersebut dengan cd mongodb-tugas1
5. masukkan syntax docker run -d -p 27023:27017 -v ~/mongodb-tugas1:/data/db --name tugas1 mongo:latest agar images terbentuk dan dapat dijalankan
6. masuk ke mongoshell dengan syntax docker exec -it tugas1 bash

Cara menjalankan aplikasi Crawler
