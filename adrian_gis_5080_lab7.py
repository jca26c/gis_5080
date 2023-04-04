# Check geemap installation
import subprocess

try:
    import geemap
except ImportError:
    print('geemap package is not installed. Installing ...')
    subprocess.check_call(["python", '-m', 'pip', 'install', 'geemap'])

 # Import libraries
import os
import streamlit as st
import ee
import geemap
import geemap.foliumap as geemap
import ipywidgets as widgets
from bqplot import pyplot as plt
from ipyleaflet import WidgetControl

# Create an interactive map
Map = geemap.Map(center=[40, -100], zoom=4, add_google_map=False)
Map.add_basemap('HYBRID')
Map.add_basemap('ROADMAP')

# Add Earth Engine data
fc = ee.FeatureCollection('TIGER/2018/Counties')
Map.addLayer(fc, {}, 'US Counties')

states = ee.FeatureCollection('TIGER/2018/States')
#Map
Map.to_streamlit()

# Create suite of buttons
submit = st.button("Submit")
state = st.text_input("State:", "Tennesse")
county = st.text_input("County:", "Knox")
user_radio = st.radio("Use user-drawn AOI",(""))
download_radio = st.radio("Download chart data",(""))
band_combo = st.selectbox(
    'Band combo',
    ('Red/Green/Blue', 'NIR/Red/Green',  'SWIR2/SWIR1/NIR', 'NIR/SWIR1/Red','SWIR2/NIR/Red', 
             'SWIR2/SWIR1/Red', 'SWIR1/NIR/Blue', 'NIR/SWIR1/Blue', 'SWIR2/NIR/Green', 'SWIR1/NIR/Red'))
year_widget = st.slider("Selected year:", min_value=1984, max_value=2020, value=2010)
mask_radio = st.radio("Apply fmask(remove cloud, shadow, snow)",(""))
index = st.selectbox(
    'Normalized Difference Indes:',
    ('Vegetation Index (NDVI)', 
              'Water Index (NDWI)',
              'Modified Water Index (MNDWI)',
              'Snow Index (NDSI)',
              'Soil Index (NDSI)',
              'Burn Ratio (NBR)',
              'Customized'))
first_band = st.selectbox(
    '1st band',
    ('Blue', 'Green','Red','NIR', 'SWIR1', 'SWIR2'))
second_band = st.selectbox(
    '2nd band',
    ('Blue', 'Green','Red','NIR', 'SWIR1', 'SWIR2'))
threshold = st.slider("Threshold:", min_value=-1, max_value=1, value=0, step= 0.01)
