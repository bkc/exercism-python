def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    result = sorted(select_shortest_combination(sorted(coins, reverse=True), target))
    if sum(result) != target:
        raise ValueError("can't make target with given coins")

    return result


def select_shortest_combination(coins, target):
    shortest_combination = []
    valid_coins = [_ for _ in coins if _ <= target]
    while valid_coins:
        highest_coin = valid_coins.pop(0)
        this_coin_count, remainder = divmod(target, highest_coin)
        if shortest_combination and this_coin_count > len(shortest_combination):
            # cannot make a shorter combination
            continue
        if not valid_coins and remainder:
            # there's no way to solve with this combination
            break

        while True:
            this_combination = [highest_coin] * this_coin_count
            this_combination.extend(
                select_shortest_combination(
                    valid_coins,
                    remainder,
                )
                if remainder and valid_coins
                else []
            )
            if sum(this_combination) == target and (
                not shortest_combination
                or len(this_combination) < len(shortest_combination)
            ):
                shortest_combination = this_combination
            this_coin_count -= 1
            if (
                not this_coin_count
                or not valid_coins
                or (
                    shortest_combination
                    and len(shortest_combination)
                    < this_coin_count + (remainder + highest_coin) // valid_coins[0]
                )
            ):
                # any other combinations will be longer than what we have or
                # no additional combinations can be made
                break
            remainder += highest_coin

    return shortest_combination
