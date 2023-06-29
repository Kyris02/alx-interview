#!/usr/bin/python3

def isWinner(x, nums):
    wins = {"Maria": 0, "Ben": 0}

    # Helper function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(x):
        n = nums[i]
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        game_over = False
        turn = "Maria"

        while not game_over:
            # Maria's turn
            if turn == "Maria":
                if not primes:
                    wins["Ben"] += 1
                    game_over = True
                else:
                    num = primes.pop(0)
                    primes = [p for p in primes if p % num != 0]
                    turn = "Ben"
            # Ben's turn
            else:
                if not primes:
                    wins["Maria"] += 1
                    game_over = True
                else:
                    num = primes.pop(0)
                    primes = [p for p in primes if p % num != 0]
                    turn = "Maria"

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
