class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # contentMap = {}

        # for pathAndFiles in paths:
        #     pathAndFilesSplit = pathAndFiles.split(" ")
        #     if len(pathAndFilesSplit) == 0:
        #         continue
        #     filePath = pathAndFilesSplit[0]
        #     for idx in range(1, len(pathAndFilesSplit)):
        #         fileAndContent = pathAndFilesSplit[idx]
        #         fileName = ""
        #         content = ""
        #         isContent = False
        #         for char in fileAndContent:
        #             if "(" == char:
        #                 isContent = True
        #             elif ")" == char:
        #                 break
        #             elif isContent:
        #                 content += char
        #             else:
        #                 fileName += char
        #         if content not in contentMap:
        #             contentMap[content] = []
        #         contentMap[content].append(filePath + "/" + fileName)

        # resultFiles = []
        # for files in contentMap.values():
        #     if len(files) > 1:
        #         resultFiles.append(files)
        # return resultFiles

        # A more Elegant Solution
        content_map = {}

        for path_info in paths:
            # Split only once to get directory and files
            directory, *files = path_info.split()

            for file in files:
                # Use more efficient string splitting
                name, content = file.split("(")
                # Remove trailing ')'
                content = content[:-1]

                # Use setdefault to simplify dictionary initialization
                content_map.setdefault(content, []).append(directory + "/" + name)

        # Filter and return in one step
        return [files for files in content_map.values() if len(files) > 1]
