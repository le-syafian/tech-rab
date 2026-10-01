# Tech Stack: Web-based RAB App

Aplikasi ini dibangun dengan pendekatan *minimalist* dan *data-driven* untuk menggantikan spreadsheet yang rentan error.

## 1. Backend: FastAPI (Python)
*   **Why**: 
    *   **Performance**: Sangat cepat untuk menangani perhitungan RAB yang kompleks.
    *   **Developer Velocity**: Dokumentasi API (Swagger) otomatis memudahkan pengembangan fitur baru.
    *   **Typed**: Integrasi erat dengan Python type-hinting, mengurangi bug kalkulasi sejak tahap penulisan kode.

## 2. Frontend: HTMX + Tailwind CSS
*   **Why**:
    *   **No Overhead**: Menghindari kerumitan framework JS berat (seperti React/Vue).
    *   **Server-Side Rendering (SSR)**: Logika bisnis tetap di Python (tidak terpecah antara client & server), sehingga hitungan RAB lebih konsisten dan mudah di-audit.
    *   **Interactivity**: HTMX memungkinkan update baris RAB di browser tanpa *page reload*, memberikan sensasi aplikasi desktop.

## 3. Database: SQLite
*   **Why**:
    *   **Portability**: Satu file (`rab.db`) yang mudah di-backup dan di-commit ke Git.
    *   **Zero Configuration**: Tidak perlu mengelola server database eksternal (seperti PostgreSQL/MySQL).
    *   **Data Integrity**: Mendukung ACID compliance untuk memastikan kalkulasi volume & harga tidak korup.

## 4. Versioning: Git
*   **Why**:
    *   **Audit Trail**: Setiap perubahan angka RAB terekam (`git log`).
    *   **Single Source of Truth**: Menghilangkan masalah file `RAB_V1`, `RAB_Final`, `RAB_Final_Banget`.
    *   **Collaboration**: Memungkinkan tim bekerja di cabang (branch) berbeda tanpa saling menimpa data.

---
*Prinsip utama: Deletion over addition, Boring over clever.*
