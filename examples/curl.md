# Plain HTTP

One request runs the Actor and returns the rows when it finishes (good for jobs under about 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/pietro_wagaitho~youtube-outlier-finder/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"channels": ["@EconomicsExplained"], "minOutlierScore": 3}'
```

Works from n8n, Make, Zapier or any tool that can send an HTTP request.
