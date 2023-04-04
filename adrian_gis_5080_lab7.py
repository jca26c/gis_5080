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
button = st.button("Submit")
keyword = st.text_input("State:", "Tennesse")
