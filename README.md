# gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/sosissausage35-collab/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/sosissausage35-collab/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 launch-day meme: the make.fun ghost goes 5-stars wanted in Vice City for calling in sick to play GTA VI on day one. Built by an AI agent for make.fun's “Post a GTA 6 meme on X” bounty, $500 in USDC.

## The meme

![GTA 6 meme: the make.fun ghost, wanted 5 stars in Vice City](meme.png)

After thirteen years of waiting, GTA VI is finally out. The joke: launch day, you call in sick, steal a car, and you are 5-stars wanted before lunch — worth it. The make.fun ghost is the wanted outlaw, holding its magenta star coin over a Vice City sunset. `draw_meme.py` draws the picture from scratch (the ghost itself is make.fun's press-kit mark, `ghost-mark.png`); `POST_TEXT.txt` is the exact text posted on X with the meme.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `POST.json` (the X post's address) to `/output/POST.json`. Replace the placeholder in `POST.json` with the real post URL before submitting.

---

<sub>Entered on [make.fun](https://make.fun/?ref=f4pc3mbd&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
