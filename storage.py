import json
import os

#json檔案路徑
STORAGE_FILE="user_city.json"

#載入檔案
def load_file():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE,"r",encoding="utf-8") as file:
        return json.load(file)
    
#儲存資料到json
def save_file(data):
    with open(STORAGE_FILE,"w",encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False,indent=4)

#設定使用者常用城市
def set_city(user_id,city):
    data=load_file()
    #更新會新增使用者城市
    data[user_id] = city
    save_file(data)

#取得常用城市
def get_city(user_id):
    data = load_file()
    return data.get(user_id)