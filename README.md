## Project 4 - Team 2
 
**I. Problem Statement**

Using aggregated climate, demographic, and health data, investigate meaningful drivers of health outcomes and create an interactive visualization of the data.

**II. Executive Summary**

In the past nearly two years, informed citizens are more aware of publicy available data and we see daiy COVID-19 trend charts on everything related to the disease.  Analysis of health data has been front and center in our lives. We have been intrigued with this and decided to fashion a workflow for informed citizens to learn for yourself from publicly available health, demographic, and climate datasets. This project will help the reader acquire, analyze, and visualize the data.

**III. Scope Note and Data Sources**

We focused on data that were completely pre-COVID as much of the county-level aggregated climate and demographic data are not yet available for the past two years. We collected data at the county level using Federal Information Processing Standards (FIPS) codes. These are five digit codes that uniquely correspond to all the counties and county-equivalents (independent cities, for example) in the United States. 

A. *Demographic*
    - We obtained data from the [Census Bureau's American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs) 5-year estimates. The ACS is a rolling, annual survey that provides county-level estimates for a variety of demographic characteristics from the previous five years. We included data on population, median household income, race and ethnicity, gender, whether or not a household had broadband, a computer, a smartphone, veteran status, and high school graduation rates. In the methodology section we discuss which variables we ultimately used in the modeling and visualizations as not all of them were useful. [OpenIntro.org](https://www.openintro.org/data/?data=county_complete)

[Background info on the county_complete file.](./data/02_demo_data/openintro_dot_org/county_complete.txt)

- [Setosa.io PCA Visualization](http://setosa.io/ev/principal-component-analysis/)
- [Medium Article: A One-Stop Shop for Principal Component Analysis](https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c)
- [Exceptional StackOverflow Answer to Understanding PCA](http://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues)


**IV. Methodology**

Put that here.
    
**V. Conclusion and Path Forward**

What did we learn? What's next

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

