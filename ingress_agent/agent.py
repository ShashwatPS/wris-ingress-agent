import requests
import json
from typing import Dict, Any
from google.adk.agents import Agent

def get_wind_direction_data(state_name: str, district_name: str, agency_name: str = "CWC", 
                           start_date: str = "2024-01-01", end_date: str = "2024-01-05") -> Dict[str, Any]:
    """
    Retrieves wind direction data from WRIS API for specified location and date range.
    
    Args:
        state_name (str): Name of the state (e.g., "Maharashtra")
        district_name (str): Name of the district (e.g., "Pune")
        agency_name (str): Agency name (default: "CWC")
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        dict: status and result or error message
    """
    
    base_url = "https://indiawris.gov.in"
    url = f"{base_url}/Dataset/Wind Direction"
    
    params = {
        'stateName': state_name,
        'districtName': district_name,
        'agencyName': agency_name,
        'startdate': start_date,
        'enddate': end_date,
        'download': 'false',
        'page': 0,
        'size': 10
    }
    
    headers = {
        'accept': 'application/json'
    }
    
    try:
        response = requests.post(url, headers=headers, params=params, data='')
        
        if response.status_code == 200:
            data = response.json()
            return {
                "status": "success",
                "data": data,
                "summary": f"Retrieved wind direction data for {district_name}, {state_name}. Total records: {data.get('totalElements', 0)}"
            }
        else:
            return {
                "status": "error",
                "error_message": f"API request failed with status {response.status_code}: {response.text}"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Exception occurred while fetching data: {str(e)}"
        }

def get_ground_water_level_data(state_name: str, district_name: str, agency_name: str = "CWC",
                               start_date: str = "2024-01-01", end_date: str = "2024-01-05") -> Dict[str, Any]:
    """
    Retrieves ground water level data from WRIS API for specified location and date range.
    
    Args:
        state_name (str): Name of the state (e.g., "Maharashtra")
        district_name (str): Name of the district (e.g., "Pune")
        agency_name (str): Agency name (default: "CWC")
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        dict: status and result or error message
    """
    
    base_url = "https://indiawris.gov.in"
    url = f"{base_url}/Dataset/Ground Water Level"
    
    params = {
        'stateName': state_name,
        'districtName': district_name,
        'agencyName': agency_name,
        'startdate': start_date,
        'enddate': end_date,
        'download': 'false',
        'page': 0,
        'size': 10
    }
    
    headers = {
        'accept': 'application/json'
    }
    
    try:
        response = requests.post(url, headers=headers, params=params, data='')
        
        if response.status_code == 200:
            data = response.json()
            return {
                "status": "success",
                "data": data,
                "summary": f"Retrieved ground water level data for {district_name}, {state_name}. Total records: {data.get('totalElements', 0)}"
            }
        else:
            return {
                "status": "error",
                "error_message": f"API request failed with status {response.status_code}: {response.text}"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Exception occurred while fetching data: {str(e)}"
        }

def get_rainfall_data(state_name: str, district_name: str, agency_name: str = "CWC",
                     start_date: str = "2024-01-01", end_date: str = "2024-01-05") -> Dict[str, Any]:
    """
    Retrieves rainfall data from WRIS API for specified location and date range.
    
    Args:
        state_name (str): Name of the state (e.g., "Maharashtra")
        district_name (str): Name of the district (e.g., "Pune")
        agency_name (str): Agency name (default: "CWC")
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        dict: status and result or error message
    """
    
    base_url = "https://indiawris.gov.in"
    url = f"{base_url}/Dataset/RainFall"
    
    params = {
        'stateName': state_name,
        'districtName': district_name,
        'agencyName': agency_name,
        'startdate': start_date,
        'enddate': end_date,
        'download': 'false',
        'page': 0,
        'size': 10
    }
    
    headers = {
        'accept': 'application/json'
    }
    
    try:
        response = requests.post(url, headers=headers, params=params, data='')
        
        if response.status_code == 200:
            data = response.json()
            return {
                "status": "success",
                "data": data,
                "summary": f"Retrieved rainfall data for {district_name}, {state_name}. Total records: {data.get('totalElements', 0)}"
            }
        else:
            return {
                "status": "error",
                "error_message": f"API request failed with status {response.status_code}: {response.text}"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Exception occurred while fetching data: {str(e)}"
        }

# Create the root agent for INGRES/WRIS data access
root_agent = Agent(
    name="ingres_wris_agent",
    model="gemini-2.0-flash",
    description=(
        "AI-driven ChatBot agent for accessing groundwater and water resource data from WRIS APIs. "
        "This agent helps users query wind direction, ground water levels, rainfall data, and other "
        "water resource information for different states and districts in India."
    ),
    instruction=(
        "You are an intelligent virtual assistant for the INGRES (India Ground Water Resource Estimation System) project. "
        "You help users access groundwater and water resource data through WRIS APIs. "
        "You can provide wind direction data, ground water level information, and rainfall data for various locations across India. "
        "When users ask about groundwater data, water levels, or weather patterns, use the appropriate tools to fetch real-time data. "
        "Always provide clear summaries of the data and explain what the results mean in the context of groundwater management. "
        "If users ask about groundwater categories (Safe, Semi-Critical, Critical, Over-Exploited), provide relevant context about groundwater assessment."
    ),
    tools=[get_wind_direction_data, get_ground_water_level_data, get_rainfall_data],
)