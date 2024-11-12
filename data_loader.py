import json
import streamlit as st
import pandas as pd
import re

# Will handle the philippines geographic data structure
def load_geojson(option_level):
        if option_level == 'Region':
            # Load the GeoJSON file
            with open('Population Dataset/PHRegions.json', 'r') as f:
                geo_data = json.load(f)
            return geo_data
        elif option_level == 'Province/Districts':
            with open('Population Dataset/PH_MuniDist_Simplified.json', 'r') as f:
                geo_data = json.load(f)
            return geo_data
        elif option_level == 'Municipality':
            return 

def load_population(selected_year , option_level , option_island): 
    if option_level == 'Region':
        if option_island == 'Luzon': 
            population = pd.read_csv('Population Dataset/Luzon-Region-Population_Cleaned.csv')
            df = pd.DataFrame(population)
            # change location name of MIMAROPA to Mimaropa only 
            df.loc[df['Name'] == 'MIMAROPA', 'Name'] = 'Mimaropa'
            ''' 
            Clean Data
            - Change  Selected Year or Population census from FLOAT to Object
            '''
            df[selected_year] = df[selected_year].str.replace(',', '').astype(float)
            # initializing the requested year of population and name of region 
            data = {'location': df['Name'].tolist(), "values": df[selected_year].tolist()}
            return data 
        
        elif option_island == 'Visayas':    
            # Read Data
            population = pd.read_csv('Population Dataset/Visayas-Region-Population.csv')
            # 
            population[selected_year] = population[selected_year].str.replace(',', '').astype(int)
            # 
            data = {'location': population['Name'].tolist(), "values": population[selected_year].tolist()}
            return data
        elif option_island == 'Mindanao':
            # Population Load
            population = pd.read_csv('Population Dataset/Mindanao-Region-Population.csv')
            df = pd.DataFrame(population)
            # Load Year and Turn in
            # Initialize the data needed
            data = {'location': df['Name'].tolist(), "values": df[selected_year].tolist()}
            # Return data
            return data
    elif option_level == 'Province/Districts':
        if option_island == 'Luzon':
            provinces = pd.read_csv('Population Dataset/Luzon-Province-Population_Cleaned.csv')
            # Convert Selected Year to Float
            provinces[selected_year] = provinces[selected_year].str.replace(',', '').astype(float)
            # Remove parentheses on names 
            provinces['Name'] = provinces['Name'].apply(lambda x: re.sub(r'\s*\(.*?\)\s*', '', x).strip())
            data = {'location': provinces['Name'].tolist(), "values": provinces[selected_year].tolist()}
            return data
        if option_island == 'Mindanao':
            
            return
        
        
def load_luzon_province(selected_year): 
    # Get the data population
    provinces = pd.read_csv('Population Dataset/Luzon-Province-Population_Cleaned.csv')
    
    # Convert Selected Year to Float
    provinces[selected_year] = provinces[selected_year].str.replace(',', '').astype(float)
    # Remove parentheses on names 
    provinces['Name'] = provinces['Name'].apply(lambda x: re.sub(r'\s*\(.*?\)\s*', '', x).strip())
    
    return provinces
# def load_luzon_province(selected_province): 
#     # Acuqire the data
#     provinces = pd.read_csv('Population Dataset/Luzon-Province-Population_Cleaned.csv')
#     # Instantiate the Province Column and current province
#     df['Province'] = pd.NA
#     # Current province will be the value of the province in the iteration
#     current_province = None
#     for index,row  in df.iterrows(): 
#         if row['Status'] == 'Province': 
#             current_province = row['Name']
#         df.at[index, 'Province'] = current_province
#     df = pd.DataFrame(provinces)
#     return df

def load_grdp_plain(): 
    
    grdp = pd.read_csv('Macroeconomics Dataset/GRDP-2000.csv')

    grdp.rename(columns={"Unnamed: 0": "Region Name"}, inplace=True)

    return grdp


def load_grdp(selected_year): 
    
    df = load_grdp_plain()

    data = {'location': df['Region Name'].tolist(), "values": df[selected_year].tolist()}
    
    return data

    
def load_GRDP_length():
    
    data = load_grdp_plain()
    
    return data.columns.drop('Region Name').tolist()