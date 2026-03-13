import os
import datetime
import random
import glob

topics = [
("The Rise of the Eurodollar Market","https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif"),
("How SWIFT Became the Backbone of Global Banking","https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"),
("Why Delaware Became America's Corporate Capital","https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif"),
("Singapore's Rise as a Global Financial Hub","https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif"),
("Luxembourg and the Global Fund Industry","https://media.giphy.com/media/l0HlHFRbmaZtBRhXG/giphy.gif"),
("The History of the Cayman Islands as a Tax Haven","https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"),
("The Evolution of Offshore Banking","https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif"),
("How Wall Street Became the Global Financial Center","https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif"),
("The Birth of the IMF and World Bank","https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"),
("The History of Hedge Funds","https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif")
]

def slugify(title):
    return title.lower().replace(" ", "-").replace("'", "")

def existing_topics():
    files = glob.glob("_posts/*.md")
    used = []
    for f in files:
        name = os.path.basename(f)
        topic = name.split("-",3)[-1].replace(".md","")
        used.append(topic)
    return used

def choose_topic():
    used = existing_topics()
    remaining = [t for t in topics if slugify(t[0]) not in used]
    if not remaining:
        remaining = topics
    return random.choice(remaining)

def internal_links():

    files = glob.glob("_posts/*.md")
    if len(files) < 3:
        return ""

    sample = random.sample(files, min(3,len(files)))

    links = []

    for f in sample:
        name = os.path.basename(f)
        slug = name.replace(".md","")
        title = slug.split("-",3)[-1].replace("-"," ").title()
        url = "/" + slug + ".html"
        links.append(f"- [{title}]({url})")

    return "\n".join(links)

def generate_article(topic):

    intro = f"""
Global finance did not emerge suddenly. The evolution of **{topic}** reflects the deeper institutional forces that shape international capital markets. Economists studying financial history often point to regulatory arbitrage, geopolitical shifts, and technological change as the three main drivers behind the emergence of new financial structures.

Understanding this history helps explain why modern financial markets operate the way they do today.
"""

    background = f"""
The origins of **{topic}** lie in the structural transformation of the global financial system during the twentieth century. As international trade expanded and multinational corporations became more influential, financial institutions needed mechanisms to move capital across borders efficiently.

These pressures created incentives for financial innovation. Banks began experimenting with new instruments, jurisdictions competed to attract capital, and regulatory frameworks adapted unevenly across countries.
"""

    development = f"""
Over time, **{topic}** developed into an important component of global finance. Institutional investors, multinational corporations, and governments all became participants in these evolving markets.

Three forces drove this process:

1. **Regulatory differences between jurisdictions**
2. **Technological improvements in financial infrastructure**
3. **The growing integration of global capital markets**

These forces combined to create new financial ecosystems that operated alongside traditional domestic banking systems.
"""

    impact = f"""
The long-term impact of **{topic}** has been profound. It influenced how capital flows internationally, how banks structure their balance sheets, and how regulators attempt to manage systemic risk.

Financial centers that successfully adapted to these developments often became dominant hubs of international finance. Meanwhile, policymakers faced the difficult challenge of balancing financial innovation with financial stability.
"""

    conclusion = f"""
The story of **{topic}** demonstrates how financial systems evolve through the interaction of markets, institutions, and regulation. By examining these historical transformations, economists gain valuable insight into the strengths and vulnerabilities of modern global finance.

As financial markets continue to evolve, the lessons from this history remain highly relevant.
"""

    body = intro + background + development + impact + conclusion

    return body * 2   # doubles length (~1200 words)

def main():

    today = datetime.date.today()

    topic, gif = choose_topic()

    slug = slugify(topic)

    filename = f"_posts/{today}-{slug}.md"

    article = generate_article(topic)

    links = internal_links()

    content = f"""---
layout: post
title: "{topic}"
date: {today}
categories: finance-history
tags: global-finance financial-history banking
---

![finance gif]({gif})

{article}

## Related Topics

{links}

"""

    os.makedirs("_posts", exist_ok=True)

    with open(filename,"w") as f:
        f.write(content)

    print("Generated:",filename)

if __name__ == "__main__":
    main()
