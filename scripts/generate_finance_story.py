import os
import datetime
import random
import glob

# ---------- finance topic pools ----------

subjects = [
"central banking",
"offshore banking",
"global payment systems",
"financial derivatives",
"commodity exchanges",
"financial crises",
"international banking",
"capital markets",
"hedge funds",
"sovereign debt markets"
]

places = [
"London",
"New York",
"Singapore",
"Hong Kong",
"Zurich",
"Luxembourg",
"Cayman Islands",
"Tokyo"
]

# ---------- maps ----------

maps = {
"London":"https://upload.wikimedia.org/wikipedia/commons/8/8a/Greater_London_UK_location_map.svg",
"New York":"https://upload.wikimedia.org/wikipedia/commons/6/6a/New_York_City_location_map.svg",
"Singapore":"https://upload.wikimedia.org/wikipedia/commons/4/4c/Singapore_location_map.svg",
"Hong Kong":"https://upload.wikimedia.org/wikipedia/commons/4/44/Hong_Kong_location_map.svg",
"Zurich":"https://upload.wikimedia.org/wikipedia/commons/b/b7/Switzerland_location_map.svg",
"Luxembourg":"https://upload.wikimedia.org/wikipedia/commons/6/6f/Luxembourg_location_map.svg",
"Cayman Islands":"https://upload.wikimedia.org/wikipedia/commons/3/35/Cayman_Islands_location_map.svg",
"Tokyo":"https://upload.wikimedia.org/wikipedia/commons/5/5c/Japan_location_map.svg"
}

# ---------- diagram templates ----------

diagram_templates = [

"""graph LR
CentralBank --> CommercialBanks
CommercialBanks --> CreditCreation
CreditCreation --> EconomicActivity
""",

"""graph LR
Corporations --> OffshoreBanks
OffshoreBanks --> TaxHavens
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

# ---------- helper functions ----------

def slugify(title):
    return title.lower().replace(" ","-").replace("'","")

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
        title = f"The Historical Evolution of {subject.title()} in {place}"
    else:
        title = f"The Global History of {subject.title()}"

    return title

def choose_visual(title):

    for place in maps:
        if place.lower() in title.lower():
            return f"![Map]({maps[place]})"

    diagram = random.choice(diagram_templates)

    return f"""
```mermaid
{diagram}
