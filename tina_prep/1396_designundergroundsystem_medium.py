class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Access and remove the data for id.  Note that removing it is optional, but will have benefits for space complexity
        start_station, start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station, stationName)][0] += (t - start_time)
        self.journey_data[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.journey_data[(startStation, endStation)]
        # the average is simply the total divided by the number of trips
        return total_time / total_trips

# Time Complexity:
# checkIn: Inserting a key/value pair into a HashMap is an O(1) operation
# checkOut: Getting the corresponding value for a key from a HashMap is an O(1) operation
# getAverageTime: Dividing two numbers is an O(1) operation

# Space Complexity:
# O(P + S^2) where S is the number of stations on the network, and P is the number of passengers making a journey concurrently during peak time
# The program uses two HashMaps.  We need to determine the maximum sizes these could become.
# Consider checkInData.  This hashmap holds one entry for each passenger who has checkIn but not checkOut.  Therefore, the maximum size of this hashmap is the maximum possible number of passengers making a journey at the same time, which we defined to be P.  Therefore, the size of this HashMap is O(P)
# Consider journeyData.  This Hashmap has one entry for each pair of stations that has had at least one passenger start and end a journey at those stations.  Over time, we could reasonably expect every possible pair of the S stations on the network to have an entry in this Hashmap, which would be O(S^2).
# Seeing as we don't know whether S^2 or P is larger, we need to add these together giving a total space complexity of O(P + S^2)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# initialize a checkIn dictionary for the customer with key id and value time
# initialize a checkOut dictionary for the customer with key id and value time
