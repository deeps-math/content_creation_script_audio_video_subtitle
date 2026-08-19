from tools.generator import ask_llama
from tools.prompts import (
    script_prompt,
    title_prompt,
    hashtag_prompt
)


# -----------------------------------
# MAIN SCRIPT AGENT
# -----------------------------------

def run_script_agent(topic):

    script = ask_llama(
        script_prompt(topic)
    )

    title = ask_llama(
        title_prompt(topic)
    )

    hashtags = ask_llama(
        hashtag_prompt(topic)
    )

    with open(
        "memory/script.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(script)

    with open(
        "memory/title.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(title)

    with open(
        "memory/hashtags.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(hashtags)

    print("✅ Script + Title + Hashtags saved")

    return {
        "title": title,
        "script": script,
        "hashtags": hashtags
    }


# -----------------------------------
# TEST
# -----------------------------------

if __name__ == "__main__":

    topic = "first love in classroom"

    result = run_script_agent(topic)

    print("\n🎬 TITLE:\n")
    print(result["title"])

    print("\n📝 SCRIPT:\n")
    print(result["script"])

    print("\n🔥 HASHTAGS:\n")
    print(result["hashtags"])