import flet as ft
import requests
from datetime import datetime
import random
import threading

# --- KONFIGURASI ---
URL_APPS_SCRIPT = "https://script.google.com/macros/s/AKfycbwLk_OWo1_BaJYaIpQvd78irmthnaHmNlMgII-HI1NrqzFIO-3uNXXoN7tqBm0-95-rIg/exec"

DB_PEGAWAI = {
    "1": {"nama": "Suwanto", "sheet": "Suwanto", "nip": "19720521 200912 1 001", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "2": {"nama": "Wawan Setiawan", "sheet": "Wawan Setiawan", "nip": "19860601 201012 1 004", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "3": {"nama": "Ineke Setiyaningsih", "sheet": "Ineke Setiyaningsih", "nip": "19831003 200912 2 001", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "4": {"nama": "Farah Agustina Setiawati", "sheet": "Farah Agustina Setiawati", "nip": "19840828 201012 2 003", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "5": {"nama": "Rusma Ariati", "sheet": "Rusma Ariati", "nip": "19840621 201101 2 013", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "6": {"nama": "Ahmad Erwan Rifani", "sheet": "Ahmad Erwan Rifani", "nip": "19830829 200811 1 001", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "7": {"nama": "Syaiful Anwar", "sheet": "Syaiful Anwar", "nip": "19741127 200710 1 001", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "8": {"nama": "Zainal Hilmi Yustan", "sheet": "Zainal Hilmi Yustan", "nip": "19821025 200701 1 003", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "9": {"nama": "Najmi Hidayati", "sheet": "Najmi Hidayati", "nip": "19850608 200701 2 003", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "10": {"nama": "Jainal Abidin", "sheet": "Jainal Abidin", "nip": "19820712 200910 1 001", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "11": {"nama": "Suci Lestari", "sheet": "Suci Lestari", "nip": "19850108 201012 2 006", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "12": {"nama": "Athaya Insyira Khairani", "sheet": "Athaya Insyira Khairani", "nip": "20010712 202506 2 017", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "13": {"nama": "Muhammad Ibnu Fahmi", "sheet": "Muhammad Ibnu Fahmi", "nip": "20010608 202506 1 007", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "14": {"nama": "Alfian Ridhani", "sheet": "Alfian Ridhani", "nip": "19950903 202506 1 005", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "15": {"nama": "Muhammad Aldi Hudaifi", "sheet": "Muhammad Aldi Hudaifi", "nip": "20010121 202506 1 007", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "16": {"nama": "Firda Aulia", "sheet": "Firda Aulia", "nip": "20020415 202506 2 007", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "17": {"nama": "Sya'bani Rona Baika", "sheet": "Sya'bani Rona Baika", "nip": "19920207 202421 2 044", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "18": {"nama": "Apriadi Rakhman", "sheet": "Apriadi Rakhman", "nip": "19890422 202421 1 013", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "19": {"nama": "M Satria Maipadly", "sheet": "M Satria Maipadly", "nip": "19890526 202421 1 016", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "20": {"nama": "Basuki Rahmat", "sheet": "Basuki Rahmat", "nip": "19770502 202421 1 007", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "21": {"nama": "Sulaiman", "sheet": "Sulaiman", "nip": "19841122 202421 1 010", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "22": {"nama": "Saldoz Yedi", "sheet": "Saldoz Yedi", "nip": "19800811 202521 1 019", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "23": {"nama": "Mastoni Ridani", "sheet": "Mastoni Ridani", "nip": "19910601 202521 1 018", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "24": {"nama": "Suriadi", "sheet": "Suriadi", "nip": "19980302 202521 1 005", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "25": {"nama": "Ami Aspihani", "sheet": "Ami Aspihani", "nip": "19820404 202521 1 031", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "26": {"nama": "Abdurrahman", "sheet": "Abdurrahman", "nip": "19881012 202521 1 031", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "27": {"nama": "Emaliani", "sheet": "Emaliani", "nip": "19890622 202521 2 027", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "28": {"nama": "Muhammad Hafiz Rijani", "sheet": "Muhammad Hafiz Rijani", "nip": "19960321 202521 1 031", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "29": {"nama": "Saiful Fahmi", "sheet": "Saiful Fahmi", "nip": "19950617 202521 1 036", "unit": "KPU KAB. HULU SUNGAI SELATAN"},
    "30": {"nama": "Nadianti", "sheet": "Nadianti", "nip": "19990606 202521 2 036", "unit": "KPU KAB. HULU SUNGAI SELATAN"}
}

MOTIVASI = [
    "Jangan tapi dipikirakan banar gawian tu, kaina hancap tuha muha...",
    "Rezeki tu kaya jodoh, dicari ngalih, dihadang kada datang. Ayuja!",
    "Biar dunya baputar hancap, hati ulun tatap diam di wadah pian haja.",
    "Dasar lain mun sudah gajihan nih, tihang listrik gin dilihumi."
    # ... (tambahkan sisanya dari daftar motivasi tadi)
]

def main(page: ft.Page):
    page.title = "KPU HSS - V.1.5"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1a0404"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # State Variables
    mon_data = {}

    # --- FUNCTIONS ---
    def fetch_monitoring():
        nonlocal mon_data
        try:
            r = requests.get(URL_APPS_SCRIPT, timeout=10)
            mon_data = r.json()
            render_monitoring()
        except:
            pass

    def check_id(e):
        p = DB_PEGAWAI.get(txt_id.value)
        if p:
            container_nama.content = ft.Text(f"Nama: {p['nama']}", color="yellow", weight="bold")
            container_nama.visible = True
        else:
            container_nama.visible = False
        validate_piket(None)
        page.update()

    def validate_piket(e):
        now = datetime.now()
        is_weekend = now.weekday() >= 5
        p = DB_PEGAWAI.get(txt_id.value)
        
        can_send = True
        msg = ""

        if is_weekend and p:
            u_info = mon_data.get(p["sheet"], {})
            is_piket_now = "PIKET" in str(u_info.get("status", "")).upper()
            
            if dd_jenis.value == "Masuk":
                if dd_status.value not in ["Piket Pagi", "Piket Malam"]:
                    can_send = False
                    msg = "Hari Libur. Masuk hanya untuk PIKET."
            elif dd_jenis.value == "Pulang":
                if not is_piket_now:
                    can_send = False
                    msg = "Anda belum absen MASUK PIKET hari ini."
        
        btn_kirim.disabled = not can_send
        lbl_error.value = msg
        
        # Sembunyikan field yang tidak perlu
        container_piket.visible = (dd_jenis.value == "Masuk")
        container_pulang.visible = (dd_jenis.value == "Pulang")
        page.update()

    def kirim_data(e):
        p = DB_PEGAWAI.get(txt_id.value)
        if not p: return

        btn_kirim.disabled = True
        btn_kirim.text = "MENGIRIM..."
        page.update()

        now = datetime.now()
        payload = {
            "sheetName": p["sheet"], "jenis": dd_jenis.value, "nama": p["nama"],
            "nip": p["nip"], "unit": p["unit"], "status": dd_status.value if dd_jenis.value == "Masuk" else dd_jenis.value,
            "tanggal": now.strftime("%d/%m/%Y"), "hari": ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"][now.weekday()],
            "uraian": txt_uraian.value, "output": txt_output.value
        }

        try:
            requests.post(URL_APPS_SCRIPT, params=payload, timeout=15)
            # Show Motivation Dialog
            dialog.title = ft.Text("ABSENSI BERHASIL! 🎊")
            dialog.content = ft.Text(f"{p['nama']}\n\n\"{random.choice(MOTIVASI)}\"", text_align="center")
            page.dialog = dialog
            dialog.open = True
            page.update()
            fetch_monitoring()
        except:
            lbl_error.value = "Gagal terhubung ke Spreadsheet!"
            btn_kirim.disabled = False
            btn_kirim.text = "KIRIM DATA ABSENSI"
        page.update()

    # --- UI COMPONENTS ---
    txt_id = ft.TextField(label="🆔 ID PEGAWAI", on_change=check_id, border_color="#5e1515", border_radius=12)
    container_nama = ft.Container(visible=False, bgcolor="#332200", padding=10, border_radius=10)
    
    dd_jenis = ft.Dropdown(
        label="📅 JENIS ABSENSI",
        value="Masuk",
        options=[ft.dropdown.Option(x) for x in ["Masuk", "Pulang", "Cuti", "Izin", "Off"]],
        on_change=validate_piket
    )
    
    dd_status = ft.Dropdown(
        label="📍 STATUS KEHADIRAN",
        value="WFO",
        options=[ft.dropdown.Option(x) for x in ["WFO", "WFH", "Dinas Luar", "Piket Pagi", "Piket Malam"]],
        on_change=validate_piket
    )

    txt_uraian = ft.TextField(label="📋 URAIAN TUGAS", multiline=True)
    txt_output = ft.TextField(label="📦 OUTPUT", multiline=True)
    
    container_piket = ft.Column([dd_status])
    container_pulang = ft.Column([txt_uraian, txt_output], visible=False)
    
    lbl_error = ft.Text("", color="red")
    
    btn_kirim = ft.ElevatedButton(
        "KIRIM DATA ABSENSI",
        bgcolor="red", color="white",
        width=400, height=50,
        on_click=kirim_data
    )

    dialog = ft.AlertDialog(
        actions=[ft.TextButton("Selesai", on_click=lambda _: page.window_close())]
    )

    mon_list = ft.Column(spacing=10)

    def render_monitoring():
        mon_list.controls.clear()
        for i in range(1, 31):
            sid = str(i)
            p = DB_PEGAWAI.get(sid)
            if p:
                inf = mon_data.get(p["sheet"], {"jamMasuk": "-", "jamPulang": "-", "status": "-", "keterangan": "Belum Absen"})
                ket = inf['keterangan'].upper()
                k_clr = "green" if "HADIR" in ket else "red"
                
                mon_list.controls.add(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"{sid}. {p['nama']}", weight="bold", color="yellow"),
                            ft.Row([
                                ft.Column([ft.Text("Masuk", size=10), ft.Text(inf['jamMasuk'], weight="bold")], spacing=2),
                                ft.Column([ft.Text("Pulang", size=10), ft.Text(inf['jamPulang'], weight="bold")], spacing=2),
                                ft.Column([ft.Text("Status", size=10), ft.Text(inf['status'], weight="bold")], spacing=2),
                                ft.Column([ft.Text("Ket", size=10), ft.Text(ket, color=k_clr, weight="bold")], spacing=2),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ]),
                        bgcolor="#2b0606", padding=15, border_radius=15, border=ft.border.all(1, "#5e1515")
                    )
                )
        page.update()

    # --- LAYOUT ---
    page.add(
        ft.Column([
            ft.Text("KPU KABUPATEN HULU SUNGAI SELATAN", size=24, weight="black", color="yellow", text_align="center"),
            ft.Text("O'lia Software Development V.1.5", color="#8a5a5a", text_align="center"),
            ft.Container(
                content=ft.Column([
                    txt_id, container_nama, dd_jenis, container_piket, container_pulang, lbl_error, btn_kirim
                ]),
                padding=20, bgcolor="#250505", border_radius=20, border=ft.border.all(1, "yellow300")
            ),
            ft.Text("MONITORING KEHADIRAN HARI INI", size=18, weight="bold", color="yellow", text_align="center"),
            mon_list
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Start Initial Fetch
    threading.Thread(target=fetch_monitoring, daemon=True).start()

ft.app(target=main)
