ARIA Command Center v11 — Larger Reactor

Based on v10 Live Feeds. Increased circular ARIA insignia/triangle core from 45% to 57% of the center column width (~27% larger), retaining all remaining styles, live-feed support, and Silk keep-awake.

Open index.html in Chrome to preview. For Echo Show, deploy the entire directory to GitHub Pages as outlined in the v10 instructions.

ARIA COMMAND CENTER v10 — LIVE FEEDS READY

1. Open index.html in Chrome to preview. The Nashville/Bellevue weather panel requests real weather from Open-Meteo (Internet required).
2. For Fox News + Cowboys headlines, publish this folder as a GitHub Pages repository. Enable GitHub Actions workflow permissions to read/write repository contents (Settings > Actions > General > Workflow permissions).
3. Enable GitHub Pages from the main branch / root in Settings > Pages. The scheduled workflow .github/workflows/refresh-feeds.yml runs every 30 minutes (and manually via Actions > Refresh ARIA Headlines > Run workflow) and updates feed-data.json in the root.
4. When the feed-data.json has headlines, v10 will rotate them every 30 seconds. Tap a headline to open the source article. If a feed fails, it will show standby instead of invented news.
5. Weather and feeds are polled roughly every 15 minutes while the screen stays open. Static GitHub Pages caching and Safari/Silk differences may affect behavior; test in Echo Silk.
6. Keep silence-loop.wav alongside index.html. ACTIVATE ARIA starts the experimental quiet-audio keep-awake loop (not guaranteed).

Note: foxnews.com RSS terms permit personal noncommercial use and require direct article links. Do not reuse for a public/commercial news product without confirming permissions.

V12: increased bold panel text for 10.1-inch Echo Show; clock size optimized for its panel.
