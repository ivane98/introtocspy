base_annual_salary = float(input("Enter your annual salary: "))

total_cost = 1000000
percent_down_payment = 0.25
monthly_r = 0.04 / 12
semi_annual_raise = 0.07
down_payment = total_cost * percent_down_payment
months = 36

epsilon = 100

initial_high = 10000
high = initial_high
low = 0

current_savings = 0
step = 0

portion_saved = (high + low) / 2

while abs(current_savings - down_payment) > epsilon:
    step += 1
    current_savings = 0
    annual_salary = base_annual_salary
    monthly_salary = annual_salary / 12
    monthly_deposit = monthly_salary * (portion_saved / 10000)

    for month in range(1, months + 1):
        current_savings += (current_savings * monthly_r)
        current_savings += monthly_deposit
        if month % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_deposit = monthly_salary * (portion_saved / 10000)

    #  assigns portion_saved to variable prev_portion_saved
    #  to be used as conditional statement to exit from the loop
    prev_portion_saved = portion_saved
    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved

    portion_saved = int(round((high + low) / 2))

    if prev_portion_saved == portion_saved:
        break

if portion_saved == initial_high:
    print("Not possible to acquire the house within 36 months.")
else:
    print("Best savings rate: {}".format(round(portion_saved / 10000, 4)))
    print("Steps in Bisection search: {}".format(step))
