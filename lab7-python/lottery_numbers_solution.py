from bst_solution import BST

class LotteryTicket:
    def __init__(self, name : str, nums : list) -> None:
        self.name = name
        self.nums = nums

class Lottery:
    # Construct lottery numbers from an input list of 5 numbers.
    def __init__(self, nums) -> None:
        if len(nums) != 5:
            raise ValueError("nums should have exactly 5 numbers")
        self._nums = BST()
        for num in nums:
            self._nums.insert(num)

    # Determine if the ticket is winning. A ticket wins if all 5 numbers on the ticket
    # match the 5 lottery numbers.
    # If it is winning, print "Congratuations, <owner name>, you win!"
    # Else, print "Sorry, <owner name>, no win today."
    def check_ticket(self, ticket : LotteryTicket) -> None:
        has_non_matching = False
        for num in ticket.nums:
            if not self._nums.find(num):
                has_non_matching = True
                break
        if has_non_matching:
            print(f"Sorry, {ticket.name}, no win today.")
        else:
            print(f"Congratulations, {ticket.name}, you win!")

if __name__ == "__main__":
    bobs_ticket = LotteryTicket("Bob", [1, 2, 3, 4, 5])
    susans_ticket = LotteryTicket("Susan", [48, 9, 22, 30, 11])

    lottery = Lottery([11, 22, 9, 48, 30])
    lottery.check_ticket(bobs_ticket)
    lottery.check_ticket(susans_ticket)
