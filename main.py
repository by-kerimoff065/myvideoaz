import json
import time

# Config faylını oxumaq
def read_config():
    with open("config.json", "r") as file:
        config = json.load(file)
    return config

# Config faylını yeniləmək
def update_config(config):
    config["tms"] = int(time.time())  # Cari vaxtı yenilə
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

# Yeni link yaratmaq
def generate_stream_url(config):
    url = f"{config['base_url']}?tkn={config['token']}&tms={config['tms']}"
    return url

# Linki fayla yazmaq
def save_link_to_file(stream_url):
    with open("stream_link.txt", "w") as file:
        file.write(stream_url)
    print("Yeni yayım linki:", stream_url)

# Skripti işə salmaq
if __name__ == "__main__":
    config = read_config()
    update_config(config)  # Config faylını yenilə
    stream_url = generate_stream_url(config)
    save_link_to_file(stream_url)
