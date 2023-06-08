def loading_bar(some_number):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percents = some_number // 10
    return f"{some_number}% [{'%' * loaded_percents}{'.' * (10 - loaded_percents)}]\nStill loading..."


number = int(input())
print(loading_bar(number))


# def loading_bar(number):
#     if number == 100:
#         print('100% Complete!')
#         print('[%%%%%%%%%%]')
#     else:
#         loading = int(number / 10)
#         needed_percent = 10 - loading
#         print(f"{number}% [{'%' * loading}{'.' * needed_percent}]")
#         print('Still loading...')
#
#
# given_number = int(input())
# (loading_bar(given_number))
