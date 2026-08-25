import os
import time
import json
import urllib.request
import urllib.parse

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN غير موجود")

    API = f"https://api.telegram.org/bot{TOKEN}"


    def send_message(chat_id, text):
        data = urllib.parse.urlencode({
                "chat_id": chat_id,
                        "text": text
                            }).encode()

                                url = f"{API}/sendMessage"

                                    with urllib.request.urlopen(
                                            urllib.request.Request(url, data=data),
                                                    timeout=40
                                                        ) as response:
                                                                return json.loads(response.read())


                                                                def get_updates(offset=None):
                                                                    url = f"{API}/getUpdates"

                                                                        if offset is not None:
                                                                                url += "?" + urllib.parse.urlencode({
                                                                                            "offset": offset,
                                                                                                        "timeout": 30
                                                                                                                })

                                                                                                                    with urllib.request.urlopen(url, timeout=40) as response:
                                                                                                                            return json.loads(response.read())


                                                                                                                            def main():
                                                                                                                                print("eSIM Bot is running...")

                                                                                                                                    offset = None

                                                                                                                                        while True:
                                                                                                                                                try:
                                                                                                                                                            result = get_updates(offset)

                                                                                                                                                                        for update in result.get("result", []):
                                                                                                                                                                                        offset = update["update_id"] + 1

                                                                                                                                                                                                        message = update.get("message")

                                                                                                                                                                                                                        if not message:
                                                                                                                                                                                                                                            continue

                                                                                                                                                                                                                                                            chat_id = message["chat"]["id"]
                                                                                                                                                                                                                                                                            text = message.get("text", "")

                                                                                                                                                                                                                                                                                            if text == "/start":
                                                                                                                                                                                                                                                                                                                send_message(
                                                                                                                                                                                                                                                                                                                                        chat_id,
                                                                                                                                                                                                                                                                                                                                                                "أهلاً بك 👋\nالبوت يعمل بنجاح."
                                                                                                                                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                        send_message(
                                                                                                                                                                                                                                                                                                                                                                                                                                                chat_id,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        f"وصلتني رسالتك:\n{text}"
                                                                                                                                                                                                                                                                                                                                                                                                                                                              )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("Error:", e)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            time.sleep(5)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                main()