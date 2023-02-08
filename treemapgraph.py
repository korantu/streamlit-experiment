import streamlit as st
import matplotlib.pyplot as plt
import squarify
from random import randint

st.write(f"Now it is {randint(0,100)}")
liquid = st.slider("Liquid", 20, 2000, 30)

volume = [liquid, 220, 170, 150, 50]
labels = ['Liquid\n volume: 100k', 'Savoury\n volume: 220k',
         'Sugar\n volume: 170k', 'Frozen\n volume: 150k',
         'Non-food\n volume: 50k']
color_list = ['#0f7216', '#b2790c', '#ffe9a3',
             '#f9d4d4', '#d35158', '#ea3033']

plt.rc('font', size=14)
squarify.plot(sizes=volume, label=labels,
             color=color_list, alpha=0.7)
plt.axis('off')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
