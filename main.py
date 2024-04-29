import streamlit as st    
import numpy as np
import pandas as pd     
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('写真.png')
    st.image(img,caption='Jun Ago', use_column_width=True)


st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration (i+1)')
    bar.progress(i +1)
    time.sleep(0.1)

'Done!!!'




option = st.sidebar.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'

st.write('Interactive Widgets')

left_column, right_column =st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')

option = st.text_input('あなたの趣味を教えて下さい')
'あなたの趣味:', option, 'です。'


condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition





st.write('Dataframe')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.dataframe(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項


```python
import streamlit as st    
import numpy as np
import pandas as pd   
"""

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)


df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.map(df2)

