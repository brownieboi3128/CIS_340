
def compound_by_period2(balance, rate, num_periods):
    """
    Calculates the compounded balance for a specified number of periods.

    This function computes and returns a list of balances, starting with an 
    initial balance and compounding it by a given rate for each period. 
    The list contains the balance at the beginning of each period, including 
    the initial balance.
    """
    balances = [balance]
    for n in range(1,num_periods+1):
        balance = round( balance * (1 + rate), 2)
        balances.append(balance)
    return balances

# wheat: list containing the number of grains of wheat on each square of the chessboard
wheat2 = compound_by_period2(1,1,63)

total_wheat2 = sum(wheat2)


