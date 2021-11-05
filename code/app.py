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
    load_health_data,
    load_demographics,
    load_kmeans,
    load_climate,
    load_heat_wave
)
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


#read in climate data
tx_climate_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_climate_wave.csv', parse_dates=['month_year_long'], dtype={'county_FIPS': object})


#demographics
#tx_demo_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_demographics.csv',dtype={'fips': object})

#kmeans
#k_means = pd.read_csv('../data/cleaned/kmeans_clusters_with_labels_and_features.csv',dtype={'fips': object})


st.title("Texas Case Study: County Level Health Trends Investigator")
st.header("A Visual Comparison of Disease Mortality & Select Demographic Variables")
st.write("We created this interactive visualization to help users dig into and identify interesting trends, hotspots & associations across mortality and demographic variables")

dfs_to_plot = ['Cardiovascular Disease', 'Infectious Diseases', 'Respiratory Diseases', 'Substance Abuse & Self Injury']
sexes = ['Male', 'Female', 'Both']
demographic_variables = ['Median Age', '% Pop < 18', '% Pop > 65', 'Unemployment Rate', '% Pop Below Poverty', 'Uninsured Population', 'Rural/Urban Continuum', 'Obesity Rate per 100K']
years = list(range(1980, 2015))

#creates a sidebar
st.sidebar.header('Choose Your Mortality Metrics')
st.sidebar.write("For a better experience, collapse this sidebar once you've made your selections.")
select_mortality_df = st.sidebar.selectbox("Select Disease", dfs_to_plot)
disease_df = load_health_data(select_mortality_df)

mortality_causes = disease_df['cause_name'].unique()

sex = st.sidebar.selectbox("Select Sex Aggregation", sexes)
cause = st.sidebar.selectbox('Select Cause of Death', mortality_causes)  
year = st.sidebar.selectbox("Select Year", years)

col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 1])

with col1:
    st.header("Mortality Infographics")
    st.write("This represents Deaths per 100K, from 1980 to 2014")
    mortality_heatmap = plot_mortality_heatmaps(disease_df, cause, year, sex)
    mortality_lineplot = plot_mortality_lines(disease_df, sex)

    st.plotly_chart(mortality_heatmap)

    #show_mortality_lines = st.checkbox('Show Mortality Lines?')

    # if show_mortality_lines:
    #     st.plotly_chart(mortality_lineplot)
    #     show_df = st.checkbox("Show Data?")
    #     if show_df:
    #         disease_df
with col3:
    st.header("Demographic Data")
    demo_metric = st.selectbox("Choose your Demographic Metric", demographic_variables)

    #creating the demographics choropleth
    st.plotly_chart(demographics_heatmap(load_demographics(), demo_metric))

#
st.header("We did some K Means Clustering")
st.write("Grouping Similar Counties")

plot_kmeans = plot_kmeans_choropleth(load_kmeans())
st.plotly_chart(plot_kmeans)


# adding in some comments for github to recognize
st.header("Here is climate stuff")
st.write("We investivated climate and participation. Check the box below to show our visual of average (max) temperature and precipitation through the years")
show_heatwaves = st.checkbox("Would you like to see the climate stuff?")

if show_heatwaves:
    hw_df = load_heat_wave()
    st.plotly_chart(plot_hw_days_choropleth(hw_df))
    

# hw_years = list(range(1981, 2011))
# hw_year = st.selectbox('Choose Year', hw_years)
# hw_df = load_heat_wave()
#hw_heatmap = plot_hw_days_choropleth(hw_df, hw_year)
#st.plotly_chart(plot_hw_days_choropleth(hw_df, hw_year))
show_climate_lines = st.checkbox('Show Climate Lines?')
if show_climate_lines:
    st.pyplot(plot_precip_lines(tx_climate_df))









#plot = plot_county_heatmaps(state_climate_df, 2014)



