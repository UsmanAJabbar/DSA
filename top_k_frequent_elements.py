def top_k_frequent_elements(nums: list, k: int) -> list:

    def element_counter(arr) -> dict:
        count = {}
        for x in arr:
            count[x] = count.get(x, 0) + 1
        return count

    def key_value_swap_dict(d: dict):
        return {
            value: key
            for key, value in d.items()
        }

    # Returns { element: occurrence_count }
    element_occ_dict = element_counter(nums)

    # Find the key: value that appears most frequently
    max_occurrence_of_any_element = max(element_occ_dict.values())

    # Returns { occurrence_count: element }
    occ_element_dict = key_value_swap_dict(element_occ_dict)

    result = []
    predicted_key = max_occurrence_of_any_element
    while k > 0 and predicted_key != 0:
        if occ_element_dict.get(predicted_key):
            result += [
                occ_element_dict[predicted_key]
            ]
            k -= 1
        predicted_key -= 1

    return result
