import streamlit as st

st.title("Calcul de la hauteur max de la machine autorisée en zmax")

st.write("""
Cette application calcule la **hauteur maximale autorisée d'une éolienne (Ht machine au Zmax)** en mètres,
en fonction du plafond (en pieds), de l'altitude max du terrain (en mètres),
et éventuellement de l'altitude de l'aérodrome (AD) si connue.
""")

# Entrées utilisateur
plafond_ft = st.number_input("Plafond (en pieds)", min_value=0, step=100)
alt_max_m = st.number_input("Altitude maximale du terrain (en mètres)", min_value=0.0, step=10.0)
alt_ad_m = st.number_input("Altitude AD (en mètres) (laisser à 0 si inconnu)", min_value=0.0, step=1.0)

# Constante
MFO_m = 300
plafond_m = plafond_ft * 0.3048

# Calcul
if plafond_ft > 0 and alt_max_m > 0:
    if alt_ad_m == 0:
        ht_machine = plafond_m - alt_max_m - MFO_m
    else:
        ht_machine = plafond_m - (alt_max_m - alt_ad_m) - MFO_m

    st.success(f"Hauteur machine au Zmax : {ht_machine:.2f} mètres")
else:
    st.warning("Veuillez entrer des valeurs valides.")
