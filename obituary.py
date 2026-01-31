import os
from datetime import datetime
import anthropic

MODEL = "claude-sonnet-4-20250514"


def build_prompt() -> str:
    return (
        "Write a single obituary for a completely fictional person who never existed. "
        "The tone is dark, contemplative, and existential. This is a memorial for a ghost. "
        "Include: full name, birth and death dates, a short life story, 2-3 achievements, "
        "and 1-2 regrets. Output in markdown with a title and short sections. "
        "Do not include explanations or meta commentary."
    )


def generate_obituary() -> str:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL"))
    message = client.messages.create(
        model=MODEL,
        max_tokens=800,
        messages=[{"role": "user", "content": build_prompt()}],
    )
    return message.content[0].text.strip()


def write_obituary(markdown: str) -> str:
    date_str = datetime.utcnow().strftime("%Y-%m-%d-%H%M")
    out_dir = os.path.join(os.path.dirname(__file__), "OBITUARIES")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{date_str}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown)
        f.write("\n")
    return out_path


def main() -> None:
    markdown = generate_obituary()
    out_path = write_obituary(markdown)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
