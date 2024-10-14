import heapq

def battle(monsters):
    # Create a max-heap by negating the values
    heap = [-m for m in monsters]
    heapq.heapify(heap)
    
    # Simulate the battle
    while len(heap) > 1:
        # Get the two strongest monsters
        monster_1 = -heapq.heappop(heap)
        monster_2 = -heapq.heappop(heap)
        
        # If they have the same power, both perish
        if monster_1 > monster_2:
            # The remaining power of monster_1 is monster_1 - monster_2
            heapq.heappush(heap, -(monster_1 - monster_2))
    
    # Determine the outcome
    if len(heap) == 1:
        print("I have won, but at what cost?")
    else:
        print("Nobody won!")

# Example usage:
monsters = [9,8,7,6]
battle(monsters)
