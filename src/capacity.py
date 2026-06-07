# Capacity Logic
# Contains capacity and utilization functions for employee capacity calculator

def calculate_capacity_gap(teamcapacity_total, demand_hours):
    capacity_gap = teamcapacity_total - demand_hours
    return capacity_gap

def calculate_utilization_rate(allocated_total, demand_hours, total_capacity):
    utilization_rate = (allocated_total + demand_hours)/total_capacity * 100
    return utilization_rate

def calculate_overall_status(gap):
    if gap >= 20:
        overall_status = 'Healthy'
    elif 0 < gap < 20:
        overall_status = 'At Risk'
    elif gap < 0:
        overall_status = 'Over Capacity'
    return overall_status