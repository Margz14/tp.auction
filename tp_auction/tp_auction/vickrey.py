from utils import Cli
from itertools import count

from auction import Auction 

class VickreyAuction(Auction):

    def __init__(self,cli=None):
        super().__init__(cli)
        

    def auction_loop(self, opening_bid, bidders):
        self.cli.display(f'Started auction of type: Vickrey')
        opening_bid = int(opening_bid)
        standing_bid = opening_bid
        self.winner = None
        history= []
        if len(bidders)==1:
            winner = bidders[0] 
            bid = self.cli.prompt(
                                f"Opening bid is {opening_bid}. {bidder} bids:"
                            )
            bid = int(bid)
            price = opening_bid
        else : 
            for bidder in bidders:
                bid = self.cli.prompt(
                    f"Opening bid is {opening_bid}. {bidder} bids:"
                )
                bid = int(bid)
                history.append((bid, bidder))
                if bid > standing_bid:
                    standing_bid = bid
                    winner = bidder
            history.sort(reverse=True)
            price=history[1][0]
        return winner, price 

if __name__ == "__main__":
    auction = VickreyAuction()
    auction.play()
