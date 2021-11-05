import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import altair as alt
# from load_data import (
#     get_states,
#     load_climate
# )
# from make_plots import (
#     plot_seaborn,
#     plot_county_heatmaps

# )



st.set_page_config(layout="wide")

# read in disease data
tx_cvd_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_cvd.csv', parse_dates=['year_id'], dtype={'FIPS': object})
tx_inf_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_inf.csv', parse_dates=['year_id'], dtype={'FIPS': object})
tx_resp_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_resp.csv', parse_dates=['year_id'], dtype={'FIPS': object})
tx_subInj_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_subInj.csv', parse_dates=['year_id'], dtype={'FIPS': object})

#read in climate data
tx_climate_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_climate_wave.csv', parse_dates=['month_year_long'], dtype={'county_FIPS': object})
tx_heat_wave_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_heat_wave.csv', dtype={'fips': object})

#demographics
tx_demo_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_demographics.csv',dtype={'fips': object})


st.title("County Level Health Trends Investigator")
st.header("Look for Drivers of Health Conditions")
st.subheader("Pretty neat, huh?")

tx_inf_df[:10]
#df_cvd = load_disease()
#states = get_states()

#creates a sidebar
st.sidebar.header('Choose Your Granularity')
#user chooses the county from selectbox
#choose_state = st.sidebar.selectbox('Select State', states)

# state_climate_df = load_climate(choose_state)
# counties = state_climate_df['county_name'].unique()

# plot_choro = plot_county_heatmaps(state_climate_df, 1989, metric='avg_daily_precip_mm')

# st.plotly_chart(plot_choro)

# choose_county = st.sidebar.selectbox('Pick Your County', counties)

# county_climate_df = state_climate_df[state_climate_df['county_name'] == choose_county]


#streamlit & plotly can also give us interactive widgets

show_hist = st.sidebar.checkbox('See Graphs?')

show_df = st.sidebar.checkbox('Do you want to see the data?')

#plot = plot_county_heatmaps(state_climate_df, 2014)

if show_hist:
    #plot = plot_seaborn(county_climate_df)
    st.pyplot(plot)

if show_df:
    county_climate_df[:10]

