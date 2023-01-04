import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title = "FIFA PAL.ai", page_icon = "fifa_logo.png")
#st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Plots')


def sub_title(m):
    st.title(f"Distribution of\
                                    {m}")


database = "C:\\" \
                 "Users\\" \
                 "huzaifa\\" \
                 "PycharmProject\\" \
                 "Fifa_Pal_AI\\" \
                 "Database\\" \
                 "Career_Mode_player_datasets_FIFA 15-22_new_streamlit.csv"
csv_data_2 = pd.read_csv(database, low_memory=False)
#age
age_coll = csv_data_2["age"]
fig1, ax1 = plt.subplots()
ax1.hist(age_coll, bins=100)

#wage
wage_coll = csv_data_2["wage_eur"]
fig2, ax2 = plt.subplots()
ax2.hist(wage_coll, bins=100)

#height
height_cm = csv_data_2["height_cm"]
height_meters = height_cm / 100
fig3, ax3 = plt.subplots()
ax3.hist(height_meters, bins=100)

nationality_coll = csv_data_2["nationality_name"]
#fig4, ax4 = plt.subplots()
#ax4.hist(wage_coll, bins=100)

sub_title("Age")
st.pyplot(fig1)

sub_title("WAGE(£)")
st.pyplot(fig2)

sub_title("Height in meter")
st.pyplot(fig3)

#mport plotly.express as px
#ist_age = px.histogram(csv_data_2, x=csv_data_2["age"], nbins=20, title="Distribution of age.")
#ist_wage = px.histogram(csv_data_2, x=csv_data_2["wage_eur"], nbins=20, title="Distribution of wage in pounds (£).")
#hist_height=px.histogram(csv_data_2, x=csv_data_2[height_meters], nbins=20, title="Distribution of height in meters")
#hist_country = px.histogram(csv_data_2, x=nationality_coll, nbins=20, title="Distribution of nationality.")
#hist_country.show()
#hist_prf_foot = px.histogram(csv_data_2, x=preferred_foot, nbins=20, title="Distribution of preferred foot.")


#sub_title("nationality")
#st.pyplot(fig4)
