import timeit
import random

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum_: int):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin

        if count > 0:
            count_coins[coin] = count

        sum_ -= coin * count

    return count_coins


def find_min_coins(sum_: int):
    min_coins_required = [0] + [float("inf")] * sum_
    last_coin_used = [0] * (sum_ + 1)

    for s in range(1, sum_ + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    count_coins = {}
    current_sum = sum_

    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum -= coin

    return count_coins


def test_find_coins_greedy(data_set, func):
    results = []
    for data in data_set:
        results.append(func(data))


if __name__ == "__main__":
    data_set = [random.randint(1_000, 2_000) for _ in range(1000)]

    time_for_greedy = timeit.timeit(
        lambda: test_find_coins_greedy(data_set[:], find_coins_greedy), number=10
    )
    time_for_min_coins = timeit.timeit(
        lambda: test_find_coins_greedy(data_set[:], find_min_coins), number=10
    )

    print(f"{'|Algorithm': <21} | {'Time to complete': <20}|")
    print(f"|{'-'*20} | {'-'*20}|")
    print(f"|{'Greedy': <20} | {time_for_greedy: <20.5f}|")
    print(f"|{'Min coins': <20} | {time_for_min_coins: <20.5f}|")

    print(
        f"\nGreedy is {time_for_min_coins / time_for_greedy:.2f} times faster than min coins"
    )
