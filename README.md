# Portofolio Cut Azizah Zahra

Portofolio pribadi Cut Azizah Zahra, lulusan S1 Informatika Universitas Samudra. Website ini menampilkan profil, keahlian, penelitian skripsi, dan karya pilihan.

**Demo:** [portofolio-cut.vercel.app](https://portofolio-cut.vercel.app)

## Menjalankan secara lokal

Pastikan Node.js dan npm sudah terpasang, lalu jalankan:

```bash
npm install
npm run dev
```

Buka alamat lokal yang ditampilkan Vite di terminal.

## Build produksi

```bash
npm run build
npm run preview
```

File hasil build tersedia di folder `dist/`.

## Unduh portofolio PDF

Portofolio PDF delapan slide berformat landscape tersedia dalam bahasa Indonesia dan English. Tombol unduh di website mengikuti bahasa yang sedang dipilih.

- Indonesia: `public/portfolio-cut-azizah-zahra.pdf`
- English: `public/portfolio-cut-azizah-zahra-en.pdf`

PDF dibuat menggunakan `python generate_portfolio_pdf.py` (memerlukan Pillow).

## Teknologi

- React
- Vite
- CSS
