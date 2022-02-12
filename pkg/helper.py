from typing import List
import random

from .term_list import list_of_terms

def random_name(join_string: str, min_length: int = 3, max_length: int = 5) -> str:
    amountOfTerms = random.randint(min_length, max_length)

    terms: List[str] = []
    for i in range(0, amountOfTerms):
      terms.append(list_of_terms[random.randint(0, len(list_of_terms) - 1)])

    return join_string.join(terms)

def write_output(item_list: List[str], output_file_name: str) -> None:
    with open(output_file_name, "w") as f:
        for item in item_list:
            f.write(item)
            f.write("\n")

def read_output(output_file_name: str) -> list[str]:
    lines: List[str] = []
    with open(output_file_name, "r") as f:
        lines = f.readlines()
    return lines