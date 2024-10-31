import requests
import pandas as pd

# URL of the .txt file
url = "https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_Cash_01_04_2022.txt"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Decode the response content to get the text data
    text_data = response.text
    
    # Split the text data into lines
    lines = text_data.splitlines()
    
    # Create a list of dictionaries to store each row of data
    data = []
    
    # Assuming the first line contains headers
    headers = lines[0].split('|')
    
    # Process each line, starting from the second line (actual data)
    for line in lines[1:]:
        row = line.split('|')
        data.append(dict(zip(headers, row)))
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save DataFrame to CSV
    df.to_csv("TradeApiInstruments_Cash.csv", index=False)
    print("File downloaded and saved as TradeApiInstruments_Cash.csv")
else:
    print("Failed to download file. Status code:", response.status_code)
    