# # ingress_agent/utils/wris_client.py

# import requests
# from urllib.parse import urlencode
# import logging

# # Use a basic logger for demonstration
# Logger = logging.getLogger(__name__)

# class WRISClient:
#     def __init__(self, base_url="https://indiawris.gov.in", page=0, size=30):
#         self.base_url = base_url
#         self.default_page = page
#         self.default_size = size
#         self.headers = {'accept': 'application/json'}

#     def get_admin_hierarchy_data(self, data_type, state_name, district_name, agency_name,
#                                  start_date, end_date):
#         # Map data types to endpoints
#         endpoint_map = {
#             'rainfall': '/Dataset/RainFall',
#             'ground_water_level': '/Dataset/Ground Water Level',
#             'wind_direction': '/Dataset/Wind Direction'
#         }
        
#         endpoint = endpoint_map.get(data_type)
#         if not endpoint:
#             return {"status": "error", "error_message": f"Unknown data type: {data_type}"}
        
#         # Prepare the query parameters
#         params = {
#             'stateName': state_name,
#             'districtName': district_name,
#             'agencyName': agency_name,
#             'startdate': start_date,
#             'enddate': end_date,
#             'download': 'false',
#             'page': self.default_page,
#             'size': self.default_size
#         }

#         # Build the full URL
#         full_url = f"{self.base_url}{endpoint}?{urlencode(params)}"

#         try:
#             print(f"Requesting WRIS Admin Data: {full_url}")
#             # Use POST with empty data, headers - exactly like the working curl command
#             resp = requests.post(
#                 full_url, 
#                 headers=self.headers, 
#                 data=''
#             )
            
#             print(f"Response Status Code: {resp.status_code}")
            
#             if resp.status_code == 200:
#                 data = resp.json()
#                 Logger.info(f"WRIS Admin Data Retrieved: {data}")
#                 return {
#                     "status": "success",
#                     "data": data,
#                     "total_records": data.get("totalElements", 0)
#                 }
#             else:
#                 return {
#                     "status": "error",
#                     "error_message": f"API request failed with status {resp.status_code}: {resp.text}"
#                 }
                
#         except requests.exceptions.RequestException as e:
#             return {"status": "error", "error_message": f"API request failed: {e}"}
#         except Exception as e:
#             return {"status": "error", "error_message": f"Exception occurred while fetching data: {str(e)}"}

#     def get_basin_hierarchy_data(self, data_type, basin_name, tributary_name, agency_name,
#                                  start_date, end_date):
#         # Map data types to endpoints
#         endpoint_map = {
#             'suspended_sediment': '/Dataset/Basin/Suspended Sediment'
#         }
        
#         endpoint = endpoint_map.get(data_type)
#         if not endpoint:
#             return {"status": "error", "error_message": f"Unknown data type: {data_type}"}
        
#         # Prepare the query parameters
#         params = {
#             'basinName': basin_name,
#             'tributaryName': tributary_name,
#             'agencyName': agency_name,
#             'startdate': start_date,
#             'enddate': end_date,
#             'download': 'false',
#             'page': self.default_page,
#             'size': self.default_size
#         }

#         # Build the full URL
#         full_url = f"{self.base_url}{endpoint}?{urlencode(params)}"

#         try:
#             print(f"Requesting WRIS Basin Data: {full_url}")
#             # Use POST with empty data, headers - exactly like the working curl command
#             resp = requests.post(
#                 full_url, 
#                 headers=self.headers, 
#                 data=''
#             )
            
#             print(f"Response Status Code: {resp.status_code}")
#             print(f"Response Headers: {dict(resp.headers)}")
            
#             if resp.status_code == 200:
#                 data = resp.json()
#                 print(f"WRIS Basin Data Response: {data}")
#                 return {
#                     "status": "success",
#                     "data": data,
#                     "total_records": data.get("totalElements", 0)
#                 }
#             else:
#                 return {
#                     "status": "error", 
#                     "error_message": f"API request failed with status {resp.status_code}: {resp.text}"
#                 }
                
#         except requests.exceptions.RequestException as e:
#             return {"status": "error", "error_message": f"API request failed: {e}"}
#         except Exception as e:
#             return {"status": "error", "error_message": f"Exception occurred while fetching data: {str(e)}"}

# # Use singleton pattern for module-wide client
# default_client = WRISClient()

# ingress_agent/utils/wris_client.py

import requests
from urllib.parse import urlencode
from .constants import WRIS_BASE_URL, ADMIN_ENDPOINTS, BASIN_ENDPOINTS, DEFAULT_HEADERS
import logging

# Use a basic logger for demonstration
Logger = logging.getLogger(__name__)

class WRISClient:
    def __init__(self, base_url=WRIS_BASE_URL, page=0, size=30):
        # Ensure base_url doesn't end with slash to avoid double slash issues
        self.base_url = base_url.rstrip('/')
        self.default_page = page
        self.default_size = size

    def get_admin_hierarchy_data(self, data_type, state_name, district_name, agency_name,
                                 start_date, end_date):
        endpoint = ADMIN_ENDPOINTS.get(data_type)
        if not endpoint:
            return {"status": "error", "error_message": f"Unknown data type: {data_type}"}
        
        # Remove leading slash from endpoint to avoid double slash
        endpoint = endpoint.lstrip('/')
        
        # Prepare the query parameters - ensure date format is YYYY-MM-DD
        params = {
            'stateName': state_name,
            'districtName': district_name,
            'agencyName': agency_name,
            'startdate': start_date,  # Should be in YYYY-MM-DD format like 2020-08-01
            'enddate': end_date,      # Should be in YYYY-MM-DD format like 2024-03-09
            'download': 'false',
            'page': self.default_page,
            'size': self.default_size
        }

        # Build the full URL
        full_url = f"{self.base_url}{endpoint}?{urlencode(params)}"

        try:
            print(f"Requesting WRIS Admin Data: {full_url}")
            # Use POST with empty data, headers - exactly like the working curl command
            resp = requests.post(
                full_url, 
                headers=DEFAULT_HEADERS, 
                data=''
            )
            
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
        endpoint = BASIN_ENDPOINTS.get(data_type)
        if not endpoint:
            return {"status": "error", "error_message": f"Unknown data type: {data_type}"}
        
        # Remove leading slash from endpoint to avoid double slash
        endpoint = endpoint.lstrip('/')
        
        # Prepare the query parameters - ensure date format is YYYY-MM-DD
        params = {
            'basinName': basin_name,
            'tributaryName': tributary_name,
            'agencyName': agency_name,
            'startdate': start_date,  # Should be in YYYY-MM-DD format like 2020-08-01
            'enddate': end_date,      # Should be in YYYY-MM-DD format like 2024-03-09  
            'download': 'false',
            'page': self.default_page,
            'size': self.default_size
        }

        # Build the full URL
        full_url = f"{self.base_url}{endpoint}?{urlencode(params)}"

        try:
            print(f"Requesting WRIS Basin Data: {full_url}")
            # Use POST with empty data, headers - exactly like the working curl command
            resp = requests.post(
                full_url, 
                headers=DEFAULT_HEADERS, 
                data=''
            )
            
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