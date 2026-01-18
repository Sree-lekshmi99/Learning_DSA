class AuctionSystem:

    def __init__(self):

        self.bids = defaultdict(dict)
        self.heap = defaultdict(list)
        
        

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bids[(itemId, userId)] = bidAmount
        heapq.heappush(self.heap[itemId], (-bidAmount, -userId))
        

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.bids[(itemId, userId)] = newAmount
        heapq.heappush(self.heap[itemId],(-newAmount,-userId))
        

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.bids[(itemId, userId)]
        

    def getHighestBidder(self, itemId: int) -> int:
        h = self.heap[itemId]
        while h:
            price = -h[0][0]
            userId = -h[0][-1]

            if self.bids.get((itemId, userId)) == price:
                return userId
            heapq.heappop(h)
        return -1        


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)