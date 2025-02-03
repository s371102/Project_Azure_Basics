from datetime import datetime

def solution(E, L):
    # Parse the entry and exit times
    format = "%H:%M"
    start_time = datetime.strptime(E, format)
    end_time = datetime.strptime(L, format)

    print(start_time)
    print(end_time)

    # Calculate total minutes between entry and exit
    total_minutes = (end_time - start_time).total_seconds() / 60

    # Base cost
    cost = 2

    # First hour cost
    if total_minutes > 0:
        cost += 3

    # Additional full or partial hours after the first
    if total_minutes > 60:
        additional_hours = (total_minutes - 60) / 60
        cost += int(additional_hours) * 4 + (4 if additional_hours % 1 > 0 else 0)

    return int(cost)

E = input("Enter the start time:")
L = input("Enter the exit time")

# Example usage
print(solution(E,L))  # Output: 17


