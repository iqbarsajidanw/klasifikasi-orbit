import pickle
import streamlit as st

# membaca model
orbit_model = pickle.load(open('orbit_model.sav', 'rb'))

#judul web
st.title('Prediksi Kelas Orbit')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    a_AU = st.number_input ('Input Nilai Sumbu semi-mayor orbit dalam AU')
    e = st.number_input ('Input Nilai Eksentrisitas orbit')
    i_deg = st.number_input ('Input Nilai Kemiringan orbit terhadap bidang ekliptika dan ekuinoks J2000 (J2000-Ekliptika) dalam derajat')
    w_deg = st.number_input ('Input Nilai Argumen perihelion (J2000-Ecliptic) dalam derajat')
    Node_deg = st.number_input ('Input Nilai Bujur dari node naik (J2000-Elips) dalam derajat')
    M_deg = st.number_input ('Input Nilai Anomali rata-rata pada zaman dalam derajat')    

with col2:
    q_AU = st.number_input ('Input Nilai Jarak perihelion orbit dalam AU')
    Q_AU_1 = st.number_input ('Input Nilai Jarak aphelion orbit dalam AU')
    P_yr = st.number_input ('Input Nilai Periode orbit dalam tahun Julian')
    H_mag = st.number_input ('Input Nilai Magnitudo V absolut')
    MOID_AU = st.number_input ('Input Nilai Jarak perpotongan orbit minimum (jarak minimum antara orbit osilasi NEO dan Bumi)')

# code untuk prediksi
orbit_class = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi orbit'):
    orbit_predict = orbit_model.predict([[a_AU, e, i_deg, w_deg, Node_deg, 
                                          M_deg, q_AU,Q_AU_1, P_yr, H_mag, 
                                          MOID_AU]])

    if orbit_predict == 0:
        orbit_class = 'Kualitas Tidur Termasuk Kedalam Kategori Normal'
    elif orbit_predict == 1:
        orbit_class = 'Kualitas Tidur Termasuk Kedalam Kategori orbit Apnea'
    else:
        orbit_class = 'Kualitas Tidur Termasuk Kedalam Kategori Insomnia'
st.success(orbit_class)
