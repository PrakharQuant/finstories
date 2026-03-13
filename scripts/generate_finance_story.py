import os
import datetime
import random
import glob

topics = [
    {
        "title": "The Rise of the Eurodollar Market",
        "gif": "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"
    },
    {
        "title": "Why Delaware Became America's Corporate Capital",
        "gif": "https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif"
    },
    {
        "title": "How SWIFT Became the Backbone of Global Banking",
        "gif": "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"
    },
    {
        "title": "The History of the Cayman Islands as a Tax Haven",
        "gif": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"
    },
    {
        "title": "Singapore's Rise as a Global Financial Hub",
        "gif": "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif"
    },
    {
        "title": "Luxembourg and the Global Fund Industry",
        "gif": "https://media.giphy.com/media/l0HlHFRbmaZtBRhXG/giphy.gif"
    }
]

def choose_topic():
    existing = glob.glob("_posts/*.md")

    used = []
    for f in existing:
        name = os.path.basename(f)
        used.append(name.split("-", 3)[-1].replace(".md","").replace("-", " "))

    remaining = [t for t in topics if t["title"].lower() not in used]

    if not remaining:
        remaining = topics

    return random.choice(remaining)

def generate_article(topic):

    intro = f"""
Global finance did not emerge overnight. The story of **{topic}** illustrates how
institutions, regulation, and economic incentives shape the architecture of
international markets.

Understanding this evolution is crucial for economists, policymakers,
and investors trying to interpret today's financial system.
"""

    history = f"""
The origins of **{topic}** lie in the structural transformation of global
capital markets during the twentieth century.

As trade expanded and multinational corporations grew, financial
intermediation had to evolve. Banks, regulatory frameworks, and offshore
financial centres developed mechanisms to accommodate cross-border capital.

These institutional innovations gradually created the foundations
of the modern global financial system.
"""

    mechanisms = f"""
Several mechanisms explain why **{topic}** became economically significant.

First, regulatory arbitrage allowed institutions to operate outside
certain domestic restrictions.

Second, technological progress in communications and settlement
systems enabled financial flows to move faster and across jurisdictions.

Third, governments often tolerated or even encouraged these developments
because they strengthened domestic financial sectors.
"""

    impact = f"""
Over time, **{topic}** reshaped the global financial landscape.

It influenced how banks structure balance sheets, how multinational
corporations manage liquidity, and how capital moves across borders.

Many of today's debates about financial regulation, monetary sovereignty,
and systemic risk can be traced back to these institutional changes.
"""

    conclusion = f"""
Financial history demonstrates that markets evolve through interaction
between private innovation and public regulation.

The development of **{topic}** highlights how seemingly technical
institutional shifts can produce profound consequences for the
structure of global capitalism.

Studying these developments helps economists better understand both
the stability and fragility of the modern financial system.
"""

    return intro + history + mechanisms + impact + conclusion

def main():

    today = datetime.date.today()

    topic = choose_topic()

    slug = topic["title"].lower().replace(" ", "-").replace("'", "")

    filename = f"_posts/{today}-{slug}.md"

    article = generate_article(topic["title"])

    content = f"""---
layout: post
title: "{topic['title']}"
date: {today}
categories: finance-history
tags: global-finance financial-history banking
---

![finance gif]({topic['gif']})

{article}
"""

    os.makedirs("_posts", exist_ok=True)

    with open(filename, "w") as f:
        f.write(content)

    print("Generated:", filename)

if __name__ == "__main__":
    main()
