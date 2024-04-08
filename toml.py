import streamlit as st
from PIL import Image
import os
import toml

# TOMLファイルからパスワード等の情報を読み込む
current_dir = os.path.dirname(os.path.abspath(__file__))
toml_file_path = os.path.join(current_dir, "main.toml")
config = toml.load(toml_file_path)

# ユーザー名とパスワードの入力
username = st.text_input("Username")
password = st.text_input("Password")

# ユーザー入力と比較してアクセス制限をかける
if username == config["database"]["user"] and password == config["auth"]["password"]:
    st.title("Welcome to the app!")
else:
    st.error("Invalid username or password")
    st.stop()
＝＝

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