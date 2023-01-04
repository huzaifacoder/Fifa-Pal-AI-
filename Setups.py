#IMPORTS
import pandas as pd

# DATABASE setting
DATABASE = "https://github.com/huzaifacoder/Fifa-Data-Exploration-and-Insights-Generation-Huzaifa-Gulzar-Shaikh/raw/main/DATABASE/Career%20Mode%20player%20datasets%20-%20FIFA%2015-22.csv" # NOQAE501

csv_data = pd.read_csv(DATABASE, low_memory=False)


# lists and arrays
short_name = csv_data["short_name"]
short_name_10s = short_name[:10]
short_name_20s = short_name[:20]
short_name_tuple = tuple(short_name.copy())

#print(short_name_list)
short_name_a_to_z = list(short_name_tuple).copy()
short_name_a_to_z.sort()
short_name_a_to_z_tuple = tuple(short_name_a_to_z)
player_face = csv_data["player_face_url"]
long_name = csv_data["long_name"]
long_name_tuple = tuple(long_name)
wage = csv_data["wage_eur"]
age = csv_data["age"]
age_tuple = tuple(age)
wage_tuple = tuple(wage)
potential = csv_data["potential"]
potential_tuple = tuple(potential)
contract_valid_until = csv_data["club_contract_valid_until"]
international_reputation = csv_data["international_reputation"]
preferred_foot = csv_data["preferred_foot"]
nationality_name = csv_data["nationality_name"]

height_cm = csv_data["height_cm"]
height_meters = height_cm / 100

international_reputation_list = tuple(international_reputation)
preferred_foot_tuple = tuple(preferred_foot)
height_meters_tuple = tuple(height_meters)