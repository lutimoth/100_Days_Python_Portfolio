from art import logo
import os

print(logo)
print("Welcome to the Auction")

auction = True
bids = {}

while auction:
    name = input("Please input your name: ")
    bid_price = int(input("Please input your bid: ").strip('$'))
    bids[name] = bid_price

    more_bid = input("Are there any other users who would like to bid? (y/n): ")

    while True:
        if more_bid not in ('y','n'):
            print("invalid entry")
        elif more_bid == 'y':
            os.system('cls')
            break
        else:
            os.system('cls')
            auction = False
            break

# Alternative method is to use a for loop to iterate and compare historic values
highest_bidder = max(bids, key = bids.get)

print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}.")