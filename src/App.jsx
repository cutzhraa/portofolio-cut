import { useEffect, useState } from 'react';
import './App.css';

const projects = [
  { name: 'StudiKoding', category: ['Belajar pemrograman', 'Learn to code'], tech: 'Next.js', image: '/studikoding.png', url: 'https://studikoding.vercel.app', description: ['Platform web interaktif untuk belajar Python dengan materi terarah.', 'An interactive web platform for learning Python through structured lessons.'] },
  { name: 'Pawroutine', category: ['Perawatan hewan', 'Pet care'], tech: 'React · Vite', image: '/pawroutine.png', url: 'https://pawroutineku.vercel.app', description: ['Aplikasi untuk mengatur rutinitas dan memantau perawatan hewan peliharaan.', 'An app for organizing routines and tracking pet care.'] },
  { name: 'Mouri Minds', category: ['Belajar bahasa', 'Language learning'], tech: 'Supabase', image: '/conan.png', url: 'https://mouri-minds.vercel.app', description: ['Platform belajar bahasa Jepang interaktif dengan Supabase dan audio karakter.', 'An interactive Japanese learning platform with Supabase and character audio.'] },
  { name: 'Dupcut', category: ['Utilitas web', 'Web utility'], tech: 'Client-side', image: '/dupcut.png', url: 'https://dupcut.vercel.app', description: ['Utilitas browser untuk mengelola file, membersihkan duplikat, dan mengedit gambar.', 'A browser utility for managing files, removing duplicates, and editing images.'] },
];
const skills = ['HTML & CSS', 'PHP', 'React', 'Next.js', 'Tailwind CSS', 'Linux', ['Jaringan komputer', 'Computer networking'], 'Git & GitHub'];

export default function App() {
  const [lang, setLang] = useState('ID');
  const [menuOpen, setMenuOpen] = useState(false);
  const en = lang === 'EN';
  useEffect(() => {
    document.documentElement.lang = en ? 'en' : 'id';
    document.title = en ? 'Cut Azizah Zahra — Portfolio' : 'Cut Azizah Zahra — Portofolio';
  }, [en]);
  useEffect(() => {
    const elements = document.querySelectorAll('[data-reveal]');
    if (!('IntersectionObserver' in window)) {
      elements.forEach((element) => element.classList.add('is-visible'));
      return undefined;
    }
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -35px 0px' });
    elements.forEach((element) => observer.observe(element));
    return () => observer.disconnect();
  }, []);
  const about = en
    ? "Hello! I'm Cut Azizah Zahra, an Informatics graduate from Samudra University with a strong interest in modern web development. I enjoy turning creative ideas into functional web applications, from a pet tracker and language-learning app to client-side utilities. Technology moves quickly, and I'm always excited to explore new tools."
    : 'Halo! Saya Cut Azizah Zahra, seorang lulusan S1 Informatika Universitas Samudra yang memiliki ketertarikan pada pengembangan web modern. Saya senang mengubah ide-ide kreatif menjadi aplikasi web yang fungsional, mulai dari pet tracker, aplikasi belajar bahasa, hingga utilitas berbasis client-side. Bagi saya, dunia teknologi bergerak sangat cepat, dan saya selalu antusias untuk mengeksplorasi berbagai tools.';
  const nav = [['Tentang', 'About', '#tentang'], ['Keahlian', 'Skills', '#keahlian'], ['Skripsi', 'Research', '#skripsi'], ['Proyek', 'Projects', '#proyek']];

  return <div className="portofolio">
    <div className="ambient ambient-one" aria-hidden="true" /><div className="ambient ambient-two" aria-hidden="true" /><div className="grid-texture" aria-hidden="true" />
    <header className="site-header">
      <a className="wordmark" href="#top" aria-label="Cut Azizah Zahra"><span className="wordmark-mark"><img src="/pass_foto.png" alt="" /></span><span>Cut Azizah Zahra</span></a>
      <nav className={`nav-links ${menuOpen ? 'is-open' : ''}`} aria-label={en ? 'Main navigation' : 'Navigasi utama'}>{nav.map(([id, eng, href]) => <a key={href} href={href} onClick={() => setMenuOpen(false)}>{en ? eng : id}</a>)}</nav>
      <div className="header-actions"><button className="language-toggle" onClick={() => setLang(en ? 'ID' : 'EN')} aria-label={en ? 'Switch language' : 'Ganti bahasa'}>{lang}</button><button className="menu-toggle" onClick={() => setMenuOpen(!menuOpen)} aria-expanded={menuOpen}>{menuOpen ? (en ? 'Close' : 'Tutup') : 'Menu'}</button></div>
    </header>
    <main id="top">
      <section className="hero section-shell" id="tentang">
        <div className="hero-copy" data-reveal><p className="eyebrow"><span className="status-dot" />{en ? 'Portfolio · Informatics' : 'Portofolio · Informatika'}</p>
          <h1 className="hero-credential">{en ? 'Samudra University' : 'Universitas Samudra'} <span>·</span> {en ? 'Informatics' : 'Informatika'}</h1><p className="hero-intro">{about}</p>
          <div className="hero-actions"><a className="button button-primary" href="/portfolio-cut-azizah-zahra.pdf" download="Portofolio-Cut-Azizah-Zahra.pdf">{en ? 'Download Portfolio (PDF)' : 'Unduh Portofolio (PDF)'} <span aria-hidden="true">&#8595;</span></a><a className="button button-quiet" href="https://github.com/cutzhraa" target="_blank" rel="noreferrer">{en ? 'Find me on GitHub' : 'Temukan saya di GitHub'}</a><a className="button button-linkedin" href="https://id.linkedin.com/in/cut-azizah-zahra-a51405437" target="_blank" rel="noreferrer">LinkedIn <span aria-hidden="true">&#8599;</span></a></div>
          <div className="hero-meta"><span>{en ? 'Samudra University' : 'Universitas Samudra'}</span><span className="meta-separator" /><span>{en ? 'B.Sc. Informatics' : 'S1 Informatika'}</span><span className="meta-separator" /><span>{en ? 'Indonesia' : 'Indonesia'}</span></div>
        </div>
        <div className="hero-visual" data-reveal><div className="portrait-frame"><img src="/pass_foto.png" alt="Cut Azizah Zahra" /></div><div className="portrait-note"><span className="note-index">01 / 04</span><span>{en ? 'Thoughtful by design' : 'Teliti dalam berkarya'}</span></div><div className="orbit orbit-large" aria-hidden="true" /><div className="orbit orbit-small" aria-hidden="true" /><span className="visual-caption">CREATIVE &#183; CURIOUS &#183; CODE</span></div>
        <a className="scroll-cue" href="#keahlian"><span />{en ? 'Scroll to explore' : 'Gulir untuk menjelajah'}</a>
      </section>
      <section className="content-section section-shell" id="keahlian" data-reveal>
        <div className="section-heading" data-reveal><div><p className="eyebrow">01 &#8212; {en ? 'Toolkit' : 'Perangkat'}</p><h2>{en ? 'Tools I work with' : 'Teknologi yang saya gunakan'}</h2></div><p>{en ? 'A practical toolkit for building useful, considered web experiences.' : 'Perangkat praktis untuk membangun pengalaman web yang berguna dan terencana.'}</p></div>
        <div className="skill-list">{skills.map((skill, i) => <div className="skill-item" data-reveal key={i}><span className="skill-number">0{i + 1}</span><span>{Array.isArray(skill) ? skill[en ? 1 : 0] : skill}</span><span className="skill-line" /></div>)}</div>
      </section>
      <section className="research-section section-shell" id="skripsi" data-reveal>
        <div className="section-heading" data-reveal><div><p className="eyebrow">02 — {en ? 'Research' : 'Penelitian'}</p><h2>{en ? "Bachelor's thesis" : 'Skripsi'}</h2></div><span className="research-tag">{en ? 'Samudra University · 2026' : 'Universitas Samudra · 2026'}</span></div>
        <article className="research-card" data-reveal><div className="research-top"><span>{en ? 'NETWORK SECURITY' : 'KEAMANAN JARINGAN'}</span><span>{en ? 'UNDERGRADUATE THESIS' : 'TUGAS AKHIR SARJANA'}</span></div>
          <h3>{en ? 'Server Security Protection with Telegram Notifications Using Port Knocking and Threat Modelling' : 'Perlindungan Keamanan Server dengan Notifikasi Telegram Menggunakan Port Knocking dan Threat Modelling'}</h3>
          <p>{en ? 'Implemented Port Knocking and Threat Modelling on a Linux server with a Mikrotik gateway to conceal critical ports from external scans. Tested against brute force, SQL injection, and DoS attacks in VirtualBox, with real-time Telegram bot notifications.' : 'Mengimplementasikan Port Knocking dan Threat Modelling pada server Linux dengan gateway Mikrotik untuk menyembunyikan port kritikal dari pemindaian luar. Pengujian dilakukan terhadap serangan Brute Force, SQL Injection, dan DoS di VirtualBox, dilengkapi notifikasi bot Telegram real-time.'}</p>
          <div className="research-results"><div><strong>{en ? '91.67%' : '91,67%'}</strong><span>{en ? 'Overall accuracy' : 'Akurasi keseluruhan'}</span></div><div><strong>100%</strong><span>{en ? 'Brute force & SQL injection' : 'Brute Force & SQLi'}</span></div><div><strong>{en ? '66.67%' : '66,67%'}</strong><span>{en ? 'DoS detection' : 'Deteksi DoS'}</span></div><div><strong>{en ? 'Filtered' : 'Tersaring'}</strong><span>{en ? 'Critical ports' : 'Port kritikal'}</span></div></div>
        </article>
      </section>
      <section className="content-section section-shell" id="proyek" data-reveal>
        <div className="section-heading" data-reveal><div><p className="eyebrow">03 &#8212; {en ? 'Selected work' : 'Karya pilihan'}</p><h2>{en ? 'Projects & experiments' : 'Proyek dan eksplorasi'}</h2></div><p>{en ? 'Small ideas, carefully shaped into useful digital products.' : 'Ide-ide yang dikembangkan menjadi produk digital yang bermanfaat.'}</p></div>
        <div className="project-grid">{projects.map((p, i) => <a className={`project-card project-${i + 1}`} data-reveal style={{ '--reveal-delay': `${i * 90}ms` }} href={p.url} target="_blank" rel="noreferrer" key={p.name}>
          <div className="project-image"><img src={p.image} alt={`${p.name} logo`} /><span className="project-open" aria-hidden="true">&#8599;</span></div>
          <div className="project-details"><div><p className="project-category">{p.category[en ? 1 : 0]}</p><h3>{p.name}</h3></div><span className="project-tech">{p.tech}</span></div><p className="project-description">{p.description[en ? 1 : 0]}</p>
        </a>)}</div>
      </section>
    </main>
    <footer className="site-footer"><div className="footer-inner section-shell"><div className="footer-signature" data-reveal><img className="footer-photo" src="/pass_foto.png" alt="Cut Azizah Zahra" /><div><strong>Cut Azizah Zahra</strong><span>{en ? 'Informatics · Web Development' : 'Informatika · Pengembangan Web'}</span></div></div><a className="footer-top" href="#top">{en ? 'Back to top' : 'Kembali ke atas'} <span aria-hidden="true">&#8593;</span></a><span className="footer-copyright">© 2026 Cut Azizah Zahra. {en ? 'All rights reserved.' : 'Seluruh hak cipta dilindungi.'}</span></div></footer>
  </div>;
}



