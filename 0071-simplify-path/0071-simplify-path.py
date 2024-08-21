class Solution:
    def simplifyPath(self, path: str) -> str:
        pathSpl = path.split('/')
        
        res = []
        i = 0
        while i < len(pathSpl):
            pt = pathSpl[i]
            i += 1
            if not pt or pt == '.':
                continue
            elif pt == '..':
                if res:
                    res.pop(-1)
            else:
                res.append(pt)
            

        res = '/'.join(res)
        if not res:
            return '/'
        return '/' + res