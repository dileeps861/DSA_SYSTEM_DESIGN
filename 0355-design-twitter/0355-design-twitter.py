class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        userTweets = self.tweets[userId]
        self.timestamp += 1 
        userTweets.append([self.timestamp, tweetId])
        if len(userTweets) > 10:
            userTweets.pop(0)
        self.tweets[userId] = userTweets

    def getNewsFeed(self, userId: int) -> List[int]:
        userTweets = self.tweets[userId][:] if userId in self.tweets else []
        for followee in self.followers[userId]:
            for tweets in self.tweets[followee]:
                heappush(userTweets, tweets)
                if len(userTweets) > 10:
                    heappop(userTweets)
        if not userTweets:
            return []
        news_feed = []
        while userTweets:
            news_feed.append(heapq.heappop(userTweets)[1])
        return news_feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)