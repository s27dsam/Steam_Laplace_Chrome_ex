from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def find_review_elements(soup):
    elements = soup.findAll('span', class_='user_reviews_count')
    return elements


def extract_numbers_from_elements(elements):
    numbers = []
    for element in elements:
        numbers.append("".join(re.findall(r"\d+", element.text)))
    return numbers


def convert_strings_to_integers(numbers):
    return [int(number) for number in numbers]


def get_reviews_percentage(url):
    soup = get_soup(url)
    elements = find_review_elements(soup)
    numbers = extract_numbers_from_elements(elements)
    int_reviews = convert_strings_to_integers(numbers)

    int_reviews[1] = int_reviews[1] + 1
    int_reviews[0] = int_reviews[0] + 2
    new_cal = int_reviews
    new_percentage = (new_cal[1] / new_cal[0]).__round__(2) * 100

    return 'Laplace Percentage: {}%'.format(new_percentage)


@app.get("/laplace_smoothing_percentage/")
def read_item(url: str):
    return get_reviews_percentage(url)