import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import altair as alt
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    geo_counties = json.load(response)

# tx_cvd_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_cvd.csv', parse_dates=['year_id'], dtype={'FIPS': object})
# tx_inf_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_inf.csv', parse_dates=['year_id'], dtype={'FIPS': object})
# tx_resp_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_resp.csv', parse_dates=['year_id'], dtype={'FIPS': object})
# tx_subInj_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_subInj.csv', parse_dates=['year_id'], dtype={'FIPS': object})


def plot_seaborn(df):
    fig, ax = plt.subplots(3, 1, figsize=(8, 5))

    sns.scatterplot(data=df, x='avg_dailyMaxAirTemp_F', y='avg_daily_precip_mm', ax=ax[0])
    sns.lineplot(data=df, x='month_year_short', y='avg_dailyMaxAirTemp_F', ax=ax[1])
    sns.lineplot(data=df, x='month_year_short', y='avg_daily_precip_mm', ax=ax[2])
    plt.title('Test Plot')
    plt.tight_layout()

    return fig

def plot_county_heatmaps(df, year=1989, metric='avg_daily_precip_mm'):
    state = df['state_abbrv'].unique()[0]
    state_df = df[df['year'] == year]
    title_string = "Avg Rainfall in " + state + " " + str(year)
    fig = px.choropleth(
        data_frame=state_df,
        locations='FIPS', geojson=geo_counties,
        width=900, height=600,
        scope='usa',
        color=metric,
        title=str(state) + " Precip Heatmap"
    )
    #fig.update_layout(margin={'r': 0, 't':0, 'l': 0, 'b':0})

    return fig

def plot_mortality_heatmaps(disease, cause_of_death, chosen_year, sex):
    
    disease['year'] = disease['year_id'].dt.year

    df_plot = disease[(disease['sex'] == sex) & (disease['year'] == chosen_year) & (disease['cause_name'] == cause_of_death)]
    #df_plot = disease[(disease['sex'] == sex) & (disease['cause_name'] == cause_of_death)]

    fig = px.choropleth(
        data_frame=df_plot,
        locations='FIPS', geojson=geo_counties,
        #width=900, height=600,
        hover_name='FIPS',
        color='mx',
        center={'lat': 31.9686, 'lon': -99.9018},
        scope='usa',
        #zoom=5,
        title=cause_of_death + "  Heatmap"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        legend_yanchor="top",
        legend_x=-2
    )

    return fig



def plot_mortality_lines(df, sex):
    df_plot = df[df['sex'] == sex]
    plot_title = 'US Diseases Mortality - 1980 - 2014 (' + sex + ')'

    # grouping rates of infectious disease mortality
    fig, ax = plt.subplots(figsize=(30, 12))
    #fig.suptitle("Infectious Disease Mortality by Sex")
    ax.set_title(plot_title, fontdict={'fontsize': 30, 'fontweight': 25}, pad=15)
    df_plot.groupby(['year_id','cause_name']).mean()['mx'].unstack().plot(ax=ax)
    ax.set_xlabel('Year', fontdict={'fontsize': 25, 'fontweight': 25}, labelpad=15)
    ax.set_ylabel('Deaths per 100K', fontdict={'fontsize': 25, 'fontweight': 25}, labelpad=15)
    plt.tight_layout()

    return fig


def plot_kmeans_choropleth(df):
    fig = px.choropleth(
        data_frame=df,
        locations='fips', geojson=geo_counties,
        scope='usa',
        color='labels_small',
        title="K Means Clustering"
    )
    return fig

#def plot_heatwaves(df):


def plot_timeline(df, x, y):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(data=data, x=x, y=y, ax=ax)
    plt.title('Test')
    plt.tight_layout()

    return fig


def plot_cvd_stats(df, disease):
    fig, ax = plt.subplots(3, 1, figsize=(8, 5))

    sns.scatterplot(data=df, x='avg_dailyMaxAirTemp_F', y='avg_daily_precip_mm', ax=ax[0])
    sns.lineplot(data=df, x='month_year_short', y='avg_dailyMaxAirTemp_F', ax=ax[1])
    sns.lineplot(data=df, x='month_year_short', y='avg_daily_precip_mm', ax=ax[2])
    plt.title('Test Plot')
    plt.tight_layout()

    return fig

##### CLIMATE PLOTTING FUNCTIONS

def plot_hw_days_choropleth(df):
    df['year_string'] = df['Year'].dt.year
    #df_plot = df
    #df_plot = df[df['year_string'] == year]

    fig = px.choropleth(
    data_frame=df,
    locations='County Code', geojson=geo_counties,
    #width=900, height=600,
    scope='usa',
    #animation_frame='Year',
    hover_name='County Code',
    color='count_hwDays_onDailyMaxTemp',
    color_continuous_scale="Viridis",
    title="Heat Wave Choropleth"
)

    return fig

def plot_precip_lines(climate_df):
    
    fig, ax = plt.subplots(1, 2, figsize=(30, 12))

    ax[0].set_title("Average Daily Max Air Temperature, Texas: Temperature 1980 - 2014", fontdict={'fontsize': 30, 'fontweight': 25}, pad=15)
    sns.lineplot(data=climate_df, x='month_year_long', y='avg_dailyMaxAirTemp_F', ax=ax[0])

    ax[1].set_title("Average Daily Precip (mm), Texas: 1980 - 2014", fontdict={'fontsize': 30, 'fontweight': 25}, pad=15)
    sns.lineplot(data=climate_df, x='month_year_long', y='avg_daily_precip_mm', ax=ax[1])

    return fig
### END CLIMATE PLOTTING FUCNTIONS


### DEMOGARPHICS HEATMAP
# demographic_variables = ['Median Age', '% Pop < 18', '% Pop > 65', 'Unemployment Rate', '% Pop Below Poverty', 'Uninsured Population', 'Rural/Urban Continuum', 'Obesity Rate per 100K']
# demographic_variables = ['Median Age', '% Pop < 18', '% Pop > 65', 'Unemployment Rate', 'Uninsured Population', 'Rural/Urban Continuum']

def demographics_heatmap(df, metric):
    if metric == 'Median Age':
        var = 'median_age'
    elif metric == '% Pop < 18':
        var = 'under_18_percent'
    elif metric == '% Pop > 65':
        var = 'over_65_percent'
    elif metric == 'Unemployment Rate':
        var = 'unemployment_rate_2019'
    elif metric == '% Pop Below Poverty':
        var = 'percent_below_poverty'
    elif metric == 'Uninsured Population':
        var = 'uninsured_2019'
    elif metric == 'Rural/Urban Continuum':
        var = 'Metro2013'
    elif metric == 'Obesity Rate per 100K':
        var = 'mx'
    

    fig = px.choropleth(
    data_frame=df,
    locations='fips', geojson=geo_counties,
    #width=900, height=600,
    scope='usa',
    center={'lat': 31.9686, 'lon': -99.9018},
    color=var,
    hover_name='county',
    color_continuous_scale="Viridis",
    title="Demographics Choropleth"
)
    fig.update_geos(fitbounds="locations", visible=False)
    return fig