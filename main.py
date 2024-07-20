from httpx import Client

import os

from pypresence import Presence

from time import sleep

BASE_API_URL: str = "https://api.music.yandex.net"

FAKE_USERAGENT: str = "os=Windows.Desktop; os_version=1337; manufacturer=0; model=0; clid=0; device_id=0; uuid=0"

DISCORD_RPC: Presence = Presence(1263992019018055691)

def get_current_track() -> dict:
    queue: list = client.get(f"{BASE_API_URL}/queues").json()["result"]["queues"]

    if(len(queue) > 0):
        queue_data: dict =  client.get(f"{BASE_API_URL}/queues/{queue[0]['id']}").json()["result"]
        current_index: int = queue_data["currentIndex"]

        current_track: int = queue_data["tracks"][current_index]["trackId"]

        track_data: dict =  client.post(f"{BASE_API_URL}/tracks", data = {
            "trackIds": [
                current_track
            ]
        }).json()["result"][0]

        author_list: list = [

        ]

        for author in track_data["artists"]:
            author_list.append(author['name'])

        return {
            "authors": author_list,
            "title": track_data["title"],
            "cover": f"https://{track_data['coverUri'].replace('%%', '200x200')}"
        }

if __name__  == "__main__":
    DISCORD_RPC.connect()

    if(not os.path.exists("access_token")):
        open("access_token", "w").close()

        print("""В открытой директории был создан файл \"access_token\".
              
Для дальнейшей работы скрипта вставь API-Токен от аккаунта Яндекс.Музыки.""")
        
        exit()

    with open("access_token", "r", encoding = "utf-8") as f:
        access_token: str =  f"OAuth {f.read()}"

    client: Client = Client(
        headers = {
            "Authorization": access_token,
            "X-Yandex-Music-Device": FAKE_USERAGENT
        }
    )

    while True:
        track_data: dict = get_current_track()

        if(track_data):
            DISCORD_RPC.update(
                state = ", ".join(track_data["authors"]),
                details = track_data["title"],
                large_image = track_data["cover"],
                small_image = "logo",
                large_text = "Сейчас играет"
            )

        sleep(5)