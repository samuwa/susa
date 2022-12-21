import streamlit as st

meds = {"medicina 1":15.00, "medicina 2": 27.00, "medicina 3": 32.00}

st.title("SuSa")
st.header("Cómo funciona?")
st.write('''
1. Sugiérenos que medicamentos deberíamos traer
2. Al instante buscamos el mejor precio en nuestra red internacional
3. Te avisamos cuando llega tu sugerencia y la reclamas con tu número telefónico
''')

st.header("Danos tu sugerencia")
selec = st.multiselect("Busca tus medicamentos", options=meds.keys())

cantidades = {}
subtotal = 0
total = 0
for x in selec:
    col1, col2 = st.columns(2)
    col1.subheader(f"{x} ----- ${meds[x]}")
    cantidades[x] = col2.number_input(f"Cúantos paquetes de {x}?", step=1, min_value=1, max_value=3)


with st.expander("Tómale foto a tu prescripción"):
    st.camera_input("")

st.header("Confírmanos tu sugerencia")
col1, col2 = st.columns(2)
for x in selec:
    col1.write(f"{x} --- {int(cantidades[x])} X ${meds[x]}")
    col2.write(f"**${int(cantidades[x]*meds[x])}**")
    subtotal += cantidades[x]*meds[x]
    total += cantidades[x]*meds[x]

col1.write(f"Impuestos de importación (30%)")
col2.write(f"**${int(subtotal * 0.3)}**")
total += int(total * 0.3)
col1.write(f"Tasa de servicio (20%)")
col2.write(f"**${int(subtotal * 0.2)}**")
total += subtotal * 0.2

st.subheader(f"Total = ${total}")

with st.form("form1"):
    email = st.text_input("Ingresa tu correo electrónico")
    num = st.text_input("Ingresa tu número telefónico")

    submit = st.form_submit_button("Enviar Sugerencia!")

    if submit:
        st.write("Sugerencia recibida! Reclama tu sugerencia con el codigo **SS8472**")


