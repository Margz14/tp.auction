# TODO !
class Auction:
    def __init__(self,cli, name):
        super().__init__(cli)
        self.name=name
    
    def prixdepart(self):
        self.cli.display(f'Started auction of type: {self.name}')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        self.opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {self.opening_bid}")
        return self.opening_bid

    def encherisseurs(self):
        self.bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            self.bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(self.bidders)}\n")
        return self.bidders 

    def gagnants(self, winner , standing_bid):
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")

