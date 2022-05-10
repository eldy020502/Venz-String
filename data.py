from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🔄 Return Home 🔄", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Status Bot dan Bot Lainnya ✨", url="https://t.me/venzproject/132")],
        [
            InlineKeyboardButton("Cara Penggunaan ❔", callback_data="help"),
            InlineKeyboardButton("🤔 Tentang 🤔", callback_data="about")
        ],
        [InlineKeyboardButton("🔥 Bot Keren Lainnya 🔥", url="https://t.me/venzproject")],
    ]

    START = """
Hey {}

Welcome to {}

Jika Anda tidak mempercayai bot ini,
1) berhenti membaca pesan ini
2) hapus obrolan ini

Masih membaca?
Anda dapat menggunakan saya untuk menghasilkan pyrogram (bahkan versi 2) dan sesi string telethon. Gunakan tombol di bawah ini untuk mempelajari lebih lanjut !

By @venzproject
    """

    HELP = """
✨ **Perintah yang tersedia** ✨

/about - Tentang Bot
/help - Pesan ini
/start - Mulai Bot
/generate - Hasilkan Sesi
/cancel - Batalkan proses
/restart - Batalkan proses
"""

    ABOUT = """
**Tentang Bot Ini** 

Telegram Bot untuk menghasilkan sesi string Pyrogram dan Telethon oleh @venzproject

Kode sumber : [Click Here](https://github.com/eldy020502/Venz-String)

Kerangka : [Pyrogram](https://docs.pyrogram.org)

Bahasa : [Python](https://www.python.org)

Pengembang : @moonscrsh
    """
