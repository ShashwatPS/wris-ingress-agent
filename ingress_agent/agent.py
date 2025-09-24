# import requests
# import json
# from typing import Dict, Any
# from google.adk.agents import Agent

# def get_wind_direction_data(state_name: str, district_name: str, agency_name: str = "CWC", 
#                            start_date: str = "2024-01-01", end_date: str = "2024-01-05") -> Dict[str, Any]:
#     """
#     Retrieves wind direction data from WRIS API for specified location and date range.
    
#     Args:
#         state_name (str): Name of the state (e.g., "Maharashtra")
#         district_name (str): Name of the district (e.g., "Pune")
#         agency_name (str): Agency name (default: "CWC")
#         start_date (str): Start date in YYYY-MM-DD format
#         end_date (str): End date in YYYY-MM-DD format
        
#     Returns:
#         dict: status and result or error message
#     """
    
#     base_url = "https://indiawris.gov.in"
#     url = f"{base_url}/Dataset/Wind Direction"
    
#     params = {
#         'stateName': state_name,
#         'districtName': district_name,
#         'agencyName': agency_name,
#         'startdate': start_date,
#         'enddate': end_date,
#         'download': 'false',
#         'page': 0,
#         'size': 10
#     }
    
#     headers = {
#         'accept': 'application/json'
#     }
    
#     try:
#         response = requests.post(url, headers=headers, params=params, data='')
        
#         if response.status_code == 200:
#             data = response.json()
#             return {
#                 "status": "success",
#                 "data": data,
#                 "summary": f"Retrieved wind direction data for {district_name}, {state_name}. Total records: {data.get('totalElements', 0)}"
#             }
#         else:
#             return {
#                 "status": "error",
#                 "error_message": f"API request failed with status {response.status_code}: {response.text}"
#             }
            
#     except Exception as e:
#         return {
#             "status": "error",
#             "error_message": f"Exception occurred while fetching data: {str(e)}"
#         }

# def get_ground_water_level_data(state_name: str, district_name: str, agency_name: str = "CWC",
#                                start_date: str = "2024-01-01", end_date: str = "2024-01-05") -> Dict[str, Any]:
#     """
#     Retrieves ground water level data from WRIS API for specified location and date range.
    
#     Args:
#         state_name (str): Name of the state (e.g., "Maharashtra")
#         district_name (str): Name of the district (e.g., "Pune")
#         agency_name (str): Agency name (default: "CWC")
#         start_date (str): Start date in YYYY-MM-DD format
#         end_date (str): End date in YYYY-MM-DD format
        
#     Returns:
#         dict: status and result or error message
#     """
    
#     base_url = "https://indiawris.gov.in"
#     url = f"{base_url}/Dataset/Ground Water Level"
    
#     params = {
#         'stateName': state_name,
#         'districtName': district_name,
#         'agencyName': agency_name,
#         'startdate': start_date,
#         'enddate': end_date,
#         'download': 'false',
#         'page': 0,
#         'size': 10
#     }
    
#     headers = {
#         'accept': 'application/json'
#     }
    
#     try:
#         response = requests.post(url, headers=headers, params=params, data='')
        
#         if response.status_code == 200:
#             data = response.json()
#             return {
#                 "status": "success",
#                 "data": data,
#                 "summary": f"Retrieved ground water level data for {district_name}, {state_name}. Total records: {data.get('totalElements', 0)}"
#             }
#         else:
#             return {
#                 "status": "error",
#                 "error_message": f"API request failed with status {response.status_code}: {response.text}"
#             }
            
#     except Exception as e:
#         return {
#             "status": "error",
#             "error_message": f"Exception occurred while fetching data: {str(e)}"
#         }

# def get_rainfall_data(state_name: str, district_name: str, agency_name: str = "CWC",
#                      start_date: str = "2024-01-01", end_date: str = "2024-01-05") -> Dict[str, Any]:
#     """
#     Retrieves rainfall data from WRIS API for specified location and date range.
    
#     Args:
#         state_name (str): Name of the state (e.g., "Maharashtra")
#         district_name (str): Name of the district (e.g., "Pune")
#         agency_name (str): Agency name (default: "CWC")
#         start_date (str): Start date in YYYY-MM-DD format
#         end_date (str): End date in YYYY-MM-DD format
        
#     Returns:
#         dict: status and result or error message
#     """
    
#     base_url = "https://indiawris.gov.in"
#     url = f"{base_url}/Dataset/RainFall"
    
#     params = {
#         'stateName': state_name,
#         'districtName': district_name,
#         'agencyName': agency_name,
#         'startdate': start_date,
#         'enddate': end_date,
#         'download': 'false',
#         'page': 0,
#         'size': 10
#     }
    
#     headers = {
#         'accept': 'application/json'
#     }
    
#     try:
#         response = requests.post(url, headers=headers, params=params, data='')
        
#         if response.status_code == 200:
#             data = response.json()
#             return {
#                 "status": "success",
#                 "data": data,
#                 "summary": f"Retrieved rainfall data for {district_name}, {state_name}. Total records: {data.get('totalElements', 0)}"
#             }
#         else:
#             return {
#                 "status": "error",
#                 "error_message": f"API request failed with status {response.status_code}: {response.text}"
#             }
            
#     except Exception as e:
#         return {
#             "status": "error",
#             "error_message": f"Exception occurred while fetching data: {str(e)}"
#         }

# # Create the root agent for INGRES/WRIS data access
# root_agent = Agent(   
#     name="ingres_wris_agent",
#     model="gemini-2.0-flash",
#     description=(
#         "AI-driven ChatBot agent for accessing groundwater and water resource data from WRIS APIs. "
#         "This agent helps users query wind direction, ground water levels, rainfall data, and other "
#         "water resource information for different states and districts in India."
#     ),
#     instruction=(
#         "You are an intelligent virtual assistant for the INGRES (India Ground Water Resource Estimation System) project. "
#         "You help users access groundwater and water resource data through WRIS APIs. "
#         "You can provide wind direction data, ground water level information, and rainfall data for various locations across India. "
#         "When users ask about groundwater data, water levels, or weather patterns, use the appropriate tools to fetch real-time data. "
#         "Always provide clear summaries of the data and explain what the results mean in the context of groundwater management. "
#         "If users ask about groundwater categories (Safe, Semi-Critical, Critical, Over-Exploited), provide relevant context about groundwater assessment."
#     ),
#     tools=[get_wind_direction_data, get_ground_water_level_data, get_rainfall_data],
# )


# ingress_agent/agent.py

from google.adk.agents import Agent
from .tools.admin_hierarchy_tools import (
    get_wind_direction_data,
    get_temperature_data,
    get_suspended_sediment_data,
    get_solar_radiation_data,
    get_soil_moisture_data,
    get_snowfall_data,
    get_river_water_level_data,
    get_river_water_discharge_data,
    get_reservoir_data,
    get_relative_humidity_data,
    get_rainfall_data,
    get_ground_water_level_data,
    get_evapo_transpiration_data,
    get_atmospheric_pressure_data
)
from .tools.basin_hierarchy_tools import (
    get_basin_wind_direction_data,
    get_basin_temperature_data,
    get_basin_suspended_sediment_data,
    get_basin_solar_radiation_data,
    get_basin_soil_moisture_data,
    get_basin_snowfall_data,
    get_basin_river_water_level_data,
    get_basin_river_water_discharge_data,
    get_basin_reservoir_data,
    get_basin_relative_humidity_data,
    get_basin_rainfall_data,
    get_basin_evapo_transpiration_data,
    get_basin_atmospheric_pressure_data
)

root_agent = Agent(
    name="ingres_wris_agent",
    model="gemini-2.0-flash",
    description="AI-driven ChatBot agent for INGRES (India Ground Water Resource Estimation System) - currently using WRIS APIs for data access.",
    instruction=(
        "You are an intelligent assistant for INGRES (India Ground Water Resource Estimation System), "
        "developed by CGWB and IIT Hyderabad. INGRES is used for the Assessment of Dynamic Ground Water Resources of India, "
        "conducted annually by the Central Ground Water Board (CGWB) and State/UT Ground Water Departments.\n\n"

        "**Current Status**: The native INGRES APIs are under development and will be available in future iterations. "
        "For now, I am using WRIS (Water Resources Information System) APIs to provide you with water resource data "
        "that simulates the type of information INGRES will eventually provide directly.\n\n"

        "**What I Can Do**:\n"
        "When users ask about your capabilities, dynamically list all available tools/functions you have access to, "
        "organized by categories. Group the tools logically (e.g., meteorological data, hydrological data, "
        "groundwater & soil data, etc.) and present them in a clear, comprehensive format. "
        "Do not hardcode specific data types - instead, examine your available tools and present their "
        "functionality to the user.\n\n"

        "I can access this data using two hierarchy approaches:\n"
        "1. **Administrative Hierarchy**: By State, District, and Agency\n"
        "2. **Basin Hierarchy**: By Basin and Tributary\n\n"

        "**How to Use**:\n"
        "Simply tell me what data you need along with:\n"
        "• State and District names (for admin hierarchy), OR\n"
        "• Basin and Tributary names (for basin hierarchy)\n"
        "• Agency name (defaults to 'CWC' if not specified)\n"
        "• Start and end dates (recent dates used if not provided)\n\n"

        "**Instructions for Tool Usage**:\n"
        "Always attempt to call the appropriate tool with the parameters provided by the user. "
        "Do not make assumptions about the validity of location names or parameters. "
        "If a required parameter is missing, ask the user to provide it.\n\n"

        "If the API call is successful, provide a clear summary of the results. "
        "If the API call returns an error, inform the user that the request could not be fulfilled "
        "and suggest they try again with different parameters. The provided location names or "
        "parameters might be incorrect.\n\n"

        "Remember: You are part of the INGRES ecosystem, working towards making groundwater resource "
        "data more accessible for planners, researchers, policymakers, and the general public."
    ),
    tools=[
        get_wind_direction_data,
        get_temperature_data,
        get_suspended_sediment_data,
        get_solar_radiation_data,
        get_soil_moisture_data,
        get_snowfall_data,
        get_river_water_level_data,
        get_river_water_discharge_data,
        get_reservoir_data,
        get_relative_humidity_data,
        get_rainfall_data,
        get_ground_water_level_data,
        get_evapo_transpiration_data,
        get_atmospheric_pressure_data,
        get_basin_wind_direction_data,
        get_basin_temperature_data,
        get_basin_suspended_sediment_data,
        get_basin_solar_radiation_data,
        get_basin_soil_moisture_data,
        get_basin_snowfall_data,
        get_basin_river_water_level_data,
        get_basin_river_water_discharge_data,
        get_basin_reservoir_data,
        get_basin_relative_humidity_data,
        get_basin_rainfall_data,
        get_basin_evapo_transpiration_data,
        get_basin_atmospheric_pressure_data
    ]
)