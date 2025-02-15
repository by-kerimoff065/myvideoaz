import time

# Token və vaxtı avtomatik yaratmaq
def generate_token():
    token = "IXSGPuL_ozDkr4KJwkXyCA"  # Bu nümunədir, real tokenı əldə etmək üçün API istifadə edin.
    tms = int(time.time())  # Cari vaxtı əldə edirik.
    return token, tms

# Yeni link yaratmaq
def generate_stream_url():
    token, tms = generate_token()
    url = f"https://ecanlitv3.etvserver.com/xazartv.m3u8?tkn={token}&tms={tms}"
    return url

# Linki fayla yazmaq
def save_link_to_file():
    stream_url = generate_stream_url()
    with open("stream_link.txt", "w") as file:
        file.write(stream_url)
    print("Yeni yayım linki:", stream_url)

# Skripti işə salmaq
if __name__ == "__main__":
    save_link_to_file()
