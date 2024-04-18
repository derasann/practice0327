import streamlit as st
from PIL import Image
import os
import toml

# TOMLファイルからパスワード等の情報を読み込む
current_dir = os.path.dirname(os.path.abspath(__file__))
toml_file_path = os.path.join(current_dir, "main.toml")
config = toml.load(toml_file_path)

# パスワードの入力
entered_password = st.text_input("Password", type="password")

# ユーザー入力と比較してアクセス制限をかける
auth_token = st.secrets["auth_key"]
#auth_token = st.secrets.auth_key
if entered_password.strip() == auth_token:
    # 認証成功時の処理
    st.title("Welcome to the app!")
    
    # ここから好きな映画の表示
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
    st.write(f'あなたの評価は、{option} です。')
else:
    if entered_password:
        st.error("Invalid password")
