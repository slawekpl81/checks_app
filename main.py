#! venv/bin/python3
"""
DataFrame:[Szyb, Poziom, Obiekt, Opis, Wykonawca, Data_wykonania, Wykonano, Czestotliwosc]
"""
import argparse
import pandas as pd
import datetime

data_file = "data.csv"
columns_name = [
    "Szyb",
    "Poziom",
    "Obiekt",
    "Opis",
    "Wykonawca",
    "Data_wykonania",
    "Wykonano",
    "Czestotliwosc",
]


def add_check(df):
    print("\n\n\n******************************************")
    print("Podaj treść zadania: ")
    input_text = []
    for i in range(len(columns_name)):
        print(f"{columns_name[i]}: ")
        values = df[columns_name[i]].unique().tolist()
        if values:
            print(f"np.: {values[:5]}")
        temp = input("\t:")
        if len(temp) == 0:
            return df
        input_text.append(temp)
    df = pd.concat(
        [
            df,
            pd.DataFrame(
                {
                    "Szyb": [input_text[0]],
                    "Poziom": [input_text[1]],
                    "Obiekt": [input_text[2]],
                    "Opis": [input_text[3]],
                    "Wykonawca": [input_text[4]],
                    "Data_wykonania": [input_text[5]],
                    "Wykonano": [input_text[6]],
                    "Czestotliwosc": [input_text[7]],
                }
            ),
        ],
        ignore_index=True,
    )
    return df


def print_all_checks(df):
    if df.empty:
        print("Brak zadań.")
    else:
        print(df)


def oznacz_jako_wykonane(df):
    print_all_checks(df)
    if not df.empty:
        try:
            indeks = int(input("Podaj numer zadania do oznaczenia jako wykonane: "))
            df.loc[indeks, "Wykonane"] = True
        except (ValueError, IndexError):
            print("Nieprawidłowy numer zadania.")
    return df


def save_to_file(df, file_name=data_file):
    df.to_csv(file_name, index=False)
    print(f"Zadania zapisane do pliku {file_name}")


def read_from_file(file_name=data_file):
    try:
        df = pd.read_csv(file_name)
        # Konwersja kolumny 'Data dodania' na datetime, jeśli istnieje
        if "Data dodania" in df.columns:
            df["Data dodania"] = pd.to_datetime(df["Data dodania"])
        return df
    except FileNotFoundError:
        print("Brak zapisanego pliku z zadaniami. Tworzę nowy DataFrame.")
        return pd.DataFrame(columns=columns_name)


def main():
    df = read_from_file(data_file)

    while True:
        print("\n\n\n******************************************")
        print("--- Aplikacja CHECKS ---")
        print("1. Dodaj zadanie")
        print("2. Wyświetl zadania")
        print("3. Oznacz jako wykonane")
        print("4. Zapisz i wyjdź")
        print("******************************************")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            df = add_check(df)
        elif wybor == "2":
            print_all_checks(df)
        elif wybor == "3":
            df = oznacz_jako_wykonane(df)
        elif wybor == "4":
            save_to_file(df, data_file)
            break
        else:
            print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()
