import streamlit as st
from PIL import Image
import os

# カレントディレクトリを取得して表示（デバッグ用）
current_dir = os.getcwd()
#st.write('Current directory:', current_dir)

st.title('好きな映画')

st.write('Display Image')
img_path = '/Users/onoderakyoko/0327/topgun.jpg'  
img = Image.open(img_path)
st.image(img, caption='マーベリック！', use_column_width=False, width=300)

option = st.slider(
    'この映画をどのくらい好きですか、',
    min_value=1, max_value=10, value=5
)
'あなたの評価は、', option, 'です。'