# Capacity Planning Calculator

## Purpose 

Calculate avaliable workforce capacity and compare against projected demand. 

## Assumptions 

- All entered employees are under one domain - data engineering 
- No employees are taking PTO/leave of absence 
- General expectation is that employees work 40 hours a week (some will work over or under this number )

## Inputs 

- Standard weekly capacity
- Allocated hours per employee
- Number of employees
- New project demand

## Process

1. Ask for standard weekly capacity
2. Ask for number of employees
3. Calculate total maximum capacity
4. Ask for current allocated hours per employee
4. Calculate available capacity per employee
5. Sum total team allocated hours
6. Sum team available capacity
6. Ask for new project demand hours
7. Calculate gap
8. Calculate utilization
9. Display total number of employees
10. Display team available capacity
11. Display new project demand hours
12. Display gap
13. Display utilization
14. Display status: Healthy, At Risk, or Over Capacity

## Outputs 

- utilization %
- status/team health 
- gap/surplus

## Definitions

### Capacity

Total available workforce hours.

Calculated as the sum of all employee hours entered by the user.

### Demand

Total project hours required.

Entered by the user.

### Capacity Gap

Capacity minus demand.

Positive values indicate available capacity.

Negative values indicate a shortage of capacity.

### Utilization Rate

The percentage of available workforce capacity required to meet current demand.

## Future Enhancements 

- Pie chart showing capacity versus demand
- Chart that breakdowns capacity by employee
- Chart that breakdowns demand per customer type 
- Domain specification both for projects and employees 
- Forecasting that projects potential outcomes if employee leaves or PTO periods 
- Forecasting that projects current demand versus future demand 