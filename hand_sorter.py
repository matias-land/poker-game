def values_val(lst):
    values = [item[1] for item in lst]
    def replace_values(values_list, check_list, replace_list):
        replace_mapping = dict(zip(check_list,replace_list))
        replaced_list = [replace_mapping.get(value, value)for value in values_list]
        return replaced_list
    check_list=['2','3','4','5','6','7','8','9','t','j','q','k','a']
    replace_list = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    values = replace_values(values, check_list, replace_list)
    lst = lst
    def bubble_sort(values):
        n = len(values)
    # Traverse through all elements in the list
        for i in range(n):
        # Track if any swaps were made during this pass
            swapped = False
        # Last i elements are already in place
            for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
                if values[j] > values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    #print(values)
                    #print(lst)
                    swapped = True
        # If no two elements were swapped by inner loop, then break
            if not swapped:
                break
        return values
    values = bubble_sort(values)
    return lst