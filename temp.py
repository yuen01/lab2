def display_main_menu():
    print()


def calc_avg(a, b, c, d, e):
    total = a + b + c + d + e
    average = total / 5
    return average


def get_user_input():
    user_input = input("Enter a sequence of numbers separated by commas: ")
    input_list = user_input.split(",")

    try:
        float_list = [float(item) for item in input_list]
        return float_list
    except ValueError:
        print("Error: Please enter valid numeric values separated by commas.")
        return []


def find_min_max(float_list):
    if not float_list:
        return [None, None]
    min_temp = min(float_list)
    max_temp = max(float_list)
    return [min_temp, max_temp]


def sort_temperature(float_list):
    sorted_list = sorted(float_list)
    return sorted_list


def calc_median_temperature(float_list):
    sorted_list = sort_temperature(float_list)
    n = len(sorted_list)
    if n % 2 == 0:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        median = sorted_list[n // 2]
    return median


def main():

    user_values = get_user_input()

    if len(user_values) == 5:
        a, b, c, d, e = user_values
        average = calc_avg(a, b, c, d, e)
        min_max = find_min_max(user_values)
        sorted_values = sort_temperature(user_values)
        median = calc_median_temperature(user_values)

        print("Average Temperature =", average)
        print("Min and Max Temperatures =", min_max)
        print("Sorted Temperatures =", sorted_values)
        print("Median Temperature =", median)
    else:
        print("You must enter exactly 5 numeric values separated by commas.")


if __name__ == "__main__":
    main()