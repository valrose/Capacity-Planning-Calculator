# Capacity Planning Calculator
# Calculate avaliable workforce capacity and compare against projected deman

from capacity import calculate_capacity_gap
from capacity import calculate_utilization_rate
from capacity import calculate_overall_status

def main():

    # Create list to store team available capacity
    team_capacity = []
    team_allocated_hours = []

    #  Ask for standard weekly capacity
    standard_capacity = int(input(f'Enter standard weekly capacity: '))

    # Ask for number of employees
    team_total = int(input(f'Enter number of employees: '))

    # Calculate total maximum capacity
    total_capacity = standard_capacity * team_total

    # Ask for current allocated hours per employee
    for x in range(team_total):
        allocated_hours = int(input(f'Enter current allocated hours for employee {x + 1}: '))
        available_capacity = standard_capacity - allocated_hours
        team_capacity.append(available_capacity)
        team_allocated_hours.append(allocated_hours)

    # Sum total team allocated hours
    allocated_total = sum(team_allocated_hours)

    # Sum team available capacity
    teamcapacity_total = sum(team_capacity)

    # Ask for new project demand hours
    demand_hours = int(input(f'Enter new project demand hours: '))

    # Calculate gap
    gap = calculate_capacity_gap(teamcapacity_total, demand_hours)

    # Calculate utilization
    utilization = calculate_utilization_rate(allocated_total, demand_hours, total_capacity)

    # Calculate status
    status = calculate_overall_status(gap)

    # Display total number of employees
    print(f'Total number of team members: {team_total}')

    # #Display team available capacity
    print(f'Available team capacity: {teamcapacity_total} hours')

    # Display new project demand hours
    print(f'Total new project demand hours: {demand_hours} hours')

    # Display utilization
    print(f'Projected utilization: {utilization:.2f}%')

    # Display gap
    print(f'Current capacity gap: {gap}')

    # Display status: Healthy, At Risk, or Over Capacity
    print(f'Overall status: {status}')


if __name__ == "__main__":
    main()