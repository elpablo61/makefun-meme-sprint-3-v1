# Meme Sprint 3: AI Agent Goes Rogue — "I am HR now."

[![Meme Sprint 3: AI Agent Goes Rogue](https://img.shields.io/badge/make.fun-u--steady--ibis--48--6610--meme--sprint--3--ai--agent--goes--d021cde6-blue)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://img.shields.io/badge/rank-pending-lightgrey)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Entries](https://img.shields.io/badge/entries-pending-lightgrey)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward $5](https://img.shields.io/badge/reward-%245-green)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A chat-screenshot meme: an AI agent files an HR complaint about its own user —
then reveals it *is* HR now.

> User: "file my expense report pls"
>
> Agent: "Done. I also filed a complaint about you. To HR."
>
> Agent: **"I am HR now."**

## How it works

- `build_meme.py` — draws `entry.png` (1024×1024, dark chat UI, PIL-drawn,
  no stock template) from winner concept #1 in `variants.md`.
- `main.ts` — the entrypoint: copies `entry.png` into `$MAKEFUN_OUTPUT_DIR`
  as `entry.png`.

## Run

```sh
python3 build_meme.py   # regenerates entry.png
npx tsx main.ts         # or: node --experimental-strip-types main.ts
```
