import streamlit as st

st.title("Calculadora de Prorrateos - Vidanet")

# Creamos 4 pestañas para cada uno de tus escenarios
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Recargo 15",
    "2. Descuento 15",
    "3. Descuento Día 1",
    "4. Recargo Día 1"
])

# -------------------------------------------------------------
# 1. Prorrateo Inicial Recargo 15 de cada mes
# -------------------------------------------------------------
with tab1:
    st.subheader("Prorrateo Inicial Recargo (Corte al 15)")
    monto_1 = st.number_input("Monto del plan ($)", value=30.00, key="m1")
    dia_1 = st.number_input("Día de instalación", min_value=1, max_value=31, value=10, key="d1")

    if st.button("Calcular Recargo 15", key="btn1"):
        dias = 0 if dia_1 == 15 else 15 - dia_1
        total = monto_1 if dia_1 == 15 else monto_1 + (monto_1 / 30 * dias)
        st.success(f"Días extra: {dias} | Total a cobrar: ${total:.2f}")

# -------------------------------------------------------------
# 2. Prorrateo Descuento 15 del mes
# -------------------------------------------------------------
with tab2:
    st.subheader("Prorrateo Descuento (Corte al 15)")
    monto_2 = st.number_input("Monto del plan ($)", value=30.00, key="m2")
    dia_2 = st.number_input("Día de instalación", min_value=1, max_value=31, value=16, key="d2")

    if st.button("Calcular Descuento 15", key="btn2"):
        dias = dia_2 - 15
        descuento = (monto_1 / 30) * dias if 'monto_1' in locals() else (monto_2 / 30) * dias
        total = monto_2 - descuento
        st.success(f"Días a descontar: {dias} | Descuento: ${descuento:.2f} | Total a cobrar: ${total:.2f}")

# -------------------------------------------------------------
# 3. Prorrateo Inicial Descuento 01 del mes
# -------------------------------------------------------------
with tab3:
    st.subheader("Prorrateo Descuento (Corte al Día 1)")
    monto_3 = st.number_input("Monto del plan ($)", value=30.00, key="m3")
    dia_3 = st.number_input("Día de instalación", min_value=1, max_value=31, value=5, key="d3")

    if st.button("Calcular Descuento Día 1", key="btn3"):
        dias = dia_3 - 1
        descuento = (monto_3 / 30) * dias
        total = monto_3 - descuento
        st.success(f"Días a descontar: {dias} | Descuento: ${descuento:.2f} | Total a cobrar: ${total:.2f}")

# -------------------------------------------------------------
# 4. Prorrateo Recargo 01 del mes
# -------------------------------------------------------------
with tab4:
    st.subheader("Prorrateo Recargo (Corte al Día 1)")
    monto_4 = st.number_input("Monto del plan ($)", value=30.00, key="m4")
    dia_4 = st.number_input("Día de instalación", min_value=1, max_value=31, value=23, key="d4")

    if st.button("Calcular Recargo Día 1", key="btn4"):
        dias = 0 if dia_4 == 1 else (30 - dia_4 + 1)
        recargo = (monto_4 / 30) * dias
        total = monto_4 + recargo
        st.success(f"Días extra: {dias} | Recargo: ${recargo:.2f} | Total a cobrar: ${total:.2f}")
