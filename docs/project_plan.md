# Capacity Planning Calculator

## Purpose 

Calculate avaliable workforce capacity and compare against current demand. 

## Assumptions 

- All entered employees are under one domain - data engineering 
- No employees are taking PTO/leave of absence 
- General expectation is that employees work 40 hours a week (some will work over or under this number )

## Inputs 

- Number of employees
- Hours each employee works/per week
- Number of projects 
- Number of project hours 

## Process

1. Ask how many employees are on the team.
2. Ask for each employee's available weekly hours.
3. Add those hours together to calculate total team capacity.
4. Ask for total project demand across all active projects.
5. Compare demand against total team capacity.
6. Calculate utilization percentage.
7. Calculate remaining capacity or capacity gap.
8. Display whether the team is under capacity, near capacity, or over capacity.

## Outputs 

- utilization %
- remaining capacity
- gap/surplus

## Future Enhancements 

- Pie chart showing capacity versus demand
- Chart that breakdowns capacity by employee
- Chart that breakdowns demand per customer type 
- Domain specification both for projects and employees 
- Forecasting that projects potential outcomes if employee leaves or PTO periods 
- Forecasting that projects current demand versus future demand 