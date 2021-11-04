import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import altair as alt


# load the climate data by state
def get_states():
    df = pd.read_csv('./data/01_climate_data/01_climate_data_CLEAN/precip_airTemp_wFIPS_1979_2011.zip', parse_dates=['month_year_short'], dtype={'FIPS': object})
    states = df['state_abbrv'].unique()
    return states

def load_climate(state):
    df = pd.read_csv('./data/01_climate_data/01_climate_data_CLEAN/precip_airTemp_wFIPS_1979_2011.zip', parse_dates=['month_year_short'], dtype={'FIPS': object})
    df = df[df['state_abbrv'] == state]
    df['year'] = df['month_year_short'].dt.year

    df = df[['FIPS', 'county_name', 'state_abbrv', 'year', 'month_year_long', 'month_year_short', 'avg_dailyMaxAirTemp_F', 'min_dailyMaxAirTemp_F', 'max_dailyMaxAirTemp_F', 'avg_daily_precip_mm', 'min_daily_precip_mm', 'max_daily_precip_mm']]
    return df
def get_inf_diseases():
    df = pd.read_csv('./data/03 - Health Data/idf_INF.zip', parse_dates=['month_year_short'])
    causes = df['cause_name'].unique()
    return causes

# def load_state_inf(cause, ):
#     df = pd.read_csv('')

