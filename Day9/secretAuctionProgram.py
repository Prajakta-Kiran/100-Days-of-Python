print("Welcome to secret auction program!!")
auction_dict = {}
wants_to_bid = True

def find_highest_bid(auction_val):
    highest_auct_val = 0
    winner = ""
    for name in auction_val:
        if auction_val[name] > highest_auct_val:
            highest_auct_val = auction_val[name]
            winner = name
    print(f"Highest Auction Bid is {highest_auct_val}")
    print(f"The highest bidder of today's auction is {name} with auction value as {highest_auct_val}")

while wants_to_bid:
    bidder_name = input("What is your name?\n")
    bid_value = int(input("How much you want to bid?\n"))
    auction_dict[bidder_name] = bid_value
    continue_bidding = input("Anyone wants to bid?Type'yes'or 'no'\n")
    if continue_bidding=='no':
        wants_to_bid = False
        find_highest_bid(auction_dict)
        






    


