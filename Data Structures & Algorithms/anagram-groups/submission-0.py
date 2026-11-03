class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in seen:
                seen[key].append(i)
            else:
                seen[key] = [i]
        
        output = []
        for i in seen:
            output.append(seen[i])
        return output 

