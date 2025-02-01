import statistics

def validate_temperature(value):

    try:
        value = float(value)
    except ValueError:
        return "Invalid input"
    if value >= -50 or value <= 150:
        return value
    return "Not within valid range"

def process_temperatures(temp_list):
    """Process the list of temperatures and return min, max, and avg."""
    # valid_temps = [float(temp) for temp in temp_list]
    # valid_temps = [validate_temperature(temp) for temp in temp_list if validate_temperature(temp) is not None]
    valid_temps = []

    for temp in temp_list:
        valid_temp = validate_temperature(temp)
        if isinstance(valid_temp, str):
            return  valid_temp
        else:
            valid_temps.append(valid_temp)


    if not valid_temps:
        return "No valid input provided."

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


# Test Cases
# Students should analyze and ensure the correctness of the outputs

test_cases = [
    [20],  # Lower boundary
    [15, 35],  # Upper boundary
    [],
    [10, -10, 30],
    [-50, 20, 150, 25],
    [10, "abc",30],
    [2**31 - 1, - 2**31],
    [10, 10, 10]
]
# Values inside range



# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 40)