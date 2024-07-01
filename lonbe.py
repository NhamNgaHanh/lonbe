import streamlit as st
import pandas as pd
import io
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
st.set_page_config(
    page_title="Trang Chủ",
    page_icon="💯",
    #initial_sidebar_state = "expanded"
    layout= "wide",
    initial_sidebar_state = "collapsed",
)
# Đọc dữ liệu từ file Excel
df = pd.read_excel("./Book1.xlsx")
sf = pd.read_excel("./result.xlsx")
excel_file = "result.xlsx"
excel_file1 = "Book1.xlsx"
# Khai báo giá trị k để so sánh
def write_to_excel(ks, row, d, excel_file):
    row1 = row + 1
    ab = st.session_state.get("ex", None)
    gf = pd.DataFrame([ab])
    with pd.ExcelWriter(excel_file, mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
        gf.to_excel(writer, startrow=row1, startcol=d, index=False, header=False)
    return
if st.button("Cập nhật dữ liệu"):
    today = datetime.now()
    st.subheader(df.iloc[0, 0])
    time = str(today - df.iloc[0, 0])
    time1 = int(str(time[:2]))
    st.write(time1)
    if time1 > 1:
        maeday = str(df.iloc[0, 0])
        date_object1 = datetime.strptime(maeday, '%Y-%m-%d %H:%M:%S')
        date_object2 = date_object1 + timedelta(days=1)
        maeday2 = str(date_object2)
        maeday1 = maeday2[:10]
        date_object = datetime.strptime(maeday1, '%Y-%m-%d')
        new_date_string = date_object.strftime('%d-%m-%Y')
        url = 'https://3ketqua.net/xo-so-mien-bac.php?ngay='+new_date_string
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        elements_with_id = soup.find(id='rs_0_0')
        div_text = elements_with_id.text
        new_row = {}
        new_row_df = pd.DataFrame([new_row])
        kf = pd.concat([df.iloc[:0], new_row_df, df.iloc[0:]], ignore_index=True)
        kf.to_excel(excel_file1, index=False)
        ks = date_object
        st.session_state["ex"] = ks
        write_to_excel(ks, 0, 0, excel_file1)
        ks1 = int(div_text)
        st.session_state["ex"] = ks1
        write_to_excel(ks1, 0, 1, excel_file1)
#nd = int(st.number_input("Độ dài của cầu",step = 1))
kd = int(st.number_input("Chọn ngày trong tháng:", step = 1))
nd = int(st.number_input("Độ dài của cầu:", step = 1))
sn = int(st.number_input("Chọn số ngày bạn muốn kiểm tra:", step = 1))
st.subheader(df.iloc[kd, 0])
st.subheader(df.iloc[kd, 1])
st.subheader(len(df))
bd = 1
#nd = 3
col1, col2 = st.columns([0.5,0.5])
with col2:
    st.header(f":red[Cầu ] {nd}")
    num_r = []
    numx = []
    numy = []
    num_d = []
    if nd >= 2:
        for u in range(0, nd):
            x_u = str(int(df.iloc[u+kd, 1]))[-2:]
            numx.append(x_u)
            if int(x_u) >= 50:
                x_u = 1
                numy.append(x_u)
            else:
                x_u = 0
                numy.append(x_u)
    st.write(str(numx))
    st.write(str(numy))
    if nd >= 2:
        kml = kd + 1
        dv = int(str(int(df.iloc[kd, 1]))[-2:])
        for i in range(kml,sn):
            l = int(str(int(df.iloc[i, 1]))[-2:])  # Lấy hai ký tự cuối cùng của giá trị và chuyển thành chuỗi
            if l >=50:
                l = 1
            else:
                l = 0
            if l == int(numy[0]):
                for p in range(1,nd):
                    l_p = int(str(int(df.iloc[i + p, 1]))[-2:])
                    if l_p >= 50:
                        l_p = 1
                    else:
                        l_p = 0
                    if l_p == int(numy[p]):
                        if p == nd-1:
                            num_r.append(str(int(df.iloc[i - 1, 1]))[-2:])
                    else:
                        break
    tl = len(num_r)
    st.subheader(f":blue[Số cầu ra là: {tl}]")
    lon = 0
    be = 0
    for nu in range(0,tl):
        kh = int(num_r[nu])
        if kh > 50:
            lon = lon + 1
        else:
            be = be + 1
    if tl != 0:
        st.subheader(f":red[Tỉ lệ ra lớn là: {round((lon/tl)*100,2)}%]")
        st.subheader(f":red[Tỉ lệ ra bé là: {round((be / tl) * 100, 2)}%]")
        #st.write( round((lon/tl)*100,2))
        #st.write( round((be / tl) * 100, 2))
    num_r = []
    num_d = []
with col1:
    st.image("images.jpg")
