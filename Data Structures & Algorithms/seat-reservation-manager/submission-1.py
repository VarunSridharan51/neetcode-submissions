class SeatManager:
    def __init__(self, n: int):
        # self.seats = [False] * n
        self.seats = list(range(1, n+1))
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

        # for i in range(len(self.seats)):
        #     if not self.seats[i]:
        #         self.seats[i] = True
        #         return i + 1
        
    def unreserve(self, seatNumber: int) -> None:
        # self.seats[seatNumber - 1] = False
        heapq.heappush(self.seats, seatNumber)
