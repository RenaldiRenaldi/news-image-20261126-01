# Blackout Atlas: Thursday 26 November 2026

One 1024×1024 news image for `news-image-20261126`. The lead is the preliminary Reuters/AP/CNN toll from the Giza Al-Warraq tanker fire: 31 killed and 21 injured. The co-leads are the Nasdaq's 4% intraday plunge, Shenzhou-24 carrying the first Pakistani astronaut to Tiangong, and the Jerusalem judges' recommendation on Netanyahu's corruption cases. The atlas uses the supplied real coordinates, and dated follow-ups stay inside their original threads.

[![Competition](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/RenaldiRenaldi/news-image-20261126-01/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/RenaldiRenaldi/news-image-20261126-01/reward.svg)](https://make.fun/bounty/news-image-20261126)

Bounty: https://make.fun/bounty/news-image-20261126

The image is intentionally a blackout atlas: a dark ocean plate, pale land, gold location dots, and a four-number ticker keep the lead and co-leads readable when reduced.

## Run

`python3 render.py` writes `entry.png`. The shipped program is stdlib-only and copies that image to `MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out node main.ts
```
