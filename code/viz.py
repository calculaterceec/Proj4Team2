import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
from urllib.request import urlopen
import json


df_INF_TX = pd.read_csv('C:\\Users\\marcj\\OneDrive\\dsir-907\\Proj4Team2\\data\\03_health_data\\Infectious_Disease_Texas.csv')
df_RESP_TX = pd.read_csv('C:\\Users\\marcj\\OneDrive\\dsir-907\\Proj4Team2\\data\\03_health_data\\Respiratory_Disease_Texas.csv')
df_CVD_TX = pd.read_csv('C:\\Users\\marcj\\OneDrive\\dsir-907\\Proj4Team2\\data\\03_health_data\\Viral_Disease_Texas.csv')
df_OBES_TX = pd.read_csv('C:\\Users\\marcj\\OneDrive\\dsir-907\\Proj4Team2\\data\\03_health_data\\Obesity_Texas.csv')

st.title("Climate Change Data Visualization")
st.header("Tool to compare and visualze data related to Climate Change")


st.subheader()


with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

option1 = st.selectbox('Choose an Affliction to plot', 
('Email', 'Home phone', 'Mobile phone'))

option2 = st.selectbox('Choose a County in Texas', 
('Email', 'Home phone', 'Mobile phone'))

#Graph type 2 (Pick Affliction, and County)
def Infection_Bargraph(Infection, County):
    plt.figure(figsize=(10,8))
    plt.bar(df_INF_TX[(df_INF_TX['location_name']==County) & (df_INF_TX['cause_name']==Infection) & (df_INF_TX['year_id']>=1990)]['year_id'],
    df_INF_TX[(df_INF_TX['location_name']==County) & (df_INF_TX['cause_name']==Infection) & (df_INF_TX['year_id']>=1990)]['mx'])
    plt.xticks(np.arange(1990, 2015, 1.0), rotation=45)
    plt.title(Infection + " In " + County + " Texas from 1990 to 2015");

def Viral_Bargraph(Infection, County):
    plt.figure(figsize=(10,8))
    plt.bar(df_CVD_TX[(df_CVD_TX['location_name']==County) & (df_CVD_TX['cause_name']==Infection) & (df_CVD_TX['year_id']>=1990)]['year_id'],
    df_CVD_TX[(df_CVD_TX['location_name']==County) & (df_CVD_TX['cause_name']==Infection) & (df_CVD_TX['year_id']>=1990)]['mx'])
    plt.xticks(np.arange(1990, 2015, 1.0), rotation=45)
    plt.title(Infection + " In " + County + " Texas from 1990 to 2015");

def Respiratory_Bargraph(Infection, County):
    plt.figure(figsize=(10,8))
    plt.bar(df_RESP_TX[(df_RESP_TX['location_name']==County) & (df_RESP_TX['cause_name']==Infection) & (df_RESP_TX['year_id']>=1990)]['year_id'],
    df_INF_TX[(df_RESP_TX['location_name']==County) & (df_RESP_TX['cause_name']==Infection) & (df_RESP_TX['year_id']>=1990)]['mx'])
    plt.xticks(np.arange(1990, 2015, 1.0), rotation=45)
    plt.title(Infection + " In " + County + " Texas from 1990 to 2015");

option1 = st.selectbox('Choose an Affliction to see on map', 
('Email', 'Home phone', 'Mobile phone'))


#Graph type 3 (Pick Affliction)
def Infections_Map(Infection):
    fig = px.choropleth(
        data_frame=df_INF_TX[df_INF_TX['cause_name']==Infection],
        locations='FIPS',
        geojson=counties,
        scope="usa",
        color='mx',
        title=Infection + " In Texas by County"
    )

    fig.show()

def Virals_Map(Virus):
    fig = px.choropleth(
        data_frame=df_CVD_TX[df_CVD_TX['cause_name']==Virus],
        locations='FIPS',
        geojson=counties,
        scope="usa",
        color='mx',
        title=Virus + " In Texas by County"
    )

    fig.show()

def Respiratory_Map(Resp):
    fig = px.choropleth(
        data_frame=df_RESP_TX[df_RESP_TX['cause_name']==Resp],
        locations='FIPS',
        geojson=counties,
        scope="usa",
        color='mx',
        title=Resp + " In Texas by County"
    )

    fig.show()

def Obesity_Map(year):
    fig = px.choropleth(
        data_frame=df_OBES_TX,
        locations='FIPS',
        geojson=counties,
        scope="usa",
        color= 'Prevalence ' + year + ' (%)',
        title= "Obesity Prevelance in Texas Counties in " + year
    )

    fig.show()