import re

def extract_dates(text):
    date_pattern = r'\b(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})|([A-Za-z]{3} \d{1,2}, \d{4})\b'
    
    dates = re.findall(date_pattern, text)
    
    extracted_dates = [date for date_tuple in dates for date in date_tuple if date]
    
    return extracted_dates

d ='''The event is scheduled for 12/09/2023. Another event will be held on 2023-09-12.
Please note that the previous event took place on Sep 12, 2023.
'''

dates = extract_dates(d)
print("Extracted dates:", dates)
