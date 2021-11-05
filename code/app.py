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
from make_plots import (
    plot_seaborn,
    plot_county_heatmaps,
    plot_kmeans_choropleth,
    plot_mortality_lines,
    plot_mortality_heatmaps,
    plot_hw_days_choropleth,
    plot_precip_lines,
    demographics_heatmap

)



st.set_page_config(layout="wide")

# read in disease data
tx_cvd_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_cvd.csv', parse_dates=['year_id'], dtype={'FIPS': object})
tx_inf_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_inf.csv', parse_dates=['year_id'], dtype={'FIPS': object})
tx_resp_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_resp.csv', parse_dates=['year_id'], dtype={'FIPS': object})
tx_subInj_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_subInj.csv', parse_dates=['year_id'], dtype={'FIPS': object})

#read in climate data
tx_climate_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_climate_wave.csv', parse_dates=['month_year_long'], dtype={'county_FIPS': object})
tx_heat_wave_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_heat_wave.csv', parse_dates=['Year'], dtype={'County Code': object})

#demographics
tx_demo_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_demographics.csv',dtype={'fips': object})
#tx_demo_USE = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_demographics_full.csv',dtype={'fips': object})
#kmeans
k_means = pd.read_csv('../data/cleaned/kmeans_clusters_with_labels_and_features.csv',dtype={'fips': object})


st.title("County Level Health Trends Investigator")
st.header("Look for Drivers of Health Conditions")
st.write("We created some interactive visualizations to help users dig into trends in climate, mortality and demographics")

dfs_to_plot = ['Cardiovascular Disease', 'Infectious Diseases', 'Respiratory Diseases', 'Substance Abuse & Self Injury']
sexes = ['Male', 'Female', 'Both']
demographic_variables = ['Median Age', '% Pop < 18', '% Pop > 65', 'Unemployment Rate', '% Pop Below Poverty', 'Uninsured Population', 'Rural/Urban Continuum', 'Obesity Rate per 100K']
years = list(range(1980, 2015))

#creates a sidebar
st.sidebar.header('Choose Your Mortality Metrics')
select_mortality_df = st.sidebar.selectbox("Select Disease", dfs_to_plot)

if select_mortality_df == 'Cardiovascular Disease':
    disease_df = tx_cvd_df
elif select_mortality_df == 'Infectious Diseases':
    disease_df = tx_inf_df
elif select_mortality_df == 'Respiratory Diseases':
    disease_df = tx_resp_df
elif select_mortality_df == 'Substance Abuse & Self Injury':
    disease_df = tx_subInj_df
    

mortality_causes = disease_df['cause_name'].unique()

sex = st.sidebar.selectbox("Select Sex Aggregation", sexes)
cause = st.sidebar.selectbox('Select Cause of Death', mortality_causes)  
year = st.sidebar.selectbox("Select Year", years)

#mortality_lineplot = plot_mortality_lines(select_mortality_df, sex)

st.header("Mortality Infographics")
st.subheader("Pretty neat, huh?")
mortality_heatmap = plot_mortality_heatmaps(disease_df, cause, year, sex)
mortality_lineplot = plot_mortality_lines(disease_df, sex)

st.plotly_chart(mortality_heatmap)


show_mortality_lines = st.checkbox('Show Mortality Lines?')


if show_mortality_lines:
    st.plotly_chart(mortality_lineplot)
    show_df = st.checkbox("Show Data?")
    if show_df:
        disease_df

# adding in some comments for github to recognize
st.header("Here is climate stuff")
st.write("We investivated climate and participation. Check the box below to show our visual of average (max) temperature and precipitation through the years")
hw_years = list(range(1981, 2011))
hw_year = st.selectbox('Choose Year', hw_years)
hw_heatmap = plot_hw_days_choropleth(tx_heat_wave_df, hw_year)
st.plotly_chart(hw_heatmap)
show_climate_lines = st.checkbox('Show Climate Lines?')
if show_climate_lines:
    st.pyplot(plot_precip_lines(tx_climate_df))


st.header("Demographic Data")
demo_metric = st.selectbox("Choose your Demographic Metric", demographic_variables)
demo_heatmap = demographics_heatmap(tx_demo_df, demo_metric)
st.plotly_chart(demo_heatmap)


st.header("We did some K Means Clustering")
st.write("Grouping Similar Counties")
plot_kmeans = plot_kmeans_choropleth(k_means)
st.plotly_chart(plot_kmeans)



#plot = plot_county_heatmaps(state_climate_df, 2014)



