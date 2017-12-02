"""
    test for jenkins
"""

def highest_affinity(site_list, user_list, time_list):

    n = len(site_list)
    if n == 0:
        print("empty")
        return ()
    if len(user_list) != n or len(time_list) != n:
        print("not same length")
        return ()
    record = dict()
    for i in range(n):
        if site_list[i] in record:
            if user_list[i] not in record[site_list[i]]:
                record[site_list[i]].append(user_list[i])
        else:
            record[site_list[i]] = [user_list[i]]
    max_aff = -1
    for key in record:
        for another_key in record:
            if key != another_key:
                common = [f for f in record[key] if f in record[another_key]]
                if len(common) > max_aff:
                    max_aff = len(common)
                    max_pair = (
                        another_key, key) if another_key < key else (
                        key, another_key)
    return max_pair
