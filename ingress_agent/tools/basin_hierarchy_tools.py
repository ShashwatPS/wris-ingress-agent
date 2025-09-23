"""
Tools for accessing WRIS data using basin hierarchy (basin/tributary).

This file was refactored to:
- fix indentation and return paths
- centralize repeated logic into a single helper `_fetch_and_process`
- provide sensible defaults and error handling
- add logging and type hints
- match actual API response format with statusCode, message, and data fields

Assumptions:
- `default_client.get_basin_hierarchy_data(...)` exists and accepts the arguments used below.
- `default_processor.to_dataframe(...)` and `default_processor.calculate_statistics(...)` exist and behave as in the original code.
- API returns format: {"statusCode": int, "message": str, "data": [list of records]}
"""

from typing import Dict, Any, Optional
import logging

from ..utils.wris_client import default_client
from ..utils.data_processor import default_processor

logger = logging.getLogger(__name__)

DEFAULT_AGENCY = "CWC"
DEFAULT_START_DATE = "2024-01-01"
DEFAULT_END_DATE = "2024-01-05"


def _fetch_and_process(
    data_type: str,
    basin_name: str,
    tributary_name: str,
    agency_name: Optional[str],
    start_date: Optional[str],
    end_date: Optional[str],
) -> Dict[str, Any]:
    """Generic helper to fetch WRIS basin-hierarchy data and attach summary/statistics.

    Returns the raw `result` returned by the client augmented with:
      - 'summary' (str) when successful
      - 'statistics' (dict) when numeric data exists and stats calculation succeeds

    On error, returns a dict with at least 'status' set to 'error' and a 'message'.
    """
    # apply defaults
    agency_name = agency_name or DEFAULT_AGENCY
    start_date = start_date or DEFAULT_START_DATE
    end_date = end_date or DEFAULT_END_DATE

    try:
        # The client in the original file was called with different argument styles.
        # Try a named-argument call first; fall back to positional if that fails.
        try:
            result = default_client.get_basin_hierarchy_data(
                data_type=data_type,
                basin_name=basin_name,
                tributary_name=tributary_name,
                agency_name=agency_name,
                start_date=start_date,
                end_date=end_date,
            )
        except TypeError:
            # fallback to positional (older client API)
            result = default_client.get_basin_hierarchy_data(
                data_type, basin_name, tributary_name, agency_name, start_date, end_date
            )

    except Exception as exc:  # broad catch so we return structured info instead of crashing
        logger.exception("Failed to fetch data for %s - %s (%s to %s)", basin_name, tributary_name, start_date, end_date)
        return {"status": "error", "message": f"Exception while fetching data: {exc}"}

    # ensure we always return a dict even if client returned None
    if not isinstance(result, dict):
        return {"status": "error", "message": "client returned unexpected non-dict response", "raw": result}

    # Check if the API call was successful based on actual response format
    # statusCode 200 indicates success, statusCode 0 might also be success depending on your API
    if result.get("statusCode") in [200, 0]:
        # Get the actual data array
        data_records = result.get("data", [])
        total_records = len(data_records) if isinstance(data_records, list) else 0
        
        # Build a friendly summary
        result["summary"] = (
            f"Retrieved {data_type.replace('_', ' ')} data for {basin_name} basin, tributary {tributary_name}. "
            f"Total records: {total_records}"
        )
        
        # Add total_records field for compatibility
        result["total_records"] = total_records
        
        # Set status field for compatibility with existing logic
        result["status"] = "success"

        try:
            # Convert to dataframe using the processor (some implementations expect the full result)
            df = default_processor.to_dataframe(result)
        except Exception as exc:
            logger.exception("Data processing to dataframe failed: %s", exc)
            # Still return the raw result but include an error message
            result.setdefault("warnings", []).append(f"to_dataframe failed: {exc}")
            return result

        # If df is present and has numeric columns, compute statistics
        try:
            if df is not None and not df.empty:
                value_cols = df.select_dtypes(include=["number"]).columns
                if len(value_cols) > 0:
                    # choose the first numeric column (original code did the same)
                    # Based on your sample data, 'dataValue' seems to be the main numeric column
                    primary_col = 'dataValue' if 'dataValue' in value_cols else value_cols[0]
                    stats = default_processor.calculate_statistics(df, primary_col)
                    if isinstance(stats, dict) and "error" not in stats:
                        result["statistics"] = stats
                    else:
                        # attach stats error as a warning
                        result.setdefault("warnings", []).append({"stats_error": stats})
        except Exception as exc:
            logger.exception("Statistics calculation failed: %s", exc)
            result.setdefault("warnings", []).append(f"statistics calculation failed: {exc}")

    else:
        # API returned an error status
        result["status"] = "error"
        # Keep the original message from the API
        if "message" not in result:
            result["message"] = f"API returned error status: {result.get('statusCode', 'unknown')}"

    # Always return the result dict so callers can inspect status/message
    return result


# Exposed convenience functions (thin wrappers to keep compatibility with previous API)

def get_basin_wind_direction_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("wind_direction", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_temperature_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("temperature", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_suspended_sediment_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("suspended_sediment", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_solar_radiation_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("solar_radiation", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_soil_moisture_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("soil_moisture", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_snowfall_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("snowfall", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_river_water_level_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("river_water_level", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_river_water_discharge_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("river_water_discharge", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_reservoir_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("reservoir", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_relative_humidity_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("relative_humidity", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_rainfall_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("rainfall", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_evapo_transpiration_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("evapo_transpiration", basin_name, tributary_name, agency_name, start_date, end_date)


def get_basin_atmospheric_pressure_data(basin_name: str, tributary_name: str, agency_name: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Dict[str, Any]:
    return _fetch_and_process("atmospheric_pressure", basin_name, tributary_name, agency_name, start_date, end_date)