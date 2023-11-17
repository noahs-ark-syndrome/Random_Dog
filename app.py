import streamlit as st
import requests


def main():
    api_url = "https://dog.ceo/api/breeds/image/random"
    r = requests.get(api_url)
    data = r.json()

    image_url = data["message"]

# ユーザーインターフェイスの構築
st.title("ランダムわんこ")
st.image("https://th.bing.com/th/id/OIG.Byw03p.SxchBtY6HtdH1?pid=ImgGn")
st.write("いろんなわんこをお見せしましょう")
if st.button("わん！"):
    main()
    st.image(data["message"])
