import os
import datetime
import random
import glob

subjects = [
"central banking",
"offshore banking",
"global payment systems",
"financial crises",
"capital markets"
]

places = [
"London",
"New York",
"Singapore",
"Hong Kong",
"Luxembourg",
"Cayman Islands"
]

maps = {
"London":"https://upload.wikimedia.org/wikipedia/commons/8/8a/Greater_London_UK_location_map.svg",
"New York":"https://upload.wikimedia.org/wikipedia/commons/6/6a/New_York_City_location_map.svg",
"Singapore":"https://upload.wikimedia.org/wikipedia/commons/4/4c/Singapore_location_map.svg",
"Hong Kong":"https://upload.wikimedia.org/wikipedia/commons/4/44/Hong_Kong_location_map.svg",
"Luxembourg":"https://upload.wikimedia.org/wikipedia/commons/6/6f/Luxembourg_location_map.svg",
"Cayman Islands":"https://upload.wikimedia.org/wikipedia/commons/3/35/Cayman_Islands_location_map.svg"
}

diagram_templates = [
"graph LR\nCentralBank --> CommercialBanks\nCommercialBanks --> CreditCreation\nCreditCreation --> Economy",
"graph LR\nCorporations --> OffshoreBanks\nOffshoreBanks --> TaxHavens\nTaxHavens --> Investment"
]

def slugify(title):
    return title.lower().replace(" ","-")

def post_exists_today():
    today = str(datetime.date.today())
    files = glob.glob("_posts/*.md")
    for f in files:
        if today in f:
            return True
    return False

def generate_topic():
    subject = random.choice(subjects)
    if random.random() < 0.5:
        place = random.choice(places)
        return f"The History of {subject.title()} in {place}"
    else:
        return f"The Global History of {subject.title()}"

def choose_visual(title):

    for place in maps:
        if place.lower() in title.lower():
            return f"![Map]({maps[place]})"

    diagram = random.choice(diagram_templates)

    return f"""```mermaid
{diagram}
```"""

def generate_article(topic):

    text = f"""
The development of {topic} reflects broader structural changes in global finance.

Financial institutions evolve in response to regulatory frameworks,
technological innovation, and cross-border capital flows.

Understanding this historical process helps explain how modern
financial systems operate today.

The evolution of these institutions reshaped global financial
centers and influenced how capital moves across jurisdictions.
"""

    return text * 6

def main():

    if post_exists_today():
        print("Post already exists today")
        return

    today = datetime.date.today()

    topic = generate_topic()

    slug = slugify(topic)

    filename = f"_posts/{today}-{slug}.md"

    visual = choose_visual(topic)

    article = generate_article(topic)

    content = f"""---
layout: post
title: "{topic}"
date: {today}
---

{visual}

{article}
"""

    os.makedirs("_posts", exist_ok=True)

    with open(filename,"w") as f:
        f.write(content)

    print("Generated:", filename)

if __name__ == "__main__":
    main()
