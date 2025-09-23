# tools/admin_hierarchy_tools.py
"""
Tools for accessing WRIS data using admin hierarchy (state/district)
"""

from typing import Dict, Any
from ..utils.wris_client import default_client
from ..utils.data_processor import default_processor

def get_wind_direction_data(state_name: str, district_name: str, agency_name: str, 
                           start_date: str, end_date: str) -> Dict[str, Any]:
    """
    Retrieves wind direction data from WRIS API for specified location and date range.
    
    Args:
        state_name (str): Name of the state (e.g., "Maharashtra")
        district_name (str): Name of the district (e.g., "Pune")
        agency_name (str): Agency name
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        dict: status and result or error message
    """
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='wind_direction',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved wind direction data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
        
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    
    return result

def get_ground_water_level_data(state_name: str, district_name: str, agency_name: str,
                               start_date: str, end_date: str) -> Dict[str, Any]:
    """
    Retrieves ground water level data from WRIS API for specified location and date range.
    
    Args:
        state_name (str): Name of the state (e.g., "Maharashtra")
        district_name (str): Name of the district (e.g., "Pune")
        agency_name (str): Agency name
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        dict: status and result or error message
    """
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='ground_water_level',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved ground water level data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
        
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
                    result['data_quality_score'] = stats.get('data_quality_score', 0)
    
    return result

def get_rainfall_data(state_name: str, district_name: str, agency_name: str,
                     start_date: str, end_date: str) -> Dict[str, Any]:
    """
    Retrieves rainfall data from WRIS API for specified location and date range.
    
    Args:
        state_name (str): Name of the state (e.g., "Maharashtra")
        district_name (str): Name of the district (e.g., "Pune")
        agency_name (str): Agency name
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        dict: status and result or error message
    """
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='rainfall',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved rainfall data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
        
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
                    mean_rainfall = stats['mean']
                    if mean_rainfall < 10:
                        result['rainfall_category'] = 'Very Low'
                    elif mean_rainfall < 25:
                        result['rainfall_category'] = 'Low'
                    elif mean_rainfall < 65:
                        result['rainfall_category'] = 'Moderate'
                    elif mean_rainfall < 115:
                        result['rainfall_category'] = 'Heavy'
                    else:
                        result['rainfall_category'] = 'Very Heavy'
    
    return result

def get_temperature_data(state_name: str, district_name: str, agency_name: str,
                        start_date: str, end_date: str) -> Dict[str, Any]:
    """
    Retrieves temperature data from WRIS API for specified location and date range.
    
    Args:
        state_name (str): Name of the state
        district_name (str): Name of the district
        agency_name (str): Agency name
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        
    Returns:
        dict: API response with status and data
    """
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='temperature',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved temperature data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_suspended_sediment_data(state_name: str, district_name: str, agency_name: str,
                               start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves suspended sediment data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='suspended_sediment',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved suspended sediment data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_solar_radiation_data(state_name: str, district_name: str, agency_name: str,
                            start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves solar radiation data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='solar_radiation',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved solar radiation data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_soil_moisture_data(state_name: str, district_name: str, agency_name: str,
                          start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves soil moisture data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='soil_moisture',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved soil moisture data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_snowfall_data(state_name: str, district_name: str, agency_name: str,
                     start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves snowfall data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='snowfall',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved snowfall data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_river_water_level_data(state_name: str, district_name: str, agency_name: str,
                              start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves river water level data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='river_water_level',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved river water level data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_river_water_discharge_data(state_name: str, district_name: str, agency_name: str,
                                  start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves river water discharge data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='river_water_discharge',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved river water discharge data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_reservoir_data(state_name: str, district_name: str, agency_name: str,
                      start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves reservoir data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='reservoir',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved reservoir data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_relative_humidity_data(state_name: str, district_name: str, agency_name: str,
                              start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves relative humidity data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='relative_humidity',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved relative humidity data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_evapo_transpiration_data(state_name: str, district_name: str, agency_name: str,
                                start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves evapotranspiration data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='evapo_transpiration',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved evapotranspiration data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result

def get_atmospheric_pressure_data(state_name: str, district_name: str, agency_name: str,
                                 start_date: str, end_date: str) -> Dict[str, Any]:
    """Retrieves atmospheric pressure data from WRIS API"""
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_admin_hierarchy_data(
        data_type='atmospheric_pressure',
        state_name=state_name,
        district_name=district_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    
    if result['status'] == 'success':
        result['summary'] = f"Retrieved atmospheric pressure data for {district_name}, {state_name}. Total records: {result.get('total_records', 0)}"
    
    return result