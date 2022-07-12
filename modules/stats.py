import json
import collections
import pandas as pd
from vk_api import VkUpload
from vk_api.utils import get_random_id
from datetime import datetime, timedelta

class Stats():
    def __init__(self, vk, event):
        next_day_raw = datetime.now() + timedelta(days=1)
        next_day = int(next_day_raw.strftime("%d%m%Y"))

        i = vk.messages.search(peer_id=event.obj.message["peer_id"], date=next_day, q="")

        offset_count = 0

        initial_search = vk.messages.search(peer_id=event.obj.message["peer_id"], date=next_day, q="", offset=offset_count, count=100)

        all_messages = [initial_search["items"]]

        while offset_count < i["count"]:
            offset_count = offset_count + 100
            try:
                parsed_json = vk.messages.search(peer_id=event.obj.message["peer_id"], date=next_day, q="", offset=offset_count, count=100)
                all_messages.append(parsed_json["items"])
            except Exception as e:
                print(e)
                print("Всьо)")
                break

        with open("stats/all_messages.json", "w", encoding="utf-8") as f:
            x = json.dump(all_messages, f, ensure_ascii=False, indent=4)

        with open("stats/all_messages.json") as f:
            all_messages = json.load(f)

        members_stats_raw = []

        for i in all_messages:
            for n in i:
                members_stats_raw.append(n["from_id"])

        self.members_stats = collections.Counter(members_stats_raw).most_common()

    def main(self, vk, event, vk_session):
        stats_df = pd.DataFrame(self.members_stats, columns=["Имя", "Статистика"], index=[i[0] for i in self.members_stats])

        for i in stats_df["Имя"]:
            try:
                id = i

                user_get=vk.users.get(user_ids = (id))

                user_get=user_get[0]
                first_name=user_get["first_name"]
                last_name=user_get["last_name"]
                full_name=first_name+" "+last_name

                stats_df["Имя"] = stats_df["Имя"].replace(i, full_name)
            except IndexError:
                stats_df["Имя"] = stats_df["Имя"].replace(i, "бот манул)")

        stats_df = stats_df.set_index(stats_df["Имя"])

        plot = stats_df.plot.pie(y="Статистика", figsize=(12,12))
        fig = plot.get_figure()
        fig.savefig("stats/output.png")

        stats_df = stats_df[0:]
        stats_df = stats_df.to_string(index=None)

        vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                        message=f"Статистика по конфачерам: \n {stats_df}")

        upload = VkUpload(vk_session)
        photo = upload.photo_messages(photos = "stats/output.png")
        vk_photo_url = "photo{}_{}".format(photo[0]["owner_id"], photo[0]["id"])

        vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                        attachment=vk_photo_url)