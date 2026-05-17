import os
import pandas as pd
import streamlit as st

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(page_title="Katalog Bunga", layout="wide")

# 1. Tampilkan Banner Utama
if os.path.exists("anggrekku.png"):
    st.image("anggrekku.png", use_container_width=True)

st.title("🌸 Koleksi Bouquet Bunga Berdasarkan Kategori")
st.divider()

# ==========================================
# MEMBACA & MENAMPILKAN DATA KATALOG
# ==========================================
try:
    if os.path.exists("website_bunga/data_bunga.csv"):
        df = pd.read_csv("website_bunga/data_bunga.csv")
        df = df.dropna(subset=["foto"])

        daftar_kategori = df["kategori"].unique()

        for kat in daftar_kategori:
            st.header(f"🌿 Jenis {kat.capitalize()}")
            data_per_kat = df[df["kategori"] == kat]

            # Membuat layout 4 kolom untuk produk
            cols = st.columns(4)

            for index, row in data_per_kat.reset_index().iterrows():
                nama_foto = str(row["foto"]).strip()

                with cols[index % 4]:
                    foto_lengkap = f"website_bunga/{nama_foto}"
                    if os.path.exists(foto_lengkap):
                        st.image(foto_lengkap, use_container_width=True)
                        st.subheader(row["nama"])

                        # --- HARGA & STATUS DENGAN FONT LEBIH BESAR ---
                        st.markdown(f"### **Rp {row['harga']:,}**")
                        st.markdown(f"**Status:** {row['status']}")
                    else:
                        st.warning(f"Foto {nama_foto} tidak ditemukan")
            st.divider()

    else:
        st.error("File 'data_bunga.csv' tidak ditemukan!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")


# ==========================================
# BAGIAN KONTAK & ALAMAT (FOOTER)
# ==========================================
st.write("")  # Memberi ruang kosong
st.write("")
st.divider()

st.subheader("📍 Hubungi Kami")
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown(
        """
    **Alamat Galeri:**    
    Kecamatan Gamping, Sleman,  
    Daerah Istimewa Yogyakarta.
    """
    )

with col_info2:
    # Ganti nomor HP di bawah ini dengan nomor Anda (gunakan format 62)
    no_hp = "6285876366016"
    pesan_wa = "Halo, saya tertarik memesan anggrek di katalog Anda."
    link_wa = f"https://wa.me/{no_hp}?text={pesan_wa.replace(' ', '%20')}"

    st.markdown("**WhatsApp:**")
    st.link_button("📱 Pesan Sekarang via WhatsApp", link_wa)

st.caption("© 2026 Toko Anggrek Digital - Semua Hak Dilindungi")