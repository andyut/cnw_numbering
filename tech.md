# Technical Documentation — CNW Numbering

## 1. Overview

Modul ini digunakan untuk mengelola nomor dokumen secara otomatis berdasarkan kombinasi berikut:

- Perusahaan
- Suffix dokumen
- Tahun
- Bulan
- Counter urut

Tujuan utama modul adalah memastikan setiap dokumen memiliki nomor unik yang terstruktur dan mudah ditelusuri.

Contoh format nomor:

**INV26040001**

Arti contoh di atas:

- INV = suffix dokumen
- 26 = tahun dua digit
- 04 = bulan
- 0001 = urutan ke-1 pada periode tersebut

---

## 2. Informasi Modul

| Item | Nilai |
|---|---|
| Nama Modul | AU-Doc Numbering |
| Technical Name | cnw_numbering |
| Versi | 0.1 |
| Author | Andy Utomo |
| Category | others |
| Application | Ya |
| Dependensi | base |

Referensi metadata modul dapat dilihat pada [cnw_numbering/__manifest__.py](cnw_numbering/__manifest__.py).

---

## 3. Struktur Proyek

Struktur utama modul:

- [cnw_numbering/__manifest__.py](cnw_numbering/__manifest__.py) — metadata modul dan daftar file yang diload
- [cnw_numbering/models/models.py](cnw_numbering/models/models.py) — model utama dan wizard numbering
- [cnw_numbering/views/views.xml](cnw_numbering/views/views.xml) — tampilan list dan form untuk data numbering
- [cnw_numbering/views/wizard_view.xml](cnw_numbering/views/wizard_view.xml) — definisi wizard generate nomor
- [cnw_numbering/menu/menu.xml](cnw_numbering/menu/menu.xml) — menu utama aplikasi
- [cnw_numbering/security/group_users.xml](cnw_numbering/security/group_users.xml) — grup user modul
- [cnw_numbering/security/ir.model.access.csv](cnw_numbering/security/ir.model.access.csv) — akses CRUD model
- [cnw_numbering/views/templates.xml](cnw_numbering/views/templates.xml) — template web placeholder
- [cnw_numbering/controllers/controllers.py](cnw_numbering/controllers/controllers.py) — placeholder controller, belum digunakan

---

## 4. Arsitektur Fungsional

Secara teknis, modul terdiri dari dua komponen inti:

### 4.1 Model Persisten

Model persisten menyimpan counter numbering per kombinasi perusahaan dan periode.

Nama model:

**cnw.numbering**

Model ini berfungsi sebagai tabel registry sequence.

### 4.2 Wizard Transien

Wizard digunakan untuk meminta input dari user saat ingin mengambil nomor dokumen baru.

Nama model:

**cnw.numbering.wizard**

Wizard ini bersifat sementara dan dipakai sebagai interface pemicu logika numbering.

---

## 5. Detail Model Data

### 5.1 Model cnw.numbering

Didefinisikan pada [cnw_numbering/models/models.py](cnw_numbering/models/models.py).

| Field | Tipe | Wajib | Fungsi |
|---|---|---:|---|
| name | Char | Tidak | Nama atau label numbering |
| company_id | Many2one ke res.company | Ya | Menentukan numbering per perusahaan |
| suffix | Char | Ya | Prefix atau kode dokumen |
| iyear | Char | Ya | Tahun numbering |
| imonth | Char | Ya | Bulan numbering |
| numbering | Integer | Tidak | Counter urut aktif |
| user_update | Many2one ke res.users | Tidak | User terakhir yang memperbarui |

### 5.2 Model cnw.numbering.wizard

| Field | Tipe | Wajib | Fungsi |
|---|---|---:|---|
| suffix | Char | Tidak | Kode dokumen yang ingin digenerate |
| docdate | Date | Ya | Tanggal dokumen untuk menentukan periode |

---

## 6. Alur Bisnis Numbering

Flow numbering saat fungsi dipanggil adalah sebagai berikut:

1. Sistem menerima input suffix dan tanggal dokumen.
2. Sistem mengambil company aktif dari user yang login.
3. Sistem mencari data pada model cnw.numbering berdasarkan kombinasi:
   - company_id
   - suffix
   - iyear
   - imonth
4. Jika data belum ada, sistem membuat record baru dengan counter awal 1.
5. Jika data sudah ada, sistem menaikkan nilai counter sebesar 1.
6. Sistem membentuk nomor dokumen akhir dengan pola:
   - suffix + tahun dua digit + bulan dua digit + urutan 4 digit
7. Hasil akhir dikembalikan sebagai string nomor dokumen.

### Formula Hasil

Pola umum:

**SUFFIX + YY + MM + NNNN**

Contoh:

- Suffix: INV
- Tanggal: 2026-04-19
- Urutan: 1
- Hasil: INV26040001

---

## 7. Implementasi Logika Utama

Logika utama terdapat pada method berikut di [cnw_numbering/models/models.py](cnw_numbering/models/models.py):

### 7.1 getnumbering

Method ini menerima dua parameter:

- suffix
- docdate

Tanggung jawab method:

- mencari counter aktif
- menentukan next number
- membuat record baru bila periode belum ada
- update record bila periode sudah ada
- membentuk hasil akhir nomor dokumen

### 7.2 getnumbering2

Method ini dipanggil dari tombol wizard.

Fungsi teknisnya hanya meneruskan input wizard ke method getnumbering.

---

## 8. User Interface

### 8.1 Menu

Menu didefinisikan pada [cnw_numbering/menu/menu.xml](cnw_numbering/menu/menu.xml).

Struktur menu:

- CNW NUMB
  - [D] oc Numbering
    - Document Numbering

Menu ini membuka action untuk model cnw.numbering dalam mode list dan form.

### 8.2 View Data Numbering

Didefinisikan pada [cnw_numbering/views/views.xml](cnw_numbering/views/views.xml).

Tampilan yang tersedia:

- List view untuk memonitor counter per perusahaan dan periode
- Form view untuk melihat atau mengedit record numbering

### 8.3 Wizard Numbering

Wizard tersedia pada [cnw_numbering/views/wizard_view.xml](cnw_numbering/views/wizard_view.xml).

Komponen wizard:

- Input suffix
- Input tanggal dokumen
- Tombol get untuk memicu generate nomor
- Tombol cancel untuk menutup dialog

---

## 9. Security dan Hak Akses

### 9.1 Group User

Grup keamanan didefinisikan pada [cnw_numbering/security/group_users.xml](cnw_numbering/security/group_users.xml).

Grup yang tersedia:

- Users

Grup ini berada pada kategori:

- CNW-Document Numbering

### 9.2 Access Rights

Hak akses berada di [cnw_numbering/security/ir.model.access.csv](cnw_numbering/security/ir.model.access.csv).

Untuk kedua model berikut, hak akses yang diberikan adalah penuh:

- Read
- Write
- Create
- Delete

Model yang tercakup:

- cnw.numbering
- cnw.numbering.wizard

Catatan penting:

Meskipun menu dibatasi oleh grup tertentu, file access CSV saat ini tidak membatasi berdasarkan grup, sehingga secara teknis akses model bersifat luas jika ada akses dari jalur lain.

---

## 10. Dependensi dan Integrasi

### 10.1 Dependensi Odoo

Modul ini hanya bergantung pada modul standar berikut:

- base

Artinya modul relatif ringan dan tidak membutuhkan modul accounting, sales, atau inventory.

### 10.2 Integrasi Saat Ini

Saat ini integrasi masih bersifat generik. Modul belum otomatis terhubung ke model transaksi tertentu seperti:

- sale.order
- purchase.order
- account.move
- stock.picking

Untuk penggunaan nyata, method numbering biasanya dipanggil dari model dokumen bisnis tersebut.

---

## 11. Skenario Penggunaan Developer

Contoh penggunaan dari sisi developer:

1. Ambil suffix berdasarkan tipe dokumen, misalnya INV.
2. Ambil tanggal dokumen dari field transaksi.
3. Panggil method numbering untuk mendapatkan nomor baru.
4. Simpan hasilnya ke field nomor dokumen pada model transaksi.

Contoh skenario bisnis:

- Invoice customer menggunakan suffix INV
- Purchase request menggunakan suffix PR
- Delivery order menggunakan suffix DO

Dengan pendekatan ini, setiap jenis dokumen memiliki sequence terpisah per bulan dan per tahun.

---

## 12. Catatan Teknis Penting

Berdasarkan implementasi saat ini, terdapat beberapa hal yang perlu diperhatikan:

### 12.1 Wizard View Belum Diload di Manifest

File wizard tersedia di source, tetapi belum tercantum pada daftar data di [cnw_numbering/__manifest__.py](cnw_numbering/__manifest__.py).

Dampaknya:

- wizard tidak otomatis terpasang saat modul di-install
- action wizard bisa tidak tersedia pada database target

### 12.2 Tidak Ada Constraint Unik

Belum ada SQL constraint atau Python constraint untuk mencegah duplikasi kombinasi berikut:

- company_id
- suffix
- iyear
- imonth

Risiko:

- bisa terbentuk lebih dari satu record sequence untuk periode yang sama
- rawan race condition bila banyak user memanggil numbering secara bersamaan

### 12.3 Potensi Inkonsistensi Tipe Data

Field iyear dan imonth disimpan sebagai Char, sedangkan sumber nilainya berasal dari angka tahun dan bulan.

Walaupun Odoo biasanya melakukan konversi, penggunaan tipe Integer atau constraint validasi akan membuat desain lebih konsisten.

### 12.4 Result Wizard Belum Ditampilkan ke User

Method getnumbering2 memanggil proses generate, tetapi tidak mengembalikan output ke tampilan wizard atau ke notification message.

Akibatnya:

- user tidak langsung melihat hasil nomor dari UI wizard
- hasil lebih cocok dipakai dari pemanggilan programatik dibanding interaksi manual murni

### 12.5 Logging Masih Menggunakan Print

Pada logika numbering masih ada penggunaan print untuk debugging.

Rekomendasi produksi:

- gunakan logger Odoo
- hindari print langsung pada server log

---

## 13. Rekomendasi Penyempurnaan

Agar modul lebih siap dipakai pada lingkungan produksi, berikut rekomendasi teknis:

1. Tambahkan [cnw_numbering/views/wizard_view.xml](cnw_numbering/views/wizard_view.xml) ke manifest.
2. Tambahkan constraint unik untuk kombinasi perusahaan, suffix, tahun, dan bulan.
3. Gunakan locking atau pendekatan sequence yang aman untuk concurrent access.
4. Ubah field tahun dan bulan menjadi tipe numerik atau validasi yang lebih ketat.
5. Tampilkan hasil numbering ke wizard atau simpan langsung ke dokumen asal.
6. Tambahkan unit test untuk skenario multi-company dan pergantian bulan.
7. Lengkapi controller atau hapus file placeholder bila tidak digunakan.

---

## 14. Ringkasan Teknis

Secara keseluruhan, modul ini adalah sequence manager sederhana untuk nomor dokumen berbasis:

- perusahaan
- suffix dokumen
- tahun
- bulan
- counter incremental

Kekuatan utama modul:

- sederhana
- mudah dipahami
- cocok sebagai pondasi numbering custom di Odoo

Batasan implementasi saat ini:

- wizard belum sepenuhnya terhubung lewat manifest
- belum ada pengamanan concurrency
- belum ada constraint unik data
- UI wizard belum menampilkan hasil secara eksplisit

Meski demikian, struktur dasarnya sudah cukup baik untuk dijadikan fondasi pengembangan lanjutan.
