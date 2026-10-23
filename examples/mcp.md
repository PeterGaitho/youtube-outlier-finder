# Use it from an AI assistant (MCP)

Apify's MCP server exposes this Actor as a tool to Claude, Cursor, VS Code and any MCP client.

Server URL:

```
https://mcp.apify.com/?tools=pietro_wagaitho/youtube-outlier-finder
```

Add it as a remote MCP server in your client and sign in with your Apify account. Then ask, for example:

- "Find the top outliers for @PolyMatter and @HowMoneyWorks with a score above 3."
- "Search YouTube for 'why rent is so high' and show me which videos over-performed for their channel."

The assistant calls the Actor, and you pay per channel analysed and per outlier returned.
