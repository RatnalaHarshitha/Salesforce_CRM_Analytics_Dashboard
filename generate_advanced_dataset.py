import csv
import random
from datetime import datetime, timedelta

def generate_data(n=100):
    sources = ['Website', 'Referral', 'Ads', 'Cold Call']
    stages = ['Prospecting', 'Negotiation', 'Closed Won', 'Closed Lost']

    data = []
    for i in range(n):
        source = random.choice(sources)
        status = random.choice(['New', 'Qualified', 'Contacted'])

        stage = random.choice(stages) if status == 'Qualified' else 'N/A'
        amount = random.randint(1000, 50000) if stage != 'N/A' else ''

        date = datetime.now() - timedelta(days=random.randint(1, 300))

        data.append({
            'Lead_ID': i,
            'Lead_Source': source,
            'Lead_Status': status,
            'Opportunity_Stage': stage,
            'Amount': amount,
            'Created_Date': date.strftime('%Y-%m-%d')
        })

    with open('crm_data_raw.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

generate_data()
