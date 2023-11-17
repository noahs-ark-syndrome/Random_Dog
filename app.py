# 以下を「app.py」に書き込み

import streamlit as st
import requests

top_image = st.secrets.Top_Image.top_image


def download_image(url, file_path):
    """
    url: ダウンロードの元になるURL
    file_path: 保存先のファイルパス
    """
    r = requests.get(url, stream = True)

    if r.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(r.content)

def main():
    api_url = "https://dog.ceo/api/breeds/image/random"
    r = requests.get(api_url)
    data = r.json()

    image_url = data["message"]

# ユーザーインターフェイスの構築
st.title("ランダムわんこ")
st.image("top_image")
st.write("いろんなわんこをお見せしましょう")
if st.button("わん！"):
    st.image(image_url)

if __name__ == "__main__":
    main()
