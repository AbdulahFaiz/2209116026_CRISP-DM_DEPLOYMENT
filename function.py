import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pickle


# Fungsi untuk membuat scatter plot
def scatter_plot(df):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)

    categories = {
        0: "Ch Rendah",
        1: "Ch Sedang",
        2: "Ch Tinggi"
    }

    # Membuat scatter plot
    for category_label in df['curah_hujan_kategori'].unique():
        category_df = df[df['curah_hujan_kategori'] == category_label]
        ax.scatter(category_df['temp_rata-rata'], category_df['lembab_rata-rata'], label=categories[category_label])

    ax.set_xlabel('Suhu rata-rata')
    ax.set_ylabel('Kelembaban Rata-rata')
    ax.set_title("Distribusi Data Berdasarkan Kategori Curah Hujan")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# Load data dari URL
df = pd.read_csv('https://raw.githubusercontent.com/AbdulahFaiz/Data-Mining/main/Data%20Cleaned2.csv')

# Membuat scatter plot
scatter_plot(df)


# Fungsi untuk membuat heatmap
def heatmap(df):
    df2 = df.drop(['Thn', 'bln', 'tgl'], axis=1)  # Drop kolom non-numerik
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df2.corr(), annot=True, cmap='coolwarm', ax=ax)
    plt.title('Korelasi Antara Fitur Numerik')
    st.pyplot(fig)

# Load data dari dataset
df = pd.read_csv('https://raw.githubusercontent.com/AbdulahFaiz/Data-Mining/main/Data%20Cleaned2.csv')

# Membuat heatmap
heatmap(df)


# Fungsi untuk menghitung komposisi dan perbandingan fitur
def compositionAndComparison(df):
    # Ganti nilai kategori curah hujan menjadi kategori yang sesuai
    df['curah_hujan_kategori'].replace({0: 'rendah', 1: 'sedang', 2: 'tinggi'}, inplace=True)
    # Hitung rata-rata fitur untuk setiap kategori curah hujan
    curah_hujan_composition = df.groupby('curah_hujan_kategori').mean()
    # Plot komposisi kategori curah hujan
    plt.figure(figsize=(10, 6))
    sns.heatmap(curah_hujan_composition.T, annot=True, cmap='YlGnBu')
    plt.title('Komposisi untuk setiap kategori curah hujan')
    plt.xlabel('Kategori Curah Hujan')
    plt.ylabel('Fitur')
    st.pyplot(plt)

# Load data dari dataset
df = pd.read_csv('https://raw.githubusercontent.com/AbdulahFaiz/Data-Mining/main/Data%20Cleaned2.csv')

# Membuat komposisi dan perbandingan fitur dengan kategori curah hujan
compositionAndComparison(df)

def Predict():
    Thn = st.number_input('Tahun', min_value=2022, max_value=2023)
    bln = st.number_input('Bulan', min_value=1, max_value=12)
    tgl = st.number_input('Tanggal', min_value=1, max_value=31)
    temp_rata_rata = st.number_input('Rata-rata Temperatur', min_value=0.0, max_value=100.0)
    lembab_rata_rata = st.number_input('Rata-rata Kelembaban', min_value=0.0, max_value=100.0)
    ch = st.number_input('Curah Hujan', min_value=0.0, max_value=100.0)
    cahaya_jam = st.number_input('Cahaya Jam', min_value=0.0, max_value=100.0)

    # Membuat DataFrame user_data
    user_data = pd.DataFrame({
        'Thn': [Thn],
        'bln': [bln],
        'tgl': [tgl],
        'temp_rata-rata': [temp_rata_rata],
        'lembab_rata-rata': [lembab_rata_rata],
        'ch': [ch],
        'cahaya_jam': [cahaya_jam],
        'curah_hujan_kategori': [None]  # Kolom ini akan diisi setelah prediksi
    })

    st.subheader('Data Pengguna:')
    st.write(user_data)

    button = st.button('Predict')
    if button:
        with open('gnb.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        # Melakukan prediksi kategori curah hujan
        predicted_kategori_curah_hujan = loaded_model.predict(user_data.drop('curah_hujan_kategori', axis=1))

        if predicted_kategori_curah_hujan == 0:
            st.write("Kategori Curah Hujan: Rendah")
        elif predicted_kategori_curah_hujan == 1:
            st.write("Kategori Curah Hujan: Sedang")
        elif predicted_kategori_curah_hujan == 2:
            st.write("Kategori Curah Hujan: Tinggi")
