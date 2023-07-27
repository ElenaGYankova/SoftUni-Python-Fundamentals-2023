def check_ticket_side(ticket_side):
    uninterrupted_match_length = 0
    match_symbol = ""
    for symbol in ticket_side:
        if symbol != match_symbol:
            if uninterrupted_match_length >= 6:
                break
            uninterrupted_match_length = 1
            match_symbol = symbol
        else:
            uninterrupted_match_length += 1
    return uninterrupted_match_length, match_symbol


tickets = [x.strip() for x in input().split(", ")]
special_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if ticket[0] in special_symbols and ticket[0] * 20 == ticket:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        else:
            first_side = ticket[:10]
            second_side = ticket[10:]
            side_one_uninterrupted, side_one_symbol = check_ticket_side(first_side)
            side_two_uninterrupted, side_two_symbol = check_ticket_side(second_side)
            winning_length = min(side_one_uninterrupted, side_two_uninterrupted)
            if side_one_symbol == side_two_symbol and side_two_symbol in special_symbols and winning_length >= 6:
                print(f'ticket "{ticket}" - {winning_length}{side_one_symbol}')
            else:
                print(f'ticket "{ticket}" - no match')
