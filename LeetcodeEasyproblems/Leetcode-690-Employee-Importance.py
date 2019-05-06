"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {e.id: e for e in employees}
        
        # Init stack based DFS
        stack, seen, out = [d[id]], set(), 0
        
        while stack:
            curr = stack.pop()
            # Add importance to output
            # Mark id as seen 
            if curr.id not in seen:
                out += curr.importance
                seen.add(curr.id)
            # Push subs to stack
            for id in curr.subordinates:
                stack.append(d[id])
        return out
        