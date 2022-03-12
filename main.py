from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bid_dict = {}
continue_flag = False

while continue_flag == False:
  name = input("What's your name? ")
  bid = input("What's your bid? $")
  bid_dict[name] = bid
  bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if bidder == "yes":
    clear()
  else:
    continue_flag = True

max_bid = max(bid_dict, key=bid_dict.get)
#print(bid_dict)
#print(max_bid)
print(f"The winner is {max_bid} with a bid of ${bid_dict[max_bid]}")
