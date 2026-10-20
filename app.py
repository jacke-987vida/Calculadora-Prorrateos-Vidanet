import streamlit as st

st.title("Calculadora de Prorrateos - Vidanet")

# Creamos 4 pestañas en el orden que indicaste
tab1, tab2, tab3, tab4 = st.tabs([
    "Recargo 15",
    "Descuento 15",
    "Recargo 01",
    "Descuento 01"
])

# -------------------------------------------------------------
# Prorrateo Recargo (15 Del Mes)
# -------------------------------------------------------------
with tab1:
    st.subheader("Prorrateo Inicial Recargo (Corte al 15)")
    monto_1 = st.number_input("Monto del plan ($)", value=30.00, key="m1")
    dia_1 = st.number_input("Día de instalación", min_value=1, max_value=31, value=10, key="d1")

    if st.button("Calcular Recargo 15", key="btn1"):
        dias = 0 if dia_1 == 15 else 15 - dia_1
        total = monto_1 if dia_1 == 15 else round(monto_1 + (monto_1 / 30 * dias), 2)
        st.success(f"Días extra: {dias} | Total a cobrar: ${total:.2f}")

# -------------------------------------------------------------
# Prorrateo Descuento (15 Del Mes)
# -------------------------------------------------------------
with tab2:
    st.subheader("Prorrateo Descuento (Corte al 15)")
    monto_2 = st.number_input("Monto del plan ($)", value=30.00, key="m2")
    dia_2 = st.number_input("Día de instalación", min_value=1, max_value=31, value=16, key="d2")

    if st.button("Calcular Descuento 15", key="btn2"):
        dias = dia_2 - 15
        descuento = round((monto_2 / 30) * dias, 2)
        total = round(monto_2 - descuento, 2)
        st.success(f"Días a descontar: {dias} | Descuento: ${descuento:.2f} | Total a cobrar: ${total:.2f}")

# -------------------------------------------------------------
# Prorrateo Recargo (01 Del Mes)
# -------------------------------------------------------------
with tab3:
    st.subheader("Prorrateo Recargo (Corte al Día 1)")
    monto_4 = st.number_input("Monto del plan ($)", value=30.00, key="m4")
    dia_4 = st.number_input("Día de instalación", min_value=1, max_value=31, value=23, key="d4")

    if st.button("Calcular Recargo Día 1", key="btn4"):
        dias = 0 if dia_4 == 1 else (30 - dia_4 + 1)
        recargo = round((monto_4 / 30) * dias, 2)
        total = round(monto_4 + recargo, 2)
        st.success(f"Días extra: {dias} | Recargo: ${recargo:.2f} | Total a cobrar: ${total:.2f}")

# -------------------------------------------------------------
# Prorrateo Descuento (01 Del Mes)
# -------------------------------------------------------------
with tab4:
    st.subheader("Prorrateo Descuento (Corte al Día 1)")
    monto_3 = st.number_input("Monto del plan ($)", value=30.00, key="m3")
    dia_3 = st.number_input("Día de instalación", min_value=1, max_value=31, value=5, key="d3")

    if st.button("Calcular Descuento Día 1", key="btn3"):
        dias = dia_3 - 1
        descuento = round((monto_3 / 30) * dias, 2)
        total = round(monto_3 - descuento, 2)
        st.success(f"Días a descontar: {dias} | Descuento: ${descuento:.2f} | Total a cobrar: ${total:.2f}")
