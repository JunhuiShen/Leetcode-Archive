# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.

 

# Example 1:

# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.
# Example 2:

# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
# - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
# - In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
# The total hiring cost is 4.
 

# Constraints:

# 1 <= costs.length <= 105 
# 1 <= costs[i] <= 105
# 1 <= k, candidates <= costs.length

import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        m = candidates
        n = len(costs)
        # Initialize two priority queues head_workers and tail_workers
        # head_workers stores the first m workers
        # tail_workers stores the last m workers, adjusted to handle cases where m > n
        head_workers = costs[:m]
        tail_workers = costs[max(m, n - m):]

        # The worker with the lowest cost has the highest priority
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        # Set up two pointers: next_head indicates the next worker to be added to head_workers
        # next_tail indicates the next worker to be added to tail_workers
        answer = 0
        next_head = m
        next_tail = n - m - 1

        # Repeat the process k times to hire k workers
        for i in range(k):
            # Compare the top workers in both queues and hire the one with the lowest cost
            # Case I: The hired worker is from head_workers
            if not tail_workers or (head_workers and head_workers[0] <= tail_workers[0]): 
                answer += heapq.heappop(head_workers)
            
            # If there are still workers left to be added to head_workers, add the next one
                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            
            # Case II: the hired worker is from tail_workers
            else:
                answer += heapq.heappop(tail_workers)
               # If there are still workers left to be added to tail_workers, add the next one
                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1
        
        return answer

# Test case
costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

# Create an instance of Solution
solution = Solution()

# Call the totalCost method
result = solution.totalCost(costs, k, candidates)
print(result)