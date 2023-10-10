def attack(oracle, pi_func, p):
    # Initialize counters for the number of queries to oracle
    queries = 0

    # Step 1: Query the oracle with 0 to get the result for 0
    query_result_0 = oracle(0)
    queries += 1

    # Check if the number of queries has exceeded 5
    if queries > 5:
        return 0

    # Step 2: Use the multiplicative inverse property to query the oracle with pi_func(1)
    query_result_pi_1 = oracle(pi_func(1))
    queries += 1

    # Check if the number of queries has exceeded 5
    if queries > 5:
        return 0

    # Step 3: Use the information gathered to predict 'b'
    if query_result_0 == query_result_pi_1:
        # If oracle(0) and oracle(pi_func(1)) give the same result, it's likely a random permutation
        predicted_b = 1
    else:
        # Otherwise, it's likely a PRP
        predicted_b = 0

    # Step 4: Return the predicted 'b'
    return predicted_b
