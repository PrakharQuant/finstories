import os
import datetime
import random

topics = [
    "The Rise of the Eurodollar Market",
    "Why Delaware Became America's Corporate Capital",
    "The History of SWIFT and Global Payments",
    "How Cayman Became a Financial Hub",
    "Singapore's Rise as a Financial Center",
    "The Evolution of Luxembourg Fund Industry"
]

today = datetime.date.today()
topic = random.choice(topics)

slug = topic.lower().replace(" ", "-").replace("'", "")
filename = f"_posts/{today}-{slug}.md"

content = f"""---
layout: post
title: "{topic}"
date: {today}
categories: finance history
---

## Introduction

{topic} is one of the most important developments in global finance.

## Historical Background

Financial systems evolve through institutions, regulations, and market incentives.

## Why It Matters

Understanding these developments helps explain how modern global finance operates today.

## Conclusion

Financial history provides insight into the structure and evolution of modern markets.
"""

os.makedirs("_posts", exist_ok=True)

with open(filename, "w") as f:
    f.write(content)

print("Generated:", filename)
