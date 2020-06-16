import praw


def news():
    r = praw.Reddit(user_agent='News Service by /u/keeck')
    submissions = r.get_subreddit('news').get_hot(limit=5)
    print('Top 5 Posts from /r/news')
    print('-' * 25)
    count = 1
    for sub in submissions:
        print(count, '\033[1m' + sub.title)
        print('\033[0m' + sub.url)
        count += 1

news()