from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).parent
PUBLIC = ROOT / "public"
W, H = 1600, 900
PAGE_W, PAGE_H = 960, 540
BG, INK, MUTED = "#fbfafc", "#25252b", "#656873"
BLUE, NAVY, TEAL, RUST = "#15559b", "#103f76", "#287c79", "#a5664d"
LINE, PALE = "#e2e5ed", "#eef1f8"
FONT = "C:/Windows/Fonts/arial.ttf"
BOLD = "C:/Windows/Fonts/arialbd.ttf"

PROJECTS = [
    ("StudiKoding", "BELAJAR PEMROGRAMAN", "LEARN TO CODE",
     "Platform web interaktif untuk belajar Python dengan materi terarah.",
     "An interactive web platform for learning Python through structured lessons.",
     "studikoding.png", "https://studikoding.vercel.app"),
    ("Pawroutine", "PERAWATAN HEWAN", "PET CARE",
     "Aplikasi untuk mengatur rutinitas dan memantau perawatan hewan peliharaan.",
     "An app for organizing routines and tracking pet care.",
     "pawroutine.png", "https://pawroutineku.vercel.app"),
    ("PocketSmart", "MANAJEMEN KEUANGAN", "PERSONAL FINANCE",
    "Aplikasi pengelola keuangan pribadi untuk mencatat pemasukan, pengeluaran, dan memantau saldo secara otomatis.",
    "A personal finance application for recording income and expenses, with automatic balance tracking.",
    "pocketsmart.png", "https://github.com/cutzhraa/pocketsmart/releases/latest"),
    ("Dupcut", "UTILITAS WEB", "WEB UTILITY",
     "Utilitas browser untuk mengelola file, menghapus duplikat, dan mengedit gambar.",
     "A browser utility for managing files, removing duplicates, and editing images.",
     "dupcut.png", "https://dupcut.vercel.app"),
]


def ft(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def page(index, label):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.polygon([(0, 0), (340, 0), (0, 230)], fill=PALE)
    d.polygon([(W, H), (W - 330, H), (W, H - 245)], fill="#edf0f8")
    d.ellipse((W - 225, -135, W + 75, 165), outline="#e2e7f0", width=3)
    d.text((76, 38), "CUT AZIZAH ZAHRA", font=ft(16, True), fill=INK)
    d.text((W - 76, 38), f"{index:02d} / 08", font=ft(15, True), fill=BLUE, anchor="ra")
    d.text((78, 84), label.upper(), font=ft(15, True), fill=RUST)
    d.line((78, 846, W - 78, 846), fill=LINE, width=2)
    d.text((78, 858), "PORTOFOLIO CUT AZIZAH ZAHRA", font=ft(12, True), fill=MUTED)
    d.text((W - 78, 858), "2026", font=ft(12, True), fill=MUTED, anchor="ra")
    return im, d, []


def lines(d, text, f, width):
    result, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if d.textlength(trial, font=f) <= width:
            current = trial
        else:
            if current:
                result.append(current)
            current = word
    if current:
        result.append(current)
    return result


def para(d, text, xy, width, size=24, color=MUTED, leading=1.45, bold=False, justify=False):
    x, y = xy
    f = ft(size, bold)
    wrapped = lines(d, text, f, width)
    for index, line in enumerate(wrapped):
        words = line.split()
        if justify and index < len(wrapped) - 1 and len(words) > 1:
            word_width = sum(d.textlength(word, font=f) for word in words)
            gap = max(0, (width - word_width) / (len(words) - 1))
            cursor = x
            for word in words:
                d.text((cursor, y), word, font=f, fill=color)
                cursor += d.textlength(word, font=f) + gap
        else:
            d.text((x, y), line, font=f, fill=color)
        y += int(size * leading)
    return y


def heading(d, text, xy, size=48, color=INK):
    d.text(xy, text, font=ft(size, True), fill=color)


def contain(path, size):
    return ImageOps.contain(Image.open(path).convert("RGB"), size, method=Image.Resampling.LANCZOS)


def crop(path, size):
    return ImageOps.fit(Image.open(path).convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(.5, .3))


def portrait(im, box, radius):
    x, y, w, h = box
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x - 14, y - 14, x + w + 14, y + h + 14), radius=radius + 10, fill="#174f91")
    photo = crop(PUBLIC / "pass_foto.png", (w, h))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=255)
    im.paste(photo, (x, y), mask)
    ImageDraw.Draw(im).rounded_rectangle((x - 14, y - 14, x + w + 14, y + h + 14), radius=radius + 10, outline="#aabbd6", width=3)


def add_link(links, rect, url):
    links.append((rect, url))


def make_pages(en=False):
    result = []

    # 1 — Cover
    im, d, links = page(1, "Portfolio · Informatics" if en else "Portofolio · Informatika")
    d.polygon([(1020, 85), (W, 85), (W, 845), (1360, 845), (1120, 620)], fill="#e8ecf5")
    portrait(im, (1120, 140, 330, 625), 160)
    heading(d, "PORTFOLIO" if en else "PORTOFOLIO", (100, 240), 73, BLUE)
    heading(d, "CUT AZIZAH ZAHRA", (105, 350), 45)
    d.line((108, 430, 590, 430), fill=BLUE, width=5)
    para(d, "Informatics graduate · Samudra University" if en else "Lulusan Informatika · Universitas Samudra", (108, 470), 770, 26)
    d.text((108, 570), "INFORMATION TECHNOLOGY" if en else "TEKNOLOGI INFORMASI", font=ft(20, True), fill=RUST)
    d.text((108, 610), "2026", font=ft(17, True), fill=MUTED)
    result.append((im, links))

    # 2 — About and education
    im, d, links = page(2, "About me" if en else "Tentang saya")
    heading(d, "Hello, I'm Cut." if en else "Halo, saya Cut.", (85, 145), 52, BLUE)
    bio = (
    "I am an Informatics graduate from Samudra University with an interest in information technology, particularly application development, database management, and computer systems. I have basic knowledge of HTML, CSS, PHP, JavaScript, MySQL, and Linux. I have worked on web-based projects during my studies and completed an internship at the Department of Communication and Informatics. I am able to work in a team, eager to learn, and responsible in completing tasks."
    if en else
    "Saya merupakan lulusan S1 Informatika Universitas Samudra yang memiliki ketertarikan di bidang teknologi informasi, khususnya pengembangan aplikasi, pengelolaan database, dan sistem komputer. Memiliki pemahaman dasar mengenai HTML, CSS, PHP, JavaScript, MySQL, serta Linux. Terbiasa mengerjakan proyek berbasis web selama masa perkuliahan dan memiliki pengalaman magang di Dinas Komunikasi dan Informatika. Mampu bekerja sama dalam tim, memiliki kemauan untuk belajar, serta bertanggung jawab dalam menyelesaikan pekerjaan.")
    para(d, bio, (90, 240), 820, 25, MUTED, 1.5, justify=True)
    d.rounded_rectangle((86, 630, 1000, 790), radius=18, fill=PALE)
    d.text((122, 660), "EDUCATION" if en else "PENDIDIKAN", font=ft(16, True), fill=RUST)
    d.text((122, 700), "B.Sc. in Informatics" if en else "S1 Informatika", font=ft(29, True), fill=INK)
    d.text((122, 746), "Samudra University · 2021–2026" if en else "Universitas Samudra · 2021–2026", font=ft(22), fill=MUTED)
    portrait(im, (1110, 185, 340, 590), 165)
    result.append((im, links))

    # 3 — Skills
    im, d, links = page(3, "Skills" if en else "Keahlian")
    heading(d, "What I bring" if en else "Keahlian yang saya miliki", (85, 150), 50, BLUE)
    d.rounded_rectangle((85, 255, 1515, 770), radius=22, fill=PALE, outline="#dbe2f0", width=2)
    d.text((125, 295), "HARD SKILLS", font=ft(18, True), fill=TEAL)
    hard = [
    "HTML & CSS",
    "JavaScript",
    "PHP",
    "MySQL",
    "Linux",
    "React",
    "Next.js",
    "Tailwind CSS",
    "Jaringan komputer" if not en else "Computer networking"
]
    for i, skill in enumerate(hard):
        row, col = divmod(i, 4)
        x, y = 125 + col * 345, 375 + row * 130
        d.rounded_rectangle((x, y, x + 300, y + 78), radius=14, fill="#fff", outline=LINE, width=2)
        d.ellipse((x + 22, y + 31, x + 36, y + 45), fill=RUST)
        d.text((x + 54, y + 23), skill, font=ft(21, True), fill=INK)
    result.append((im, links))

    # 4 — Experience. Keep the proof of completion on the certificate slide.
    im, d, links = page(4, "Experience" if en else "Pengalaman")
    d.rounded_rectangle((85, 180, 835, 760), radius=23, fill=PALE, outline="#dbe2f0", width=2)
    d.text((125, 230), "MBKM · CERTIFIED INTERNSHIP" if en else "MBKM · MAGANG BERSERTIFIKAT", font=ft(16, True), fill=RUST)
    heading(d, "Diskominfo Langsa", (125, 292), 43, BLUE)
    para(d, "Langsa City Communication and Informatics Office" if en else "Dinas Komunikasi dan Informatika Kota Langsa", (130, 360), 650, 21)
    d.line((130, 445, 785, 445), fill="#cad4e5", width=2)
    d.text((130, 485), "JANUARY 23 – APRIL 23, 2024" if en else "23 JANUARI – 23 APRIL 2024", font=ft(21, True), fill=TEAL)
    para(d, "Completed the Certified Internship Program (MBKM) with Diskominfo Langsa." if en else "Menyelesaikan Program Magang Bersertifikat Kampus Merdeka (MBKM) bersama Diskominfo Langsa.", (130, 550), 635, 20)
    d.rounded_rectangle((940, 250, 1515, 700), radius=24, fill="#164f95")
    d.text((990, 305), "MBKM" if en else "PROGRAM MBKM", font=ft(20, True), fill="#d9e5f5")
    d.text((990, 370), "2024", font=ft(61, True), fill="white")
    d.line((994, 470, 1455, 470), fill="#8aa9d0", width=3)
    d.text((990, 505), "JANUARY 23" if en else "23 JANUARI", font=ft(22, True), fill="white")
    d.text((990, 560), "APRIL 23" if en else "23 APRIL", font=ft(22, True), fill="white")
    d.ellipse((966, 515, 980, 529), fill="#d9e5f5")
    d.ellipse((966, 570, 980, 584), fill="#d9e5f5")
    result.append((im, links))

    # 5 & 6 — Two projects per slide, with clickable demo labels.
    for page_no, group in ((5, PROJECTS[:2]), (6, PROJECTS[2:])):
        im, d, links = page(page_no, "Selected projects" if en else "Proyek pilihan")
        heading(d, "Selected work" if en else "Karya pilihan", (85, 150), 50, BLUE)
        for i, project in enumerate(group):
            x, y, cw, ch = 85 + i * 725, 245, 675, 535
            d.rounded_rectangle((x, y, x + cw, y + ch), radius=23, fill="#fff", outline=LINE, width=2)
            d.rounded_rectangle((x + 28, y + 28, x + 190, y + 190), radius=18, fill=PALE)
            logo = contain(PUBLIC / project[5], (132, 132))
            im.paste(logo, (x + 43 + (132 - logo.width)//2, y + 43 + (132 - logo.height)//2))
            d.text((x + 28, y + 215), project[2] if en else project[1], font=ft(14, True), fill=RUST)
            d.text((x + 28, y + 252), project[0], font=ft(31, True), fill=INK)
            para(d, project[4] if en else project[3], (x + 30, y + 310), cw - 60, 19, MUTED, 1.42)
            label = "ONLINE DEMO" if en else "DEMO ONLINE"
            d.text((x + 30, y + 440), label, font=ft(15, True), fill=TEAL)
            demo_url = project[6].removeprefix("https://")
            d.text((x + 30, y + 468), demo_url, font=ft(15), fill=BLUE)
            add_link(links, (x + 24, y + 432, x + 420, y + 500), project[6])
        result.append((im, links))

    # 7 — Research, text and point-by-point focus only.
    im, d, links = page(7, "Research" if en else "Penelitian")
    d.text((85, 145), "FINAL PROJECT" if en else "PENELITIAN SKRIPSI", font=ft(17, True), fill=RUST)
    heading(d, "Network security" if en else "Keamanan jaringan", (85, 185), 46, BLUE)
    thesis = ("Server Security Protection with Telegram Notifications Using Port Knocking and Threat Modelling" if en else
              "Perlindungan Keamanan Server dengan Notifikasi Telegram Menggunakan Port Knocking dan Threat Modelling")
    y = para(d, thesis, (88, 255), 900, 25, INK, 1.35, True)
    summary = ("Port Knocking and Threat Modelling were implemented on a Linux server with a Mikrotik gateway to conceal critical ports. Testing covered brute force, SQL injection, and DoS attacks in VirtualBox, with real-time Telegram bot notifications." if en else
               "Port Knocking dan Threat Modelling diterapkan pada server Linux dengan gateway Mikrotik untuk menyembunyikan port penting. Pengujian mencakup Brute Force, SQL Injection, dan DoS di VirtualBox, dengan notifikasi bot Telegram real-time.")
    y = para(d, summary, (88, y + 12), 900, 18, MUTED, 1.35)
    d.text((88, y + 14), "RESEARCH FOCUS" if en else "FOKUS PENELITIAN", font=ft(16, True), fill=RUST)
    points = (["Linux server security with a Mikrotik gateway.", "Port Knocking to conceal ports from external scans.", "Threat Modelling and real-time Telegram alerts.", "VirtualBox tests for brute force, SQL injection, and DoS."] if en else
              ["Keamanan server Linux dengan gateway Mikrotik.", "Port Knocking untuk menyamarkan port dari pemindaian luar.", "Threat Modelling dan notifikasi Telegram real-time.", "Pengujian VirtualBox terhadap Brute Force, SQL Injection, dan DoS."])
    for i, item in enumerate(points):
        yy = y + 48 + i * 39
        d.text((90, yy), "*", font=ft(20, True), fill=TEAL)
        d.text((120, yy + 2), item, font=ft(16), fill=INK)
    book = contain(PUBLIC / "skripsi.png", (390, 600))
    d.rounded_rectangle((1090, 195, 1500, 810), radius=14, fill="white", outline=LINE, width=2)
    im.paste(book, (1090 + (410 - book.width)//2, 200 + (600 - book.height)//2))
    result.append((im, links))

    # 8 — Certificate, confirmed public profile URLs and closing.
    im, d, links = page(8, "Contact · Thank you" if en else "Kontak · Terima kasih")
    heading(d, "Thank you" if en else "Terima kasih", (85, 155), 54, BLUE)
    para(d, "Thanks for exploring my portfolio." if en else "Terima kasih sudah melihat portofolio saya.", (90, 235), 700, 23)
    d.text((90, 315), "INTERNSHIP CERTIFICATE" if en else "SERTIFIKAT MAGANG", font=ft(16, True), fill=RUST)
    certificate = contain(PUBLIC / "sertifikat_magang.png", (675, 395))
    d.rounded_rectangle((82, 355, 770, 775), radius=13, fill="white", outline=LINE, width=2)
    im.paste(certificate, (82 + (688 - certificate.width)//2, 355 + (420 - certificate.height)//2))
    contacts = [
        ("LINKEDIN", "linkedin.com/in/cut-azizah-zahra-a51405437", "https://id.linkedin.com/in/cut-azizah-zahra-a51405437"),
        ("GITHUB", "github.com/cutzhraa", "https://github.com/cutzhraa/pocketsmart/releases/latest"),
    ]
    for i, (label, text, url) in enumerate(contacts):
        x, y = 830, 365 + i * 145
        d.rounded_rectangle((x, y, x + 660, y + 112), radius=17, fill="#fff", outline=LINE, width=2)
        d.text((x + 28, y + 20), label, font=ft(15, True), fill=RUST)
        d.text((x + 28, y + 57), text, font=ft(18, True), fill=TEAL)
        add_link(links, (x, y, x + 660, y + 112), url)
    d.text((830, 700), "Cut Azizah Zahra · Informatika · Universitas Samudra" if not en else "Cut Azizah Zahra · Informatics · Samudra University", font=ft(16, True), fill=INK)
    result.append((im, links))

    return result


def escape_pdf(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def save_pdf(pages, path):
    objects = [None, None, None]  # Catalog, Pages tree, then page objects.
    page_ids = []
    for _ in pages:
        page_ids.append(len(objects))
        objects.append(None)
    objects[1] = b"<< /Type /Catalog /Pages 2 0 R >>"
    objects[2] = ("<< /Type /Pages /Kids [" + " ".join(f"{p} 0 R" for p in page_ids) + f"] /Count {len(page_ids)} >>").encode()

    for i, (im, links) in enumerate(pages):
        image = BytesIO()
        im.save(image, format="JPEG", quality=92, optimize=True)
        image_data = image.getvalue()
        img_id = len(objects)
        objects.append(f"<< /Type /XObject /Subtype /Image /Width {W} /Height {H} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(image_data)} >>\nstream\n".encode() + image_data + b"\nendstream")
        stream = b"q\n960 0 0 540 0 0 cm\n/Im0 Do\nQ\n"
        stream_id = len(objects)
        objects.append(f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"endstream")
        annotation_ids = []
        for (left, top, right, bottom), url in links:
            sx, sy = PAGE_W / W, PAGE_H / H
            rect = (left * sx, PAGE_H - bottom * sy, right * sx, PAGE_H - top * sy)
            annotation_ids.append(len(objects))
            objects.append((f"<< /Type /Annot /Subtype /Link /Rect [{rect[0]:.2f} {rect[1]:.2f} {rect[2]:.2f} {rect[3]:.2f}] /Border [0 0 0] /A << /S /URI /URI ({escape_pdf(url)}) >> >>").encode())
        annots = " /Annots [" + " ".join(f"{a} 0 R" for a in annotation_ids) + "]" if annotation_ids else ""
        objects[page_ids[i]] = (f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] /Resources << /XObject << /Im0 {img_id} 0 R >> >> /Contents {stream_id} 0 R{annots} >>").encode()

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for object_id, obj in enumerate(objects[1:], 1):
        offsets.append(len(out))
        out.extend(f"{object_id} 0 obj\n".encode())
        out.extend(obj)
        out.extend(b"\nendobj\n")
    xref = len(out)
    out.extend(f"xref\n0 {len(objects)}\n0000000000 65535 f \n".encode())
    for offset in offsets[1:]:
        out.extend(f"{offset:010d} 00000 n \n".encode())
    out.extend(f"trailer\n<< /Size {len(objects)} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    path.write_bytes(out)


if __name__ == "__main__":
    save_pdf(make_pages(False), PUBLIC / "portfolio-cut-azizah-zahra.pdf")
    save_pdf(make_pages(True), PUBLIC / "portfolio-cut-azizah-zahra-en.pdf")
