employee_id = 1001
employee_name = "Alice"
employee_department = "IT"
hourly_rate = 25.50
hours_worked_this_week = 50
is_active_employee = True

print(f"Employee ID: {employee_id}, Type: {type(employee_id)}")
print(f"Employee Name: {employee_name}, Type: {type(employee_name)}")
print(f"Employee Department: {employee_department}, Type: {type(employee_department)}")
print(f"Employee Hourly Rate: {hourly_rate}, Type: {type(hourly_rate)}")
print(f"Hours Worked In This Week: {hours_worked_this_week}, Type: {type(hours_worked_this_week)}")
print(f"Active Employee: {is_active_employee}, Type: {type(is_active_employee)}")

weekly_gross_pay = hourly_rate * hours_worked_this_week
print(f"Weekly gross pay: {weekly_gross_pay:.1f}")

bonus_input = input("Enter a one-time bonus amount for the employee: ")
bonus_amount = float(bonus_input)

total_pay_with_bonus = weekly_gross_pay + bonus_amount
print(f"Total pay with bonus: {total_pay_with_bonus}")

duration_in_month = int(input("Enter employment duration: "))
on_probation = True
if duration_in_month >= 3:
    on_probation = False
print(f"Probation: {on_probation}")

is_eligible_for_benefits = False
if is_active_employee and not on_probation:
    is_eligible_for_benefits = True
print(f"Eligible for benefits: {is_eligible_for_benefits}")
