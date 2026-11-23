"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # # sort by start time
        # starts = sorted(i.start for i in intervals)
        # # sort by end time 
        # ends = sorted(i.end for i in intervals)

        # min_rooms = 0
        # e = 0

        # for s in starts:
        #     if s < ends[e]:
        #         min_rooms += 1
        #     else:
        #         e += 1	
        # return min_rooms


        # sort by start time
        sorted_intervals = sorted(intervals, key = lambda x : x.start)
        ends = []
        for meeting in sorted_intervals:
            if ends and ends[0] <= meeting.start: #check if room is free
                heapq.heappop(ends)
            heapq.heappush(ends, meeting.end) # opening a room
        return len(ends)


