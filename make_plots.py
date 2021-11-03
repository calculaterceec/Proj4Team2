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
        scope='usa',
        color=metric,
        title=str(state) + " Precip Heatmap"
    )
    #fig.update_layout(margin={'r': 0, 't':0, 'l': 0, 'b':0})

    return fig

def plot_cvd_stats(df, disease):
    fig, ax = plt.subplots(3, 1, figsize=(8, 5))

    sns.scatterplot(data=df, x='avg_dailyMaxAirTemp_F', y='avg_daily_precip_mm', ax=ax[0])
    sns.lineplot(data=df, x='month_year_short', y='avg_dailyMaxAirTemp_F', ax=ax[1])
    sns.lineplot(data=df, x='month_year_short', y='avg_daily_precip_mm', ax=ax[2])
    plt.title('Test Plot')
    plt.tight_layout()

    return fig