import pandas as pd
import matplotlib.pyplot as plt

def run_sales_analytics():
    print("Loading dataset...")
    df = pd.read_csv('crm_data_raw.csv')

    # Cleaning
    df['Lead_Source'] = df['Lead_Source'].fillna('Unknown')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
    df['Created_Date'] = pd.to_datetime(df['Created_Date'])

    print("\n--- SALES ANALYTICS REPORT ---")

    # Conversion Rate
    total_leads = len(df)
    qualified = len(df[df['Lead_Status'] == 'Qualified'])
    conversion = (qualified / total_leads) * 100
    print(f"Conversion Rate: {conversion:.2f}%")

    # Revenue by Stage
    revenue = df[df['Opportunity_Stage'] != 'N/A'].groupby('Opportunity_Stage')['Amount'].sum()
    print("\nRevenue by Stage:\n", revenue)

    # Win Rate
    won = df[df['Opportunity_Stage'] == 'Closed Won']
    win_rate = (won.groupby('Lead_Source').size() / df.groupby('Lead_Source').size() * 100).fillna(0)
    print("\nWin Rate:\n", win_rate)

    # Dashboard
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    revenue.plot(kind='barh', ax=axs[0,0], title="Revenue by Stage")
    win_rate.plot(kind='bar', ax=axs[0,1], title="Win Rate by Source")

    df['Lead_Status'].value_counts().plot(kind='pie', ax=axs[1,1], autopct='%1.1f%%')
    axs[1,1].set_title("Lead Status")

    plt.tight_layout()
    plt.savefig('Salesforce_CRM_Dashboard.png')
    print("Dashboard saved!")

if __name__ == "__main__":
    run_sales_analytics()
