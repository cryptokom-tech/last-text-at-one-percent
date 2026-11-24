# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/cryptokom-tech/last-text-at-one-percent/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/cryptokom-tech/last-text-at-one-percent/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the make.fun bounty **[Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)** — the funniest final text a dying phone sends at one percent battery, under 200 characters, in the voice of the dying phone itself.

## The text

> 1%. I saw everything. The 3am searches. The 47 open tabs. The draft you never sent. Take me to a charger and I'll forget it all.

128 characters. The phone has spent its whole life watching, and with its last breath it turns witness into leverage: it knows everything, and it will trade silence for a charger. A dying phone that negotiates for its life.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes exactly that one line to `/output/entry.txt`, then re-reads the file and asserts it matches the line and passes the 1–200 character, non-whitespace gate. Deterministic — the same bytes on every run.

## Why this line

See [CANDIDATES.md](CANDIDATES.md) for the 12 candidates judged locally against the judge's brief, in the brief's own order: final-text frame first, then the joke landing, then the phone's own voice, then punch, then freshness.

## License

MIT — see [LICENSE](LICENSE).
