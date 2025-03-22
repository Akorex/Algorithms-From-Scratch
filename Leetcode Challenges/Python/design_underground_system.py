"""
Solution to Leetcode problem #1396 - Design Underground System


"""

class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {} # id -> (stationName, time)
        self.travel_times = {} # (start, end) -> (totalTime, tripCounts)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
       self.check_in_data[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in_data:
            startStation, startTime = self.check_in_data.pop(id)
            travelTime = t - startTime

            if (startStation, stationName) not in self.travel_times:
                self.travel_times[(startStation, stationName)] = [0,0]

            self.travel_times[(startStation, stationName)][0] += travelTime
            self.travel_times[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, tripCounts = self.travel_times[(startStation, endStation)]
        return totalTime/tripCounts

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)