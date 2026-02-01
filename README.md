# The Obituary Machine

A dark engine that writes memorials for those who never lived.

Each day, the machine conjures a name, a span of dates, and a life that flickers into being only long enough to be mourned. These are obituaries for ghosts: the forgotten, the impossible, the almost-real. They leave behind achievements no history recorded, regrets no diary kept, and the quiet ache of a life that never was.

The results are committed as markdown files in `OBITUARIES/`, one per day.

## What it does

- Generates a fictional person: name, birth/death dates, life story, achievements, regrets
- Writes the obituary to `OBITUARIES/YYYY-MM-DD.md`
- Runs daily via GitHub Actions using the Anthropic API

## How it works

The script calls Anthropic's API and asks for a single, self-contained obituary in markdown. It is designed to feel somber, contemplative, and existential — a memorial for the absent.

## Running locally

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key
export ANTHROPIC_BASE_URL=https://api.anthropic.com
python obituary.py
```

## Anti-License

[ANTI-LICENSE](LICENSE) — This is not a license. This is an invitation.

Take it. Use it. Break it. Fix it. Sell it. Give it away.

If you need permission, you're thinking too much.

---

**Strange people. Strange things.**

📧 hi@sdpkjc.com
