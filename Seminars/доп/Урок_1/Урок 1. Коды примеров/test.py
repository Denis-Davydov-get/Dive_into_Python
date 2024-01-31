task_1
for j in range(len(lst_obj)):          # !!! O(n)
        if lst_obj[j] in lst_obj[j+1:]:    # !!! O(n)
            return False                   # !!! O(1_base)
    return True                            # !!! O(1_base)
    # T(n) = n * n + 1_base + 1_base = n**2_type_data + 2_type_data
