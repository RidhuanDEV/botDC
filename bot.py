import requests
import datetime
import time

# Gantilah YOUR_TOKEN dengan token Discord kamu
YOUR_TOKEN = ''
channel_id = ['']  # Gantilah dengan ID channel Discord yang kamu tuju
# log_file = "/home/username/message_log1.txt"

# def log_message(status, message):
#     with open(log_file, "a") as file:
#         time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         file.write(f"[{time_stamp}] {status}: {message}\n")

def send_message(token, channel_id, message):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "content": message
    }

    while True:  # Loop untuk mencoba mengirim pesan hingga sukses
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            print("Pesan berhasil dikirim!")
            # log_message("SUCCESS", message)
            break  # Keluar dari loop jika pesan terkirim
        elif response.status_code == 429:
            error_data = response.json()
            retry_after = error_data.get("retry_after", 30)  # Gunakan waktu tunggu yang disarankan atau default 30 detik
            print(f"Rate limit error, menunggu {retry_after} detik sebelum mencoba lagi...")
            # log_message("FAILED", f"Error 429 - Retry after {retry_after} detik")
            time.sleep(retry_after)  # Tunggu sesuai waktu retry yang diberikan oleh Discord API
        else:
            error_message = f"Error: {response.status_code} - {response.text}"
            print(error_message)
            # log_message("FAILED", error_message)
            break  # Keluar dari loop jika terjadi error selain 429

# Contoh penggunaan
pesan = "DAW PRO PLAYER DONATE PLS NOOB LOL NOOB LOL NOOOB"

for i in channel_id:
    a = 0
    while a < 10:
        send_message(YOUR_TOKEN, i, pesan)
        a += 1
        time.sleep(10)
