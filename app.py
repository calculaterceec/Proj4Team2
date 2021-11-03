import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import altair as alt
from load_data import (
    get_states,
    load_climate
)
from make_plots import (
    plot_seaborn,
    plot_county_heatmaps

)

st.set_page_config(layout="wide")

st.title("County Level Health Trends Investigator")
st.header("Look for Drivers of Health Conditions")
st.subheader("Pretty neat, huh?")


#df_cvd = load_disease()
states = get_states()

#creates a sidebar
st.sidebar.header('Choose Your Granularity')
#user chooses the county from selectbox
choose_state = st.sidebar.selectbox('Select State', states)

state_climate_df = load_climate(choose_state)
counties = state_climate_df['county_name'].unique()

plot_choro = plot_county_heatmaps(state_climate_df, 1989, metric='avg_daily_precip_mm')

st.plotly_chart(plot_choro)

choose_county = st.sidebar.selectbox('Pick Your County', counties)

county_climate_df = state_climate_df[state_climate_df['county_name'] == choose_county]


#streamlit & plotly can also give us interactive widgets

show_hist = st.sidebar.checkbox('See Graphs?')

show_df = st.sidebar.checkbox('Do you want to see the data?')

plot = plot_county_heatmaps(state_climate_df, 2014)

if show_hist:
    plot = plot_seaborn(county_climate_df)
    st.pyplot(plot)

if show_df:
    county_climate_df[:10]

