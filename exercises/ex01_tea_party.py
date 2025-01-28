"""My first program in COMP110!"""

__author__: str = "730518576"


def main_planner(guests: int) -> None:
    """Defining the Entrypoint of the Program"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


def tea_bags(people: int) -> int:
    """Defining the tea_bags Function"""
    return people * 2


def treats(people: int) -> int:
    """Defining the treats Function"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Defining the cost Function"""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
