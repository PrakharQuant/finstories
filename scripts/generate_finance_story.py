
import os
import datetime
import random
import glob


diagram_templates = [

"""graph LR
CentralBank --> CommercialBanks
CommercialBanks --> CreditCreation
CreditCreation --> EconomicGrowth
""",

"""graph LR
Corporations --> OffshoreBanking
OffshoreBanking --> TaxHavens
TaxHavens --> GlobalInvestment
""",

"""graph LR
Investors --> HedgeFunds
HedgeFunds --> Leverage
Leverage --> MarketImpact
""",

"""graph LR
GlobalTrade --> CurrencyMarkets
CurrencyMarkets --> ExchangeRates
ExchangeRates --> CapitalFlows
"""
]


def generate_diagram():
    return random.choice(diagram_templates)


maps = {
"London":"https://upload.wikimedia.org/wikipedia/commons/8/8a/Greater_London_UK_location_map.svg",
"New York":"https://upload.wikimedia.org/wikipedia/commons/6/6a/New_York_City_location_map.svg",
"Singapore":"https://upload.wikimedia.org/wikipedia/commons/4/4c/Singapore_location_map.svg",
"Hong Kong":"https://upload.wikimedia.org/wikipedia/commons/4/44/Hong_Kong_location_map.svg",
"Zurich":"https://upload.wikimedia.org/wikipedia/commons/b/b7/Switzerland_location_map.svg",
"Luxembourg":"https://upload.wikimedia.org/wikipedia/commons/6/6f/Luxembourg_location_map.svg",
"Cayman Islands":"https://upload.wikimedia.org/wikipedia/commons/3/35/Cayman_Islands_location_map.svg",
"Tokyo":"https://upload.wikimedia.org/wikipedia/commons/5/5c/Japan_location_map.svg",
"Delaware":"https://upload.wikimedia.org/wikipedia/commons/4/4b/Delaware_in_United_States.svg",
"Dublin":"https://upload.wikimedia.org/wikipedia/commons/5/5e/Ireland_location_map.svg"
}


gifs = [
"https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif",
"https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif",
"https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
"https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif"
]


finance_subjects = [
"central banking",
"sovereign debt markets",
"global payment systems",
"financial derivatives",
"commodity exchanges",
"financial crises",
"offshore banking",
"international banking",
"capital markets",
"hedge funds",
"private equity",
"stock exchanges",
"bond markets",
"currency markets",
"global financial regulation",
"banking supervision",
"financial innovation",
"shadow banking"
]


finance_places = [
"London",
"New York",
"Singapore",
"Hong Kong",
"Zurich",
"Luxembourg",
"Delaware",
"Cayman Islands",
"Dublin",
"Tokyo"
]


def post_exists_today():

    today = str(datetime.date.today())
    files = glob.glob("_posts/*.md")

    for f in files:
        if today in f:
            return True

    return False


def topic_exists(slug):

    files = glob.glob("_posts/*.md")

    for f in files:
        if slug in f:
            return True

    return False


def generate_topic():

    subject = random.choice(finance_subjects)

    if random.random() < 0.5:
        place = random.choice(finance_places)
        title = f"The Historical Evolution of {subject.title()} in {place}"
    else:
        title = f"The Global History of {subject.title()}"

    gif = random.choice(gifs)

    return title, gif


def slugify(title):
    return title.lower().replace(" ", "-").replace("'", "")


def internal_links():

    files = glob.glob("_posts/*.md")

    if len(files) < 3:
        return ""

    sample = random.sample(files, min(3, len(files)))

    links = []

    for f in sample:

        name = os.path.basename(f)
        slug = name.replace(".md","")
        title = slug.split("-",3)[-1].replace("-"," ").title()

        url = "/" + slug

        links.append(f"- [{title}]({url})")

    return "\n".join(links)


def generate_article(topic):

    intro = f"""
> **Key Insight:**  
> {topic} emerged from the interaction between financial innovation, regulatory competition, and the globalization of capital markets.

**{topic}** did not emerge suddenly. Its development reflects deeper institutional forces that shape international capital markets. Economists studying financial history often point to regulatory arbitrage, geopolitical shifts, and technological change as the main drivers behind the emergence of new financial structures.
"""

    origins = """
## Origins of the System

The origins of this system lie in the structural transformation of the global financial system during the twentieth century. As international trade expanded and multinational corporations became more influential, financial institutions needed mechanisms to move capital across borders efficiently.

These pressures created incentives for financial innovation. Banks began experimenting with new instruments, jurisdictions competed to attract capital, and regulatory frameworks evolved unevenly across countries.
"""

    development = """
## Institutional Development

Over time the system developed into an important component of global finance. Institutional investors, multinational corporations, and governments all became participants in these evolving markets.

Three forces played a particularly important role:

1. Regulatory differences between jurisdictions  
2. Technological improvements in financial infrastructure  
3. The increasing integration of global capital markets
"""

    impact = """
## Global Impact

The long-term impact has been profound. It influenced how capital flows internationally, how banks structure their balance sheets, and how regulators attempt to manage systemic risk.

Financial centers that successfully adapted to these developments often became dominant hubs of international finance.
"""

    conclusion = """
## Why This History Matters

The evolution of financial systems demonstrates how markets, institutions, and regulation interact over time. By examining these historical transformations, economists gain valuable insight into the strengths and vulnerabilities of modern global finance.

As financial markets continue to evolve, the lessons from this history remain highly relevant.
"""

    body = intro + origins + development + impact + conclusion

    return body


def choose_visual(title):

    for place in maps:
        if place.lower() in title.lower():
            return maps[place]

    return None


def main():

    if post_exists_today():
        print("Post already exists for today")
        return


    today = datetime.date.today()


    # avoid duplicate topics
    while True:

        topic, gif = generate_topic()
        slug = slugify(topic)

        if not topic_exists(slug):
            break


    visual = choose_visual(topic)
    diagram = generate_diagram()

    filename = f"_posts/{today}-{slug}.md"

    article = generate_article(topic)

    links = internal_links()

    visual_line = f"![Map]({visual})" if visual else ""


    content = f"""---
layout: post
title: "{topic}"
date: {today}
categories: finance-history
tags: global-finance financial-history banking
---

```mermaid
{diagram}
````

{visual_line}

![Finance GIF]({gif})

{article}

## Related Posts

{links}
"""

```
os.makedirs("_posts", exist_ok=True)

with open(filename, "w") as f:
    f.write(content)

print(f"Generated: {filename}")
```

if **name** == "**main**":
main()

```
```

