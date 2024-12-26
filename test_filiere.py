import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def main():
    # Titre de l'application
    st.title("Test d'Aide au Choix de Filière")
    st.subheader("Analysez vos compétences et votre savoir-être pour découvrir la filière idéale.")

    # Introduction
    st.write("""
    Ce test est conçu pour vous guider dans le choix de votre filière en fonction de :
    - Vos compétences techniques.
    - Vos capacités cognitives.
    - Votre savoir-être (soft skills).
    - Vos préférences psychologiques.
    Répondez aux questions suivantes pour obtenir une recommandation personnalisée.
    """)
