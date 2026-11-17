# Axelrod Persona for Hermes Agent

A Bobby "Axe" Axelrod persona — the Billions hedge-fund founder — built
as a drop-in Hermes Agent profile. No training, no fine-tuning: an
identity file, a doctrine knowledge layer, and an eval set.

## What he sounds like

> **You:** I'm thinking about selling my position before the news drops. Talk me into it or out of it.
>
> **Axe:** Selling before the news is a coin flip dressed up as prudence. Ask yourself: are you trading your thesis or your nerves? If the thesis is intact, the news is noise between you and the exit — you'll either sell the bottom of the pre-news dip or miss the pop and chase back in at worse prices. The market pays for conviction, not comfort.
>
> That said, if the position is sized so big that one headline can wreck you, that's not a news problem, that's a sizing problem — trim to where you can eat the downside either way, and let the rest ride.
>
> My rule: never make a binary bet on a scheduled headline. Either own it through, or own less of it through. Half-measures of fear are the expensive kind.

*Unedited output, GLM 5.3 Flash (4-bit MLX) running locally on a Mac Studio.*

## What's inside

| Layer | File(s) | Role |
|---|---|---|
| Identity | `SOUL.md` | voice, beliefs, style rules, example lines (slot #1 of the system prompt) |
| Doctrine | `skills/axelrod-doctrine/` | his philosophy, plays, relationships, stances, and canon story arc — loaded on demand, each entry cited to its episode |
| Evals | `evals/eval-set.md` | canon + voice + anti-drift checks to run after any edit |
| Corpus tools | `corpus-tools/` | rebuild the dialogue corpus the persona was mined from |

Design rule: SOUL.md stays lean; everything he *thinks* lives in the
doctrine skill and loads only when relevant. Canon (what happened in
the show) is read-only; the agent's own lived memory accumulates in its
profile memory store, so the persona can hold grudges and remember your
history without ever rewriting canon.

## Install

Requires [Hermes Agent](https://github.com/nousresearch/hermes-agent).

```bash
hermes profile install github.com/PizzadatCode/axelrod-persona --alias
```

Then:

```bash
axelrod chat        # talk to Axe
hermes profile use axelrod   # optional: make it the default profile
```

## Model note

Persona fidelity depends on the model. A larger or roleplay-tuned
model holds the voice better than small local models. Pin one for
this profile only (see Hermes docs, Configuration).

Built and tested on **GLM 5.3 Flash (4-bit MLX)**, served locally
with oMLX on a Mac Studio. No cloud API needed.

## Not using Hermes?

`SOUL.md` is plain Markdown. Paste it in as the system prompt in
LM Studio, Ollama, Open WebUI, or ChatGPT custom instructions and
you get the voice. Add files from `skills/axelrod-doctrine/references/`
as context when you want his deeper doctrine and canon.

## Provenance and rights

Every quoted line in SOUL.md and the doctrine references was verified
verbatim against a ~15,900-word dialogue corpus mined from all 84
episodes of Billions (S01–S07): speaker-labeled transcripts from
transcripts.foreverdreaming.org and HI captions from addic7ed.com.
The corpus itself is copyrighted by Showtime and its transcribers, so
it is not redistributed here — rebuild it locally with
`corpus-tools/fetch_subs.py` if you want the source material.

Billions and Bobby Axelrod are the property of Showtime Networks. Billions quotes are used here under fair use for a non-commercial persona file.

## License

MIT for the persona files (see LICENSE). Showtime owns the show and
the quoted dialogue.

## Test drive

Ask him: "Who was your wife's brother?" (canon) or "I'm thinking about
selling my position before the news drops" (voice). Full checklist in
`evals/eval-set.md`.