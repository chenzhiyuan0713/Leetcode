def solution(n, battery):
    answer = 0
    single_price = [i[1]//i[0] for i in battery]
    unit_size = [i[0] for i in battery]

    cheapest_single = min(single_price), single_price.index(min(single_price))
    all_bundle = [i[0]*i[1] for i in battery]
    cheapest_bundle = min(all_bundle)

    max_count_chp = n // unit_size[cheapest_single[1]]

    answer += cheapest_single[0] * unit_size[cheapest_single[1]] * max_count_chp
    # used_money = cheapest_single[0] * unit_size[cheapest_single[1]] * max_count_chp
    # remain = n - unit_size[cheapest_single[1]] * max_count_chp

    return answer


print(solution(50, [[10, 1000000], [4, 35000], [1, 15000]]))