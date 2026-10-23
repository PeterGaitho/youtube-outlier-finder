"""Find breakout videos for two channels and print them.

pip install apify-client
set APIFY_TOKEN=your_token   (Windows)   or   export APIFY_TOKEN=your_token
python python_example.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("pietro_wagaitho/youtube-outlier-finder").call(
    run_input={
        "channels": ["@HowMoneyWorks", "@PolyMatter"],
        "minOutlierScore": 3,
        "maxOutliersPerChannel": 5,
    },
    max_total_charge_usd=1.0,  # hard spending cap for this run
)

for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f'{row["outlierScore"]:>6}x  {row["views"]:>10,} views  {row["channelName"]}: {row["title"]}')
