class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source==target:
            return 0
        
        revStopMap=defaultdict(list)

        for bus,route in enumerate(routes):
            for stops in route:
                revStopMap[stops].append(bus)
        
        if source not in revStopMap or target not in revStopMap:
            return -1
        q=deque()
        # for route in revStopMap[source]:
        #     time, bus = route
        visited=set([source])
        visitedBus=set()
        changes=0
        q.append(source)
        while q:
            size = len(q)

            for _ in range(size):
                stop = q.popleft()
                if stop == target:
                    return changes
                for bus in revStopMap[stop]:
                    if bus not in visitedBus:
                        for stops in routes[bus]:
                            if stops not in visited:
                                q.append(stops)
                    visitedBus.add(bus)

            changes+=1
        return -1