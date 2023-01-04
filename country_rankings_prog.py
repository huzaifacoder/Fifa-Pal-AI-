import pandas as pd

DATABASE = "https://github.com/huzaifacoder/Fifa-Data-Exploration-and-Insights-Generation-Huzaifa-Gulzar-Shaikh/raw/main/DATABASE/Career%20Mode%20player%20datasets%20-%20FIFA%2015-22.csv" # NOQAE501

csv_data = pd.read_csv(DATABASE, low_memory=False)
country_full_no_dupp = csv_data["country_full"].drop_duplicates()
country_abrv_no_dupp = csv_data["country_abrv"].drop_duplicates()

country_full_no_dupp.drop(country_full_no_dupp.index[-66:-1], inplace=True)
country_full_no_dupp.drop(index=country_full_no_dupp.index[-1], axis=0, inplace=True)