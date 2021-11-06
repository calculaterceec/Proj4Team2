import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



# load in the health data. Accepts a string that says what kind of data is desired, 
# and uses and if/elif statement to load the corresponding dataset
def load_health_data(health_source):
    if health_source == 'Cardiovascular Disease':
        disease_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_cvd.csv', parse_dates=['year_id'], dtype={'FIPS': object})
    elif health_source == 'Infectious Diseases':
        disease_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_inf.csv', parse_dates=['year_id'], dtype={'FIPS': object})
    elif health_source == 'Respiratory Diseases':
        disease_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_resp.csv', parse_dates=['year_id'], dtype={'FIPS': object})
    elif health_source == 'Substance Abuse & Self Injury':
        disease_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_subInj.csv', parse_dates=['year_id'], dtype={'FIPS': object})

    return disease_df

# returns the climate data ('precip, and air temp)
def load_climate():
    df = pd.read_csv('./data/01_climate_data/01_climate_data_CLEAN/precip_airTemp_wFIPS_1979_2011.zip', parse_dates=['month_year_short'], dtype={'FIPS': object})
    #df = df[df['state_abbrv'] == state]
    df['year'] = df['month_year_short'].dt.year

    df = df[['FIPS', 'county_name', 'state_abbrv', 'year', 'month_year_long', 'month_year_short', 'avg_dailyMaxAirTemp_F', 'min_dailyMaxAirTemp_F', 'max_dailyMaxAirTemp_F', 'avg_daily_precip_mm', 'min_daily_precip_mm', 'max_daily_precip_mm']]
    return df

# demographic data 
def load_demographics():
    df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_demographics.csv',dtype={'fips': object})
    return df

# heat wave data
def load_heat_wave():
    df = tx_heat_wave_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_heat_wave.csv', parse_dates=['Year'], dtype={'County Code': object})
    return df
# def load_state_inf(cause, ):
#     df = pd.read_csv('')

def load_kmeans():
    df = pd.read_csv('../data/cleaned/kmeans_clusters_with_labels_and_features.csv',dtype={'fips': object})
    return df

