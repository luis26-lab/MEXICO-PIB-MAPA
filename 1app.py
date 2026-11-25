import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧠 Simulador de Neurona Matemática")
st.write("Mueve los controles para ver cómo cambian los cálculos y la función de activación.")

# --- 1. Controles para los alumnos ---
st.sidebar.header("⚙️ Entradas (x)")
x0 = st.sidebar.slider("x0", -2.0, 2.0, 0.12)
x1 = st.sidebar.slider("x1", -2.0, 2.0, 0.93)
x2 = st.sidebar.slider("x2", -2.0, 2.0, 0.91)

st.sidebar.header("⚖️ Pesos (w)")
w0 = st.sidebar.slider("w0", -3.0, 3.0, 0.61)
w1 = st.sidebar.slider("w1", -3.0, 3.0, 0.07)
w2 = st.sidebar.slider("w2", -3.0, 3.0, 2.16)

b = st.sidebar.slider("Sesgo (b)", -2.0, 2.0, -0.50)

# --- 2. Cálculos matemáticos ---
z = (w0 * x0) + (w1 * x1) + (w2 * x2) + b
salida = np.tanh(z)

# --- 3. Mostrar las fórmulas ---
st.latex(r"f(z) = \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}")
st.latex(f"z = ({w0})({x0}) + ({w1})({x1}) + ({w2})({x2}) + ({b}) = {z:.4f}")
st.latex(f"\\text{{Salida}} = \\tanh({z:.4f}) = {salida:.4f}")

# --- 4. Gráfica de la función ---
st.subheader("📈 Gráfica de la función Tangente Hiperbólica")

z_vals = np.linspace(-4, 4, 100)
a_vals = np.tanh(z_vals)

fig, ax = plt.subplots()
ax.plot(z_vals, a_vals, label='f(z) = tanh(z)', color='purple', linewidth=2)
ax.plot(z, salida, 'ro', markersize=10, label=f'Punto actual ({z:.2f}, {salida:.2f})')
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True)
ax.legend()
ax.set_xlabel("z (Suma ponderada)")
ax.set_ylabel("Salida (Activación)")

st.pyplot(fig)
