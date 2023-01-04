#IMPORTS
import pandas as pd
import streamlit as st
from country_rankings_prog import country_full_no_dupp

# database setting
DATABASE = "https://github.com/huzaifacoder/Fifa-Data-Exploration-and-Insights-Generation-Huzaifa-Gulzar-Shaikh/raw/main/DATABASE/Career%20Mode%20player%20datasets%20-%20FIFA%2015-22.csv" # NOQAE501

csv_data_1 = pd.read_csv(DATABASE, low_memory=False)


# lists and arrays
short_name = csv_data_1["short_name"]
short_name_10s = short_name[:10]
short_name_20s = short_name[:20]
short_name_list = list(short_name.copy())

#print(short_name_list)
short_name_a_to_z = short_name_list.copy()
short_name_a_to_z.sort()
player_face = csv_data_1["player_face_url"]
long_name = csv_data_1["long_name"]
long_name_list = list(long_name)
wage = csv_data_1["wage_eur"]
age = csv_data_1["age"]
age_list = list(age)
wage_list = list(wage)
potential = csv_data_1["potential"]
potential_list = list(potential)
contract_valid_until = csv_data_1["club_contract_valid_until"]
international_reputation = csv_data_1["international_reputation"]
preferred_foot = csv_data_1["preferred_foot"]
nationality_name = csv_data_1["nationality_name"]

height_cm = csv_data_1["height_cm"]
height_meters = height_cm / 100

international_reputation_list = list(international_reputation)
preferred_foot_list = list(preferred_foot)
height_meters_list = list(height_meters)

nationality_name_no_dup = nationality_name.drop_duplicates()
nationality_name_a_z = nationality_name.sort_values()
nationality_name_length = len(nationality_name_no_dup)
nationality_name_list_org = list(nationality_name)
nationality_name_10s = country_full_no_dupp[:10]
nationality_name_20s = country_full_no_dupp[:20]
print(nationality_name_length)

# gui setting
st.set_page_config(page_title = "FIFA PAL.ai", page_icon = "fifa_logo.png")

#st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Nationality Analysis')
filters_list_nationality = ["Ranking/Default", "A-Z.", "Top 10s.", "Top 20s."]
filter_options_nationality = st.selectbox("Pick a Filter", filters_list_nationality)


def WritePlayerStats(x):  # Writing the selected Player's Statistics
    x_index = short_name_list.index(x)
    wage_output_format = f"{int(wage[x_index]):,}"
    colT1, colT2, colT3 = st.columns([5 , 6, 4])

    with colT1:
        st.image(player_face[x_index], width = 180, output_format="PNG" )
        st.write('_You selected:_', f"_{x}_\n")

    with colT2:

        st.write(f"Long Name: {long_name.dropna()[x_index]}\n"
                      f"\nShort Name: {short_name[x_index]}\n"
                      f"\nAge: {str(age[x_index])}\n"
                      f"\nWage: £{wage_output_format}\n"  # note: f'{wage[x_index]:,} for comma separation'
                      f"\nInternational reputation: {str(international_reputation_list[x_index])}\n")
    with colT3:
        st.write(f"\nPotential: {str(potential[x_index])}\n"
                    f"\nHeight: {str(height_meters[x_index])} meters\n"
                    f"\nPreferred foot: {preferred_foot_list[x_index]}\n"
                    
                    f"\nNationality: {str(nationality_name[x_index])}\n"
                    f"\nPrefered foot: {str(preferred_foot[x_index])}\n")
        st.write(f"\nContract_valid_until: {str(int(contract_valid_until[x_index]))}\n")


def nationality_func(op):
    intNationalIndex1 = 0
    player_c = []

    for country_name in nationality_name_list_org:
        if country_name == op:
            player_c.append(short_name[intNationalIndex1])
        intNationalIndex1 += 1
    filters_option_player = st.selectbox("Players", player_c)
    WritePlayerStats(filters_option_player)


def ranking_option_nationality():
    filter_options_ranking_n = st.selectbox("Country", country_full_no_dupp)
    nationality_func(filter_options_ranking_n)


def A_z_option_nationality():
    filter_options_a_z_n = st.selectbox("Country", nationality_name_a_z)
    nationality_func(filter_options_a_z_n)


def Top_10s_option_nationality():
    filter_options_10s_n = st.selectbox("Country", nationality_name_10s)
    nationality_func(filter_options_10s_n)


def Top_20s_option_nationality():
    filter_options_20s_n = st.selectbox("Country", nationality_name_20s)
    nationality_func(filter_options_20s_n)


if filter_options_nationality == filters_list_nationality[0]:
    ranking_option_nationality()

elif filter_options_nationality == filters_list_nationality[1]:
    A_z_option_nationality()

elif filter_options_nationality == filters_list_nationality[2]:
    Top_10s_option_nationality()

else:
    Top_20s_option_nationality()