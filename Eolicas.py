# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 7: Energía Asequible y No Contaminante ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir la eficiencia de un parque eólico
, alineado con el **ODS 7: Energía Asequible y No Contaminante**.
""")
# Insertamos una imagen
st.image("turbinas.jpg", caption="Eficiencia energetica eolica basada en la velocidad del viento.")



# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Parámetro velocidad del viento")
# Definimos los parámetros de nuestro deslizador:
  
temp_input = st.sidebar.slider("Velocidad del viento (m/s)", 0, 30, 15)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('Energia_Eol.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['Velocidad_Viento_ms']]
y = df['Eficiencia_Energetica_kWh']

# Creamos y entrenamos el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

# Hacemos la predicción con el modelo y la temperatura seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

# Presentamos los resultados
st.subheader('Eficiencia Energetica estimada')
st.write(f'La eficiencia energética es: {prediccion:.2f}kWh')

