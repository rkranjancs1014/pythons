class Capital_gain_inStock:
    def __init__(self):
        self._data = ArrayQueue()
    def buy(self, no_of_shares, share_price):
        self._data.enqueue((no_of_shares, share_price))
    def sell(self, no_of_shares, share_rate):
        share_counter = no_of_shares
        capital = 0
        while(not self._data.is_empty() and share_counter != 0):
            pop_share = self._data.dequeue()
            if pop_share[0] > share_counter:
                push_share = (pop_share[0] - no_of_shares, pop_share[1])
                capital = capital + (share_rate - pop_share[1]) * share_counter
                self._data.enqueue(push_share)
                share_counter = 0
            else:
                share_counter = share_counter - pop_share[0]
                capital = capital + (share_rate - pop_share[1]) * pop_share[0]
        return capital
