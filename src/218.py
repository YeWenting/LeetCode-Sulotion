import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        i, act_bd, ans = 0, [], []
        while (i < len(buildings) or act_bd):
            if (i < len(buildings) and (not act_bd or buildings[i][0] <= -act_bd[0][1])):
                # This building is under the reach of highest BD
                start_x, prev_max = buildings[i][0], -act_bd[0][0] if act_bd else 0
                while i < len(buildings) and start_x == buildings[i][0]:
                    heapq.heappush(act_bd, (-buildings[i][2], -buildings[i][1]))
                    i += 1
                if prev_max != -act_bd[0][0]:
                    ans.append([start_x, -act_bd[0][0]])
            else:
                # Remove current highest BD
                end_x = -act_bd[0][1]
                while (act_bd and -act_bd[0][1] <= end_x):
                    heapq.heappop(act_bd)
                if (not ans or (-act_bd[0][0] if act_bd else 0) != ans[-1][1]):
                    ans.append([end_x, -act_bd[0][0] if act_bd else 0])
        return ans