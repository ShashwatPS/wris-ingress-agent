# ingress_agent/utils/data_processor.py

import pandas as pd

class WRISDataProcessor:
    def to_dataframe(self, api_response):
        # Expecting api_response['data'] with 'content' list
        if 'data' in api_response and 'content' in api_response['data']:
            df = pd.DataFrame(api_response['data']['content'])
        else:
            df = pd.DataFrame()
        return df

    def calculate_statistics(self, df, value_col):
        result = {}
        if value_col in df.columns and not df.empty:
            col = df[value_col]
            # Only analyze numeric columns
            if pd.api.types.is_numeric_dtype(col):
                result['mean'] = float(col.mean())
                result['min'] = float(col.min())
                result['max'] = float(col.max())
                result['std'] = float(col.std())
                result['count'] = int(col.count())
            else:
                result['error'] = f'Column {value_col} is not numeric'
        else:
            result['error'] = f'Column {value_col} not found'
        return result

default_processor = WRISDataProcessor()
