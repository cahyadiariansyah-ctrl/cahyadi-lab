import streamlit as st

def tampil2():
    st.header("🔢 Kuis Angka Penting - Cahyadi Ariansah")

    soal = "Berapa jumlah angka penting pada nilai 0.00450?"
    opsi = ["2", "3", "4"]
    jawaban = st.radio(soal, opsi)

    if st.button("Periksa"):
        if jawaban == "3":
            st.success("Benar, selamat terus tingkatkan belajar mu 🎉")
        else:
            st.error("salah, anda harus belajar lagi")


    st.caption("Kuis ini disusun oleh Cahyadi Ariansah")

