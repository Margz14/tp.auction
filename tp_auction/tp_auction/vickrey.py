from utils import Cli
from itertools import count

from auction import Auction 

class VickreyAuction(Auction):

    def __init__(self,cli , name):
        super().__init__(cli)
        self.name=name


    def auction_loop(self, opening_bid, bidders):
        standing_bid = opening_bid
        self.winner = None
        history= []
        if len(bidders)==1:
            bidder = bidders[0] 
            bid = self.cli.prompt(
                                f"Opening bid is {opening_bid}. {bidder} bids:"
                            )
            bid = int(bid)
            winner = bidder
            price = opening_bid
        else : 
            for bidder in bidders:
                bid = self.cli.prompt(
                    f"Opening bid is {opening_bid}. {bidder} bids:"
                )
                bid = int(bid)
                if bid > opening_bid:
                    history.append((bid, bidder))
                if bid > standing_bid:
                    standing_bid = bid
                    winner = bidder
            history.sort(reverse=True)
            price=history[1][0]
        return winner, price 

if __name__ == "__main__":
    auction = VickreyAuction(Cli,"Vickey")
    auction.play()
