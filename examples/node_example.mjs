// Find topic outliers: every search result scored against its own channel.
// npm install apify-client
// APIFY_TOKEN=your_token node node_example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('pietro_wagaitho/youtube-outlier-finder').call(
  { searchQueries: ['why rent is so high'], resultsPerQuery: 30 },
  { maxTotalChargeUsd: 1 },
);

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const r of items) {
  console.log(`${r.outlierScore}x  ${r.views.toLocaleString()} views  ${r.channelName}: ${r.title}`);
}
