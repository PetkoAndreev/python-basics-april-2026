# Calculate deposit profitability
deposit_sum = float(input())
maturuty_in_months = int(input())
int_rate = float(input())
# Formula to calculate total sum of deposit
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент / 100 ) / 12)
profitability = deposit_sum + (maturuty_in_months * \
                               (\
                                   (deposit_sum * \
                                 (int_rate/100) / \
                                 12)\
                                   )\
                               )
print(profitability)