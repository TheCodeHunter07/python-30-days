# ASSIGNMENT
# 2 profile.py — a function that takes **kwargs and prints a formatted profile


def display_profile(**kwargs):

    for key, value in kwargs.items():

        print(key, ":", value)

display_profile(
    name="Sumit",
    age=22,
    role="Python Developer",
    city="Pune"
)