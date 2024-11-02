class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentMap = {}

        for pathAndFiles in paths:
            pathAndFilesSplit = pathAndFiles.split(" ")
            if len(pathAndFilesSplit) == 0:
                continue
            filePath = pathAndFilesSplit[0]
            for idx in range(1, len(pathAndFilesSplit)):
                fileAndContent = pathAndFilesSplit[idx]
                fileName = ""
                content = ""
                isContent = False
                for char in fileAndContent:
                    if "(" == char:
                        isContent = True
                    elif ")" == char:
                        break
                    elif isContent:
                        content += char
                    else:
                        fileName += char
                if content not in contentMap:
                    contentMap[content] = []
                contentMap[content].append(filePath + "/" + fileName)

        resultFiles = []
        for files in contentMap.values():
            if len(files) > 1:
                resultFiles.append(files)
        return resultFiles
