import os

def find_highest_bidder(auction_bid):
    highest_bid = 0
    winning_bidder = ""
    for bidder in auction_bid:
        bid_amount = int(auction_bid[bidder]) 
        if bid_amount > highest_bid:
            highest_bid = auction_bid[bidder]
            winning_bidder = bidder
    print(" {} is the highest bidder with £ {}".format(winning_bidder,highest_bid))

print("Welcome to the Secret Auction!")
auction_bid = {}
continue_flag = "y"

while continue_flag != "n":
    name = input("Enter the name of the bidder :-")
    amount = input("Enter the bid amount :- £")
    auction_bid = {name:amount}
    print(auction_bid)
    
    continue_flag = input("Are there more bidders :- enter y or n ").lower()
    os.system('clear')
find_highest_bidder(auction_bid)