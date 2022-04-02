import praw, sys

actions = 0
version = '1'
useragent = "predditor-" + version  # user agent

# sockpuppet accounts [username, password, api_client_id, api_secret_id]
accounts = [
    ['username1', 'password1', 'api_client_id1', 'api_secret_id1'],
    ['username2', 'password2', 'api_client_id2', 'api_secret_id2'],
    ['username3', 'password3', 'api_client_id3', 'api_secret_id3']
]

targetuser = "target_username"  # the user to vote on
mode = "up"  # [up] or [down] vote
thelimit = None  # how many posts/comments to downvote (for unlimited, set to None)

for account in accounts:
    reddit = praw.Reddit(
        client_id=account[2],
        client_secret=account[3],
        user_agent=useragent,
        username=account[0],
        password=account[1]
    )
    # vote on posts
    for submission in reddit.redditor(targetuser).submissions.new(limit=thelimit):
        actions += 1
        try:
            if mode == 'down':
                submission.downvote()
            elif mode == 'up':
                submission.upvote()
            print("action " + str(actions) + ": " + mode + "voting " + targetuser + "'s post: " + submission.id +
                  " (" + str(submission.score) + ") with " + account[0])
        except:
            print('⚠ there was some problem voting on  ' + submission.id)
    # vote on comments
    for submission in reddit.redditor(targetuser).comments.new(limit=thelimit):
        actions += 1
        try:
            if mode == 'down':
                submission.downvote()
            elif mode == 'up':
                submission.upvote()
            print("action " + str(actions) + ": " + mode + "voting " + targetuser + "'s comment: " + submission.id +
                  " (" + str(submission.score) + ") with " + account[0])
        except:
            print('⚠ there was some problem voting on ' + submission.id)
