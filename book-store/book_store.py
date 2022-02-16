from typing import Dict, List
from collections import Counter


INDIVIDUAL_BOOK_COST = 8
MULTIPLIER = 100
QUANTITY_TO_DISCOUNTED_COST_MAP: Dict[int, int] = {
    0: 0,
    1: INDIVIDUAL_BOOK_COST * (100 - 0),
    2: INDIVIDUAL_BOOK_COST * (100 - 5),
    3: INDIVIDUAL_BOOK_COST * (100 - 10),
    4: INDIVIDUAL_BOOK_COST * (100 - 20),
    5: INDIVIDUAL_BOOK_COST * (100 - 25),
}

DISCOUNTABLE_QUANTITIES = set(QUANTITY_TO_DISCOUNTED_COST_MAP)


def basket_to_cost(basket: List[int], indentation="") -> int:
    """given a basket calculate combinations of costs"""
    if not basket:
        return 0
    if len(basket) == 1:
        return QUANTITY_TO_DISCOUNTED_COST_MAP[1]

    counted_basket = Counter(basket)
    assert len(counted_basket) in DISCOUNTABLE_QUANTITIES
    # iterate over all possible discount maps starting from largest valid
    # to smallest
    largest_valid_map = min(len(counted_basket), max(DISCOUNTABLE_QUANTITIES))
    combination_costs = []
    for starting_discount_map in range(largest_valid_map, 0, -1):
        this_combination = list(counted_basket)[:starting_discount_map]
        this_combination_size = len(this_combination)
        remaining_combination = counted_basket - Counter(this_combination)
        this_combination_cost = (
            this_combination_size
            * QUANTITY_TO_DISCOUNTED_COST_MAP[this_combination_size]
        )
        print(
            f"{indentation}{basket=} {largest_valid_map=} {starting_discount_map=} {this_combination=} {this_combination_size=} = {this_combination_cost}"
        )
        remaining_combination_cost = (
            basket_to_cost(list(remaining_combination), indentation=indentation + "  ")
            if remaining_combination
            else 0
        )
        print(
            f"{indentation}{basket=} {this_combination_cost=} + {remaining_combination_cost=} = {remaining_combination_cost+this_combination_cost}"
        )
        combination_costs.append(this_combination_cost + remaining_combination_cost)

    result = min(combination_costs)
    print(f"{indentation}{basket=} => {result}")
    return result


def total(basket: List[int]) -> int:
    if not basket:
        return 0

    result = basket_to_cost(basket)
    print(f"start {basket} -> {result}")

    return result
