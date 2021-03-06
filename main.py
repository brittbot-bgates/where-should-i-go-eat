#!/usr/bin/env python3
"""
Title: Where Should I Go Eat?
Creator: Brittany Gates (https://github.com/brittbot-bgates)
About: If you're hungry and unsure of where to go, this app randomly tells you where to go eat with a click of a button.
"""

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def blank():
    """
    :return: The function returns the blank index.html website without a restaurant chosen. It is also used to
    clear the website of any choices if the reset button is clicked.
    """
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def main():
    """
    This function opens and read the restaurant.txt file which is located in the /static/files directory.
    Then a loop runs over the entire file, reading each line. The loop collects all the lines as a list, and then pulls
    out a restaurant randomly using the random.choice function.

    :return: The function returns a random restaurant to the index.html template, which displays it
    on the website.
    """
    with open("static/files/restaurant.txt", "r") as restaurant:
        restaurant_list = restaurant.readlines()
    return render_template("index.html", restaurant=random.choice(restaurant_list))


if __name__ == "__main__":
    main()
