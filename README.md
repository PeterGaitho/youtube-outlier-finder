# YouTube Outlier Finder: examples

Find the YouTube videos that **broke out**: the ones that got many times more views than their channel normally gets. Useful for video idea research, competitor analysis, and spotting topics that travel beyond a creator's own audience.

This repo holds ready-to-run examples for the [YouTube Outlier Finder](https://apify.com/pietro_wagaitho/youtube-outlier-finder) Actor on Apify. No YouTube API key, no login, pay only per channel analysed.

## The score

```
outlierScore = video views / median views of the ~10 uploads published around it
```

A score of **7.5** means the video got 7.5 times what that channel was normally getting at the time. Comparing against neighbouring uploads, instead of the channel's all-time average, means fast-growing channels are not misread, and brand-new videos are left out until their views settle.

## Real output

Topic search: `why rent is so high`

| Score | Views | Channel norm | Channel | Title |
|---|---|---|---|---|
| 7.52 | 199,232 | 26,500 | Foundation for Economic Education | The Real Reason Your Rent Is So High |
| 4.45 | 855,226 | 192,000 | 60 Minutes | Why rents are dramatically increasing across the United States |

Full rows: [`sample-output.json`](sample-output.json).

## Run it

| Example | File |
|---|---|
| Python | [`examples/python_example.py`](examples/python_example.py) |
| Node.js | [`examples/node_example.mjs`](examples/node_example.mjs) |
| From Claude, Cursor or any MCP client | [`examples/mcp.md`](examples/mcp.md) |
| Plain HTTP (curl) | [`examples/curl.md`](examples/curl.md) |

Each needs an Apify API token (free account: https://console.apify.com/sign-up, then Settings, API & Integrations).

## Input, in short

| Field | Example | Meaning |
|---|---|---|
| `channels` | `["@HowMoneyWorks"]` | @handles, UC... IDs or channel URLs |
| `searchQueries` | `["why rent is so high"]` | score every search result against its own channel |
| `minOutlierScore` | `2` | keep videos at or above this multiple |
| `includeShorts` | `true` | Shorts are only compared with Shorts |

Full input and pricing: https://apify.com/pietro_wagaitho/youtube-outlier-finder

## License

Examples are MIT licensed.
