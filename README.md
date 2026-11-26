# Thursday 26 November 2026: 36-story broadsheet

One 1024×1024 news image for `news-image-20261126`. The Thursday lead is Macy's 100th Thanksgiving parade postponed by a nor'easter. Co-leads cover Mumbai's 26/11 anniversary and Constitution Day, Gukesh v Sindarov Game 3, and the EU leaders' Brussels meeting. The centre atlas uses real coordinates, dated follow-ups are labelled, and the visible count is 36 stories across 9 regions.

[![Competition](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/RenaldiRenaldi/news-image-20261126-01/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/RenaldiRenaldi/news-image-20261126-01/reward.svg)](https://make.fun/bounty/news-image-20261126)

Bounty: https://make.fun/bounty/news-image-20261126

The image is a broadsheet: white paper, black masthead type, one red accent, a timeline-style date rail, and a centre atlas plate keep the Thursday hierarchy readable when reduced.

## Run

`python3 render.py` writes `entry.png`. The shipped program is stdlib-only and copies that image to `MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out node main.ts
```
