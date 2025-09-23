# utils/constants.py
"""
Constants and configuration values for WRIS API integration
"""

# Base URL for WRIS API
WRIS_BASE_URL = "https://indiawris.gov.in"

# Admin Hierarchy API Endpoints
ADMIN_ENDPOINTS = {
    'wind_direction': 'Dataset/Wind%20Direction',
    'temperature': 'Dataset/Temperature',
    'suspended_sediment': 'Dataset/Suspended%20Sediment',
    'solar_radiation': 'Dataset/Solar%20Radiation',
    'soil_moisture': 'Dataset/Soil%20Moisture',
    'snowfall': 'Dataset/SnowFall',
    'river_water_level': 'Dataset/River%20Water%20Level',
    'river_water_discharge': 'Dataset/River%20Water%20Discharge',
    'reservoir': 'Dataset/Reservoir',
    'relative_humidity': 'Dataset/Relative%20Humidity',
    'rainfall': 'Dataset/RainFall',
    'ground_water_level': 'Dataset/Ground%20Water%20Level',
    'evapo_transpiration': 'Dataset/Evapo%20Transpiration',
    'atmospheric_pressure': 'Dataset/Atmospheric%20Pressure'
}

# Basin Hierarchy API Endpoints
BASIN_ENDPOINTS = {
    'wind_direction': 'Dataset/Basin/Wind%20Direction',
    'temperature': 'Dataset/Basin/Temperature',
    'suspended_sediment': 'Dataset/Basin/Suspended%20Sediment',
    'solar_radiation': 'Dataset/Basin/Solar%20Radiation',
    'soil_moisture': 'Dataset/Basin/Soil%20Moisture',
    'snowfall': 'Dataset/Basin/SnowFall',
    'river_water_level': 'Dataset/Basin/River%20WaterLevel',
    'river_water_discharge': 'Dataset/Basin/River%20Water%20Discharge',
    'reservoir': 'Dataset/Basin/Reservoir',
    'relative_humidity': 'Dataset/Basin/Relative%20Humidity',
    'rainfall': 'Dataset/Basin/RainFall',
    'evapo_transpiration': 'Dataset/Basin/Evapo%20Transpiration',
    'atmospheric_pressure': 'Dataset/Basin/Atmospheric%20Pressure'
}

# Default API Parameters
DEFAULT_PARAMS = {
    'agency_name': 'CWC',
    'download': 'false',
    'page': 0,
    'size': 50
}

# HTTP Headers
DEFAULT_HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Groundwater Categories
GROUNDWATER_CATEGORIES = {
    'SAFE': 'Groundwater extraction is less than 70% of annual recharge',
    'SEMI_CRITICAL': 'Groundwater extraction is between 70-90% of annual recharge',
    'CRITICAL': 'Groundwater extraction is between 90-100% of annual recharge',
    'OVER_EXPLOITED': 'Groundwater extraction is more than 100% of annual recharge'
}

# Common Indian States and Districts for validation
STATES_DISTRICTS = {
    'Maharashtra': ['Pune', 'Mumbai', 'Nagpur', 'Aurangabad', 'Nashik', 'Solapur'],
    'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar', 'Gandhinagar'],
    'Rajasthan': ['Jaipur', 'Jodhpur', 'Kota', 'Bikaner', 'Ajmer', 'Udaipur'],
    'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Ghaziabad', 'Agra', 'Meerut', 'Varanasi'],
    'Madhya Pradesh': ['Bhopal', 'Indore', 'Jabalpur', 'Gwalior', 'Ujjain', 'Sagar'],
    'Karnataka': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore', 'Belgaum', 'Gulbarga'],
    'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem', 'Tirunelveli'],
    'Andhra Pradesh': ['Hyderabad', 'Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool'],
    'West Bengal': ['Kolkata', 'Howrah', 'Durgapur', 'Asansol', 'Siliguri', 'Malda'],
    'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Purnia', 'Darbhanga']
}

# Major River Basins in India
MAJOR_BASINS = [
    'Ganga',
    'Brahmaputra',
    'Indus',
    'Godavari', 
    'Krishna',
    'Cauvery',
    'Mahanadi',
    'Narmada',
    'Tapti',
    'Brahmani',
    'Sabarmati',
    'Mahi',
    'Pennar',
    'Subarnarekha',
    'West flowing rivers of Kutch and Saurashtra including Luni'
]

# Data Quality Indicators
DATA_QUALITY_THRESHOLDS = {
    'rainfall': {'min': 0, 'max': 10000},  # mm
    'temperature': {'min': -50, 'max': 60},  # Celsius
    'humidity': {'min': 0, 'max': 100},  # percentage
    'wind_speed': {'min': 0, 'max': 500},  # km/h
    'water_level': {'min': -100, 'max': 1000},  # meters
    'discharge': {'min': 0, 'max': 100000}  # cumecs
}

# Time-related constants
DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# API Response Status Codes
HTTP_STATUS = {
    'SUCCESS': 200,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'NOT_FOUND': 404,
    'SERVER_ERROR': 500
}