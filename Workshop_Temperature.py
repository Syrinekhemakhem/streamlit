#Workshop_Temperature 
#EXERCICE2 : 
import streamlit as st
st.markdown("<h1 style='text-align: center; color: #3F51B5;'>🌡️ Exercice 2 : Convertisseur de Température</h1>", unsafe_allow_html=True)
#st.title("Eexercice 2 : Temperature Converter ")


conversion=st.selectbox("Select type de conversion",("Celsius ➡️ Fahrenheit","Fahrenheit ➡️ Celsius"))
if conversion=="Celsius ➡️ Fahrenheit":
    celsus=st.number_input("🌡️ Entrez la température en Celsius :")
    if st.button("Convertir"):
        fahren=(celsus*9/5)+32
         # Emoji en fonction de la température en °C
        if celsus <= 5:
            emoji = "❄️"
            color = "#00008B"
        elif celsus >= 30:
            emoji = "🔥"
            color = "#FF0000"
        else:
            emoji = "🌤️"
            color = "#E0FFFF"
        st.write(f"{emoji} {celsus} °C équivaut à {fahren:.2f} °F")
        #st.write(f"{celsus} C equivaut à {fahren} F")
else:
    conversion=="Fahrenheit ➡️ Celsius"
    fahren=st.number_input("🌡️ Entrez la température en Fahrenheit :")
    if st.button("Convertir"):
        celsus=(fahren-32)*5/9
        if celsus <= 5:
            emoji = "❄️"
            color = "#00008B"
        elif celsus >= 30:
            emoji = "🔥"
            color = "#FF0000"
        else:
            emoji = "🌤️"
            color = "#E0FFFF"
        st.write(f"{emoji} {fahren} °F équivaut à {celsus:.2f} °C")

        #st.write(f"{fahren} F equivaut à {celsus} C")

#esthétique de l'application : 
# Fond légèrement coloré avec CSS
# Titre principal
#st.markdown("<h1 style='text-align: center; color: #3F51B5;'>🌡️ Exercice 2 : Convertisseur de Température</h1>", unsafe_allow_html=True)
# Fin du bloc principal
st.markdown("</div>", unsafe_allow_html=True)



#CHANGER LA COULEUR DU FOND SELON LA TEMPERATURE: 
st.markdown(
    f"""
    <style>
    /* Fond de la page */
    .stApp {{
        background-color: {"#ADD8E6" if celsus <= 5 else "#FF7F7F" if celsus >= 30 else "#F0E68C"};  /* Exemple: bleu ciel très clair */
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div style='background-color: {"#ADD8E6" if celsus <= 5 else "#FF7F7F" if celsus >= 30 else "#F0E68C"};
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-size: 20px;
                margin-top: 15px;'>
        
    </div>
    """,
    unsafe_allow_html=True
)
