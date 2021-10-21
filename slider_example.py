import streamlit as st
import matplotlib.pyplot as plt
from math import sin, atan
import numpy as np




# Definition of Pacejka parameters
# X : longitudinal slip
# B : stiffness factor
# C : shape factor
# D : peak factor
# E : curvature factor

# B = 0.171
B = st.slider('B',0.1,0.2,0.15)
C = 1.69
D = 4236
E = 0.619

def F(x):
    return(D * sin(C * atan(B*x - E*(B*x - atan(B*x)))))
  
num_points=100
X = np.linspace(0,100,100)

plt.rcParams["figure.figsize"] = (8,6) # set fig size for matplotlib
fig=plt.plot(X,np.vectorize(F)(X));
st.pyplot(fig)
