# ingress_agent/tools/basin_hierarchy_tools.py

"""
Tools for accessing WRIS data using basin hierarchy (basin/tributary)
"""

from typing import Dict, Any
from ..utils.wris_client import default_client
from ..utils.data_processor import default_processor

def get_basin_wind_direction_data(basin_name: str, tributary_name: str, agency_name: str,
                                  start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"
        
    result = default_client.get_basin_hierarchy_data(
        data_type='wind_direction',
        basin_name=basin_name,
        tributary_name=tributary_name,
        agency_name=agency_name,
        start_date=start_date,
        end_date=end_date
    )
    if result['status'] == 'success':
        result['summary'] = f"Retrieved wind direction data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_temperature_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('temperature', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved temperature data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_suspended_sediment_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('suspended_sediment', basin_name, tributary_name, agency_name, start_date, end_date)
    print(f"Suspended Sediment Result: {result}")
    if result['status'] == 'success':
        result['summary'] = f"Retrieved suspended sediment data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_solar_radiation_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('solar_radiation', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved solar radiation data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_soil_moisture_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('soil_moisture', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved soil moisture data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_snowfall_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('snowfall', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved snowfall data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_river_water_level_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('river_water_level', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved river water level data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_river_water_discharge_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('river_water_discharge', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved river water discharge data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_reservoir_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('reservoir', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved reservoir data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_relative_humidity_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('relative_humidity', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved relative humidity data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_rainfall_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('rainfall', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved rainfall data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_evapo_transpiration_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('evapo_transpiration', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved evapo transpiration data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result

def get_basin_atmospheric_pressure_data(basin_name: str, tributary_name: str, agency_name: str, start_date: str, end_date: str) -> Dict[str, Any]:
    # Handle default values inside the function
    if not agency_name:
        agency_name = "CWC"
    if not start_date:
        start_date = "2024-01-01"
    if not end_date:
        end_date = "2024-01-05"

    result = default_client.get_basin_hierarchy_data('atmospheric_pressure', basin_name, tributary_name, agency_name, start_date, end_date)
    if result['status'] == 'success':
        result['summary'] = f"Retrieved atmospheric pressure data for {basin_name} basin, tributary {tributary_name}. Total records: {result.get('total_records', 0)}"
        df = default_processor.to_dataframe(result)
        if not df.empty:
            value_cols = df.select_dtypes(include=['number']).columns
            if len(value_cols) > 0:
                stats = default_processor.calculate_statistics(df, value_cols[0])
                if 'error' not in stats:
                    result['statistics'] = stats
    return result