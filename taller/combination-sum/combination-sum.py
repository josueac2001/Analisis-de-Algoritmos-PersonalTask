class Solution(object):
    def combinationSum(self, candidates, target):

        result = []
        
        def backtrack(start_index, current_target, current_comb):
            if current_target == 0:
                result.append(list(current_comb))
                return
            
            if current_target < 0:
                return
                
            for i in range(start_index, len(candidates)):
                current_comb.append(candidates[i])
                
                backtrack(i, current_target - candidates[i], current_comb)
                
                current_comb.pop()
                
        backtrack(0, target, [])
        return result