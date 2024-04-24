#!/usr/bin/env python3

"""Calculate a gender score based on survey input."""

import json, sys

def calc_max(weights: dict, invert: bool) -> dict:
    """Return the maximum score for each category."""
    maximums = dict()
    for category in weights.keys():
        maximums[category] = dict()
        for quality in weights[category].keys():
            if weights[category][quality] > 0:
                maximums[category][quality] = 5
            elif weights[category][quality] < 0:
                maximums[category][quality] = 1
            else:
                maximums[category][quality] = 3
            if invert:
                maximums[category][quality] = 6 - maximums[category][quality]
    return maximums

def calculate_score(weights: dict, values: dict) -> float:
    """Calculate the gender score of the given values."""
    meta = dict()
    for category in weights.keys():
        cat = dict()
        for quality in weights[category].keys():
            cat[quality] = weights[category][quality] * values[category][quality]
        meta[category] = cat
    count = sum(len(meta[category].keys()) for category in meta.keys())
    total = sum(sum(meta[category].values()) for category in meta.keys())
    return total / count

def main() -> None:
    """Calculate the gender score based on survey input."""
    filenames = sys.argv[1:]
    if len(filenames) < 1:
        print("Usage: calculate.py <filename(s)>")
        sys.exit(1)
    
    with open("weights.json", "r") as file:
        weights = json.load(file)

    max_masc_values = calc_max(weights, True)
    max_femme_values = calc_max(weights, False)

    response_values = {
        "max_masc": max_masc_values,
        "max_femme": max_femme_values,
    }
    for source_name in filenames:
        with open(source_name, "r") as file:
            response_values[source_name] = json.load(file)

    max_femme_score = calculate_score(weights, max_femme_values)
    max_masc_score = calculate_score(weights, max_masc_values)

    for source_name in response_values.keys():
        response_score = calculate_score(weights, response_values[source_name])
        # Adjust scores to a scale of 0.0 (max masc) to 1.0 (max femme).
        score = (response_score - max_masc_score) / (max_femme_score - max_masc_score)
        percent = int(round(score * 100))
        gender = "Feminine"
        if percent < 50:
            percent = 100 - percent
            gender = "Masculine"
        masc_pips = int(round(score, 1) * 30)
        femme_pips = 30 - masc_pips
        scoreline = "▰" * masc_pips + "▱" * femme_pips
        padding = " " * (max(len(filename) for filename in filenames) - len(source_name))
        print(f"[{source_name}] Score: {score:.4f} {padding}(M {scoreline} F :: {percent}% {gender})")
    


if __name__ == '__main__':
    main()