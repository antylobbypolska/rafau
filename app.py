import streamlit as st
import pandas as pd
import random

# Tytuł aplikacji
st.title("Dowiedz się jakie poglądy ma dzisiaj Rafal")
# Wyświetlenie obrazu JPEG pod tytułem
try:
    st.image("obraz.jpeg", caption="Rafau",width=300)  # Zmień 'obraz.jpeg' na nazwę swojego pliku
except FileNotFoundError:
    st.warning("Błąd: Nie znaleziono pliku 'obraz.jpeg'. Upewnij się, że plik znajduje się w folderze projektu.")
# Funkcja do wczytania pliku CSV i losowania poglądu
def losuj_poglad():
    try:
        # Wczytanie pliku CSV
        df = pd.read_csv("poglady.csv")  # Zmień na właściwą nazwę pliku
        # Sprawdzenie, czy kolumna 'poglądy' istnieje
        if 'poglądy' not in df.columns:
            return "Błąd: Plik CSV nie zawiera kolumny 'poglądy'."
        # Losowanie wartości z kolumny 'poglądy'
        losowy_poglad = random.choice(df['poglądy'].dropna().tolist())
        return losowy_poglad
    except FileNotFoundError:
        return "Błąd: Nie znaleziono pliku 'poglady.csv'."
    except Exception as e:
        return f"Błąd: {str(e)}"

# Przycisk do losowania
if st.button("zapytaj o pogląd"):
    wynik = losuj_poglad()
    st.write("Pogląd na dzis:")
    st.header(wynik)
