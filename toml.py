import streamlit as st
from PIL import Image
import os
import toml


# TOMLファイルからパスワード等の情報を読み込む
config = toml.load("config.toml")
password = os.environ.get("DB_TOKEN")

# ユーザー入力と比較してアクセス制限をかける
if st.text_input("Password") != password:
    st.error("Invalid password")
    st.stop()

# パスワードが正しい場合はアプリの通常の処理を実行する
st.title("Welcome to the app!")


# カレントディレクトリを取得して表示（デバッグ用）
current_dir = os.getcwd()
#st.write('Current directory:', current_dir)

# ここから前のデータ
st.title('好きな映画')

st.write('Display Image')

# 相対パスの例
img_path = "topgun.jpg"
img = Image.open(img_path)
st.image(img, caption='マーベリック！', use_column_width=False, width=300)

option = st.slider(
    'この映画をどのくらい好きですか、',
    min_value=1, max_value=10, value=5
)
'あなたの評価は、', option, 'です。'
