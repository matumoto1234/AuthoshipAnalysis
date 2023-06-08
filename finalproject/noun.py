import nltk
nltk.download('punkt', quiet=True)
from utility import *


def _count_noun(text: str) -> tuple[int, int]:
    return count_n_gram(text, ["NN"])


def noun_token_ratio(text: str):
    return (_count_noun(text) / count_token(text)) * 100


def _authors_noun_token_ratio_average(authors: list[str], author_to_texts: dict[str, list[list[str]]]):
    ratio_sum = 0
    num_of_text = 0

    for author in authors:
        for text in author_to_texts[author]:
            ratio_sum += noun_token_ratio(text)
            num_of_text += 1

    if num_of_text == 0:
        return 0

    return ratio_sum / num_of_text


def noun_token_ratio_label(male_authors: list[str], female_authors: list[str], author_to_texts: dict[str, list[list[str]]]) -> tuple[float, float]:
    return (
        _authors_noun_token_ratio_average(male_authors, author_to_texts),
        _authors_noun_token_ratio_average(female_authors, author_to_texts)
    )

