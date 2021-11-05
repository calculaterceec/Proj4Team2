## Project 4 - Team 2
 
**I. Problem Statement**

Using aggregated climate, demographic, and health data, investigate meaningful drivers of health outcomes and create an interactive visualization of the data.

**II. Executive Summary**

In the past nearly two years, informed citizens are more aware of publicy available data and we see daily COVID-19 trend charts on everything related to the disease.  Analysis of health data has been front and center in our lives. We have been intrigued with this renewed focus and, as a group, are concerned about climate change, its effects on health, and the [disparate access to green space that different neighborhoods have](./background_sources/People_of_color_3_x_more_likely_to_live_in_deprived_neighborhoods.pdfghborhoods.pdf). We chose to focus our project on gathering and examining a host of climate, health, and demographic datasets in order to practice our data science skills. We provide a workflow and provide our Python notebooks for informed citizens to learn how to obtain data from publicly available health, demographic, and climate datasets. We hope that this project will help empower the reader acquire, analyze, and visualize data or interest.

**III. Scope Note and Data Sources**

We focused on data that were completely pre-COVID as much of the county-level aggregated climate and demographic data are not yet available for the past two years. We collected data at the county level using Federal Information Processing Standards (FIPS) codes. These are five-digit codes that uniquely correspond to all the counties and county-equivalents (independent cities, for example) in the United States. For our `streamlit` application, we focused on Texas because of bandwidth, performance, and storage issues. We also looked at Texas for some of our more in-depth analyses.

A. *CLIMATE* - We found county-level climate data on [monthly air temperature](insert link here), [monthly precipitation](insert link here), and [heat wave days](insert link here). Provide some additional information about the climate data here.


B. *DEMOGRAPHIC* - We obtained data from the [Census Bureau's American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs) 2019 5-year estimates. The ACS is a rolling, annual survey that provides county-level estimates for a variety of demographic characteristics from the previous five years. (The Census Bureau will [release](https://www.census.gov/programs-surveys/acs/news/data-releases/2020/release-schedule.html) 2020 5-year estimates in December 2021.)] We included data on population, median household [income](./data/02_demo_data/ACS/ACS_2019_income_by_county/ACSST5Y2019.S1901_metadata_2021-10-05T144610.csv), [poverty](./data/02_demo_data/ACS/ACS_2019_poverty_by_county/ACSST5Y2019.S1701_metadata_2021-11-02T160432.csv), [age and sex](./data/02_demo_data/ACS/ACS_2019_age_and_sex_by_county/ACSST5Y2019.S0101_metadata_2021-10-06T131343.csv), [race and ethnicity](./data/02_demo_data/ACS/ACS_2019_race_and_ethnicity_by_county/ACSDT5Y2019.B02001_metadata_2021-10-08T032031.csv), whether or not a household had broadband, a computer, a smartphone, veteran status, and high school graduation rates. In the methodology section we discuss which variables we ultimately used in the modeling and visualizations as not all of them were useful. The website [OpenIntro.org](https://www.openintro.org/data/?data=county_complete) hosts many datasets that are ready for educational use and had a ready-made `.csv` dataset that included some of the ACS variables of interest, and race percentages that were not readily available from the Census website. We included this file and used a handful of its columns. This [dataset](./data/02_demo_data/openintro_dot_org/county_complete.txt) also had information about what kind, if any, smoking bans were in place as of 2010. 

C. *HEALTH* - The Institute for Health Metrics and Evaluation ([IMHE](http://www.healthdata.org/)) was a rich source of mortality statistics (again, pre-COVID) from cardiovascular, respiratory, and infectious diseases. Data was also collected on obesity prevalence in the U.S. from 2001 to 2011 on the [Globa Health data Exchange website](http://ghdx.healthdata.org/record/ihme-data/united-states-physical-activity-and-obesity-prevalence-county-2001-2011)

D. *COUNTY CLASSIFICATIONS* -The United States Department of Agriculture (USDA)'s Economic Research Office hosts a data [Atlas](https://www.ers.usda.gov/data-products/atlas-of-rural-and-small-town-america/download-the-data/) of Rural and Small-Town America with hundreds of different variables. We chose to include two variables that classified counties as being either a metro area or not, and where the county landed on a rural-urban continuum. 

**IV. Methodology**

A. *DATA ACQUISTIION* - Divide and conquer. Each group member acquired climate, demographic, and health data, respectively. We examined over a a dozen websites--mostly from United States government agencies such as the [Census](https://data.census.gov/cedsci/) Bureau, USDA, [IMHE](http://www.healthdata.org/), the Centers for Disease Control ([CDC](https://www.cdc.gov/)), National Oceanic and Atmospheric Administration ([NOAA](https://www.noaa.gov/)), among others.We set up this public [GitHub](https://github.com/) repository to make the data accessible to others.

B. *DATA CLEANING, MUNGING* - Continuing in the divide and conquer method, each of us cleaned, combined, and "munged" (transformed the data into useful and case-specific forms) our respective data sources. This was by far the most time-consuming aspect of this project since even though we had data in `.csv` format with a unique FIPS identifier on which to combine datasets, not all of the datasets were in a collapsed or pivoted format. For instance, some of the health and climate datasets had millions of rows, one for each county for each year and for each disease or climate measurement. The dataset sizes proved to be challenging for processing and storage. The FIPS codes are five digits but some at the beginning of the alphabet have leading zeroes which were stripped every time the file was read into a new coding notebook. We created workarounds and functions to deal with these challenges and ultimately created several cleaned datasets on [temperature](./data/cleaned/precip_AirTemp_monthly_1979_2011.zip), [heat waves](./data/cleaned/heat_wave_days_1981_2010.csv), [demographics](./data/cleaned/final_demo.csv), health ([respiratory](./data/cleaned/Cleaned_Respiratory_Diseases.csv),  [obesity](./data/cleaned/Cleaned_Obesity_Prevalence.csv), [infectious diseases](./data/cleaned/Cleaned_Infectious_Diseases.csv), and [cardiovascular diseases](./data/cleaned/Cleaned_Cardiovascular_Diseases.csv)), and a [final combined](./data/cleaned/final_combined.csv) dataset for further exploratory analysis and visualization.

C. *EXPLORATORY DATA ANALYSIS* - We examined trends in climate such as average heatwaves per year and average maximum temperature by year. The average maximum temperature by year. have risen more quickly since the late 1970s, approximately 2.34 degrees Fahrenheit higher than the 20th century average. 

D. *INVESTIGATE HIGH MORTALITY DISEASES* - We investigated disease mortality rates in the United States generally and Texas specifically, to include infectious diseases, and we were able to see the upward trend in HIV-AIDS disease mortality with a drop-off occurring after the introduction of antiretroviral therapies in the late 1980s. You can see these graphics in our final [presentation](./project4_team_2_presentation.pdf).

E. *CLUSTER MODELING* We looked at this project as one of exploration rather than prediction, and determined that we could use a k-means clustering model in an attempt to identify any meaningful clusters of counties. In our initial attempt, we threw all the county-level demographic and health variables at our model (we did not include climate data in this clustering due to technical issues) and found that the iterative cluster-selection algorithm recommended only two clusters. We knew this wouldn't be very helpful since it would not be meaningful. Therefore, we removed all features except those related to the `percent_below_poverty`, `smoking_ban_2010`, `unemployment_rate_2019`, `obesity_prev_100K`, and the `rural_urban_continuum_code_2013`. Our algorithm suggested we should cluster the counties into four groups, which we did. You can see the labels with the FIPS codes and features [here](./data/cleaned/kmeans_clusters_with_labels_and_features.csv) Viewing these on a map visually shows some identifiable patterns, though it is not readily clear exactly which variable is driving the clustering. We would need to create additional maps for each of the individual clusters to see if there are obvious patterns. (You can see the k-means clustering choropleth in our [presentation](./project4_team_2_presentation.pdf).)
    
**V. Conclusion and Path Forward**

A. *WHAT DID WE LEARN?* - We showed a general model and workflow for conducting exploratory analysis and join data from different sources, clean it and munge it in a way that made sense for our particular analysis. We did find some unexpected patterns such as a slight upward trend in diarrheal diseases after the late 1990s. We identified variables that we thought might be drivers of health outcomes and started exploring those patterns. We created an interactive visualization of the data via our streamlit app. We do not have this hosted on the web but our repository includes the code for you to launch it from your local machine.

B. *PATH FORWARD* - Given more time, we would investigate a variety of predictive models to predict income, mortality, disease, and climate metrics. We would investigate hosting the interactive on a Tableau dashboard to avoid some of the bandwidth and storage issues we confronted.

**VI. Data**

```python
df_climate

XXXX total entries.
```

|Feature|Type|Dataset|Description|
|---|---|---|---|

|**var1**|*int64*|df_climate|blah blah blah|.

|**var1**|*int64*|df_climate|Eblah blah blah|.

|**var2**|*object*|df_climate|blah blah blah|
|**var3**|*object*|df_climate|blah blah blah|
|**var4**|*object*|df_climate|blah blah blah|
|**var5**|*int64*|df_climate|blah blah blah|



```python
df_demographic
xxxx total entries.
```

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**var1**|*int64*|df_demographic|blah blah blah|.
|**var2**|*object*|df_demographic|blah blah blah|
|**var3**|*object*|df_demographic|blah blah blah|
|**var4**|*object*|df_demographic|blah blah blah|
|**var5**|*int64*|df_demographic|blah blah blah|
|**var6**|*object*|df_demographic|blah blah blah|



df_health
etc.
=======
=======

