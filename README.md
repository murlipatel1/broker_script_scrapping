# Broker Script Master Mapping Project

## Project Overview

The purpose of this project is to achieve a singular mapping of script masters from multiple brokers. The project allows users to select a script from one broker and retrieve corresponding mappings from other brokers. This integration is crucial for traders who need to make informed decisions based on data from different sources.

## Data Sources

The project utilizes four CSV files containing data from different brokers, each with different structures and column names. The columns contain various attributes related to trading instruments. Below are the details of each CSV file:

1. **CSV1**: 
    - **Columns**: `token`, `symbol`, `name`, `expiry`, `strike`, `lotsize`, `instrumenttype`, `exch_seg`, `tick_size`
    - **Description**: Contains basic information about instruments from Broker 1.

2. **CSV2**:
    - **Columns**: `id`, `instrument_name`, `segment`, `lot_size`, `tick_size`, `expiry`, `trading_sessions`, `date`, `unknown_field_1`, `symbol_exchange`, `price_step`, `decimal_places`, `instrument_type`, `symbol`, `market_status`, `unidentified_field`, `exchange_code`, `product_code`, `expiry_date`, `open_interest`, `strike_price`
    - **Description**: Contains trading instrument details from Broker 2.

3. **CSV3**:
    - **Columns**: `id`, `company_name`, `volume`, `price`, `change`, `isin`, `trading_sessions`, `date`, `unknown_field_1`, `symbol_exchange`, `lot_size`, `face_value`, `tick_size`, `symbol`, `market_status`, `unidentified_field`, `exchange_code`, `product_code`, `expiry_date`, `open_interest`, `strike_price`
    - **Description**: Contains trading information from Broker 3.

4. **CSV4**:
    - **Columns**: `instrumentToken`, `instrumentName`, `name`, `lastPrice`, `expiry`, `strike`, `tickSize`, `lotSize`, `instrumentType`, `segment`, `exchange`, `isin`, `multiplier`, `exchangeToken`, `OptionType`
    - **Description**: Contains trading details from Broker 4.

## How to Run the Project
Save the above code in a Python file, for example, broker_script_master.py.

Ensure that the CSV files (csv1.csv, csv2.csv, csv3.csv, csv4.csv) are in the same directory as the script.

Run the script using Python:
```bash
python app.py
```

The script will read the CSV files, perform the merging, and generate visualizations showing the distribution of lot sizes and the count of instruments by exchange.
