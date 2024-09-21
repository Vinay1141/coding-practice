MOD = 10**9 + 7

def getCount(N):
    if N == 1:
        return 4
    
    # Initialize the number of ways to configure the first storey
    previous = [1, 1, 1, 1]  # dp[0]: 1 house, 2 houses, 3 houses, 4 houses
    
    for i in range(1, N):
        current = [0] * 4
        
        # Transition states: dp[i][j] depends on dp[i-1][k] for k in {1, 2, 3, 4}
        current[0] = (previous[1] + previous[2] + previous[3]) % MOD
        current[1] = (sum(previous) % MOD)
        current[2] = (sum(previous) % MOD)
        current[3] = (sum(previous) % MOD)
        
        # Move to the next state
        previous = current
    
    # Return the sum of the ways to configure the last storey
    return sum(previous) % MOD

def main():
    N = 10  # Fixed input value for testing
    print(f"Input N: {N}")
    print(getCount(N))

if __name__ == "__main__":
    main()
