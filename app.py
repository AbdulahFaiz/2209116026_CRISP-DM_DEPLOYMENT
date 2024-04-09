import streamlit as st
import pandas as pd
from streamlit_option_menu import *
from function import *


df = pd.read_csv('https://raw.githubusercontent.com/AbdulahFaiz/Data-Mining/main/Data%20Cleaned2.csv')

st.title("Prediksi Cuaca")
st.write(df)


with st.sidebar :
    selected = option_menu('Prediksi Cuaca',['Data Distribution','Relation','Composition & Comparison','Predict'],default_index=0)



if (selected == 'Data Distribution'):
    st.header("Data Distribution")
    scatter_plot(df)
    st.subheader("Dari plot, kita dapat mengamati beberapa hal:")
    st.write("- Data cenderung berkumpul dan menunjukkan pola penyebaran yang menukik dari kiri atas ke kanan bawah. Ini menunjukkan adanya tren dimana suhu yang lebih tinggi berkorelasi dengan kelembaban yang lebih rendah, dan sebaliknya.")
    st.write("- Data untuk 'Ch Rendah' (hijau) tampaknya berkumpul di area dengan kelembaban yang lebih rendah dan suhu yang lebih tinggi.")
    st.write("- Data untuk 'Ch Tinggi' (oranye) lebih sering ditemukan pada suhu yang lebih rendah dan kelembaban rata-rata yang lebih tinggi.")
    st.write("- Data untuk 'Ch Sedang' (biru) tersebar di seluruh area plot, menunjukkan bahwa untuk kelembaban dan suhu rata-rata, curah hujan dapat bervariasi di kategori sedang.")
    st.write("- Ada beberapa outlier atau titik data yang tidak mengikuti pola umum, misalnya, beberapa titik yang menunjukkan kelembaban sangat tinggi namun dengan kategori curah hujan rendah.")
    
if (selected == 'Relation'):
    st.title('Relations')
    heatmap(df)
    st.subheader("Dari plot, kita dapat mengamati beberapa hal:")
    st.write("- Fitur temp_rata-rata memiliki korelasi negatif yang kuat dengan lembab_rata-rata, yang ditunjukkan oleh warna biru gelap dengan nilai korelasi -0.79. Ini berarti bahwa seiring dengan peningkatan nilai temperatur rata-rata, kelembaban rata-rata cenderung menurun, dan sebaliknya.")
    st.write("- Fitur ch memiliki korelasi yang sangat rendah dengan fitur-fitur lainnya, dengan nilai yang mendekati 0, yang menunjukkan bahwa tidak ada hubungan yang signifikan antara ch dengan fitur-fitur tersebut.")
    st.write("- Fitur cahaya_jam memiliki korelasi positif yang tinggi dengan curah_hujan_kategori dengan nilai 0.98, menunjukkan bahwa ada hubungan yang kuat dan positif antara jumlah cahaya dalam sehari dengan kategori curah hujan.")

if (selected == 'Composition & Comparison'):
    st.title('Composition')
    compositionAndComparison(df)
    st.write("Dari heatmap bisa kita lihat bahwa untuk Tahun, bulan, tanggal nilai tampaknya konstan di semua kategori curah hujan. Namun, terdapat variasi untuk suhu rata-rata, kelembaban rata-rata, dan jam cahaya matahari antara kategori. Misalnya, untuk kelembaban rata-rata dan cahaya jam, nilai meningkat dari kategori rendah ke tinggi.")

if (selected == 'Predict'):
    st.title('Let\'s Predict!')
    Predict()