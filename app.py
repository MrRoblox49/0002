import streamlit as st

# ตั้งค่าหน้าเว็บเบื้องต้น
st.set_page_config(page_title="My Streamlit App", page_icon="🎈")

# ส่วนแสดงข้อความ
st.title("Hello, World!")
st.write("เว็บแอปนี้รันอยู่บน Streamlit Community Cloud")

# สร้างตัวแปรเก็บจำนวนการกดปุ่ม (ใช้ session_state เพื่อจำค่าไว้เมื่อหน้ารีเฟรช)
if 'count' not in st.session_state:
    st.session_state.count = 0

# สร้างปุ่มกด
if st.button("Click Me"):
    st.session_state.count += 1

# แสดงผลการกดปุ่ม
if st.session_state.count > 0:
    st.success(f"Button clicked {st.session_state.count} time(s)!")