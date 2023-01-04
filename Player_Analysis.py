#IMPORTS
import pandas as pd
import streamlit as st
from Setups import *

st.set_page_config(page_title = "FIFA PAL.ai", page_icon = "fifa_logo.png")
#st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('FIFA PAL.ai')

filters_list = ["Ranking/Default", "A-Z.", "Top 10s.", "Top 20s."]
filter_options = st.selectbox("Pick a Filter", filters_list)

# gui setting..👇👇👇..


def WritePlayerStats(x):  # Writing the selected Player's Statistics
    x_index = short_name_tuple.index(x)
    wage_output_format = f"{int(wage[x_index]):,}"
    colT1, colT2, colT3 = st.columns([5, 6, 4])

    with colT1:
        st.image(player_face[x_index], width=180, output_format="PNG")
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
                 f"\nPreferred foot: {preferred_foot_tuple[x_index]}\n"

                 f"\nNationality: {str(nationality_name[x_index])}\n"
                 f"\nPrefered foot: {str(preferred_foot[x_index])}\n")
        st.write(f"\nContract_valid_until: {str(int(contract_valid_until[x_index]))}\n")


def ranking_option():
    filter_options_ranking = st.selectbox("Players", short_name)
    WritePlayerStats(filter_options_ranking)


def A_z_option():
    filter_options_a_z = st.selectbox("Players", short_name_a_to_z_tuple)
    WritePlayerStats(filter_options_a_z)


def Top_10s_option():
    filter_options_10s = st.selectbox("Players", short_name_10s)
    WritePlayerStats(filter_options_10s)


def Top_20s_option():
    filter_options_20s = st.selectbox("Players", short_name_20s)
    WritePlayerStats(filter_options_20s)


if filter_options == filters_list[0]:
    ranking_option()

elif filter_options == filters_list[1]:
    A_z_option()

elif filter_options == filters_list[2]:
    Top_10s_option()

else:
    Top_20s_option()

# testing
#var = [ranking_option() if filter_options == filters_list[0]\
#           else Top_10s_option()\
#    if filter_options == filters_list[2] else Top_20s_option()]
