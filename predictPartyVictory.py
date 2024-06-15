# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. 
# In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. 
# Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. 
# This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. 
# Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

# Constraints:

# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.

from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        # Convert the senate string to a deque for easy manipulation
        newqueue = deque(list(senate))

        # Counters for the number of bans each party has accumulated
        r_before_count = 0
        d_before_count = 0

        # Continue until only one type of senator is left in the queue
        while len(set(newqueue)) > 1:
            # Take the next senator from the front of the queue
            takeout_element = newqueue.popleft()
            if takeout_element == "D":
                # If the senator is 'D', check if they can be banned by 'R'
                if r_before_count == 0:
                    # If no 'R' bans are available, this 'D' senator stays in the queue
                    newqueue.append(takeout_element)
                    # Increment the 'D' bans counter
                    d_before_count += 1
                else:
                    # If an 'R' ban is available, use it to ban this 'D' senator
                    r_before_count -= 1
            else:
                # If the senator is 'R', check if they can be banned by 'D'
                if d_before_count == 0:
                    # If no 'D' bans are available, this 'R' senator stays in the queue
                    newqueue.append(takeout_element)
                    # Increment the 'R' bans counter
                    r_before_count += 1
                else:
                    # If a 'D' ban is available, use it to ban this 'R' senator
                    d_before_count -= 1
        
        # Determine the winning party based on the remaining senators
        final_element = newqueue.popleft()
        if final_element == "D":
            return "Dire"
        else:
            return "Radiant"