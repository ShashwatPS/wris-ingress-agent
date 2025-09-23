# ingress_agent/utils/wris_client.py

import requests
from urllib.parse import urlencode
import logging

# Use a basic logger for demonstration
Logger = logging.getLogger(__name__)

class WRISClient:
    def __init__(self, base_url="https://indiawris.gov.in", page=0, size=30):
        self.base_url = base_url
        self.default_page = page
        self.default_size = size
        self.headers = {'accept': 'application/json'}

    def get_admin_hierarchy_data(self, data_type, state_name, district_name, agency_name,
                                 start_date, end_date):
        # Map data types to endpoints - EXACTLY like your working version
        endpoint_map = {
            'rainfall': '/Dataset/RainFall',
            'ground_water_level': '/Dataset/Ground Water Level',
            'wind_direction': '/Dataset/Wind Direction',
            'temperature': '/Dataset/Temperature',
            'suspended_sediment': '/Dataset/Suspended Sediment',
            'solar_radiation': '/Dataset/Solar Radiation',
            'soil_moisture': '/Dataset/Soil Moisture',
            'snowfall': '/Dataset/SnowFall',
            'river_water_level': '/Dataset/River Water Level',
            'river_water_discharge': '/Dataset/River Water Discharge',
            'reservoir': '/Dataset/Reservoir',
            'relative_humidity': '/Dataset/Relative Humidity',
            'evapo_transpiration': '/Dataset/Evapo Transpiration',
            'atmospheric_pressure': '/Dataset/Atmospheric Pressure'
        }
        
        endpoint = endpoint_map.get(data_type)
        if not endpoint:
            return {"status": "error", "error_message": f"Unknown data type: {data_type}"}
        
        # Build URL EXACTLY like your working version
        url = f"{self.base_url}{endpoint}"
        
        # Prepare the query parameters
        params = {
            'stateName': state_name,
            'districtName': district_name,
            'agencyName': agency_name,
            'startdate': start_date,
            'enddate': end_date,
            'download': 'false',
            'page': self.default_page,
            'size': self.default_size
        }

        try:
            print(f"Requesting WRIS Admin Data: {url}")
            # Use POST exactly like your working version
            resp = requests.post(url, headers=self.headers, params=params, data='')
            
            print(f"Response Status Code: {resp.status_code}")
            
            if resp.status_code == 200:
                data = resp.json()
                Logger.info(f"WRIS Admin Data Retrieved: {data}")
                return {
                    "status": "success",
                    "data": data,
                    "total_records": data.get("totalElements", 0)
                }
            else:
                return {
                    "status": "error",
                    "error_message": f"API request failed with status {resp.status_code}: {resp.text}"
                }
                
        except requests.exceptions.RequestException as e:
            return {"status": "error", "error_message": f"API request failed: {e}"}
        except Exception as e:
            return {"status": "error", "error_message": f"Exception occurred while fetching data: {str(e)}"}

    def get_basin_hierarchy_data(self, data_type, basin_name, tributary_name, agency_name,
                                 start_date, end_date):
        # Map data types to endpoints - EXACTLY like your working version
        endpoint_map = {
            'suspended_sediment': '/Dataset/Basin/Suspended Sediment',
            'wind_direction': '/Dataset/Basin/Wind Direction',
            'temperature': '/Dataset/Basin/Temperature',
            'solar_radiation': '/Dataset/Basin/Solar Radiation',
            'soil_moisture': '/Dataset/Basin/Soil Moisture',
            'snowfall': '/Dataset/Basin/SnowFall',
            'river_water_level': '/Dataset/Basin/River WaterLevel',
            'river_water_discharge': '/Dataset/Basin/River Water Discharge',
            'reservoir': '/Dataset/Basin/Reservoir',
            'relative_humidity': '/Dataset/Basin/Relative Humidity',
            'rainfall': '/Dataset/Basin/RainFall',
            'evapo_transpiration': '/Dataset/Basin/Evapo Transpiration',
            'atmospheric_pressure': '/Dataset/Basin/Atmospheric Pressure'
        }
        
        endpoint = endpoint_map.get(data_type)
        if not endpoint:
            return {"status": "error", "error_message": f"Unknown data type: {data_type}"}
        
        # Build URL EXACTLY like your working version
        url = f"{self.base_url}{endpoint}"
        
        # Prepare the query parameters
        params = {
            'basinName': basin_name,
            'tributaryName': tributary_name,
            'agencyName': agency_name,
            'startdate': start_date,
            'enddate': end_date,
            'download': 'false',
            'page': self.default_page,
            'size': self.default_size
        }

        try:
            print(f"Requesting WRIS Basin Data: {url}")
            # Use POST exactly like your working version
            resp = requests.post(url, headers=self.headers, params=params, data='')
            
            print(f"Response Status Code: {resp.status_code}")
            print(f"Response Headers: {dict(resp.headers)}")
            
            if resp.status_code == 200:
                data = resp.json()
                print(f"WRIS Basin Data Response: {data}")
                return {
                    "status": "success",
                    "data": data,
                    "total_records": data.get("totalElements", 0)
                }
            else:
                return {
                    "status": "error", 
                    "error_message": f"API request failed with status {resp.status_code}: {resp.text}"
                }
                
        except requests.exceptions.RequestException as e:
            return {"status": "error", "error_message": f"API request failed: {e}"}
        except Exception as e:
            return {"status": "error", "error_message": f"Exception occurred while fetching data: {str(e)}"}

# Use singleton pattern for module-wide client
default_client = WRISClient()