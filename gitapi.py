from pygithub3 import Github
import requests
import json

gh = Github(login='username', password='password')

copitux = gh.events
# print dir(copitux)
# kennethreitz = gh.users.get('kennethreitz')

# copitux_repos = gh.repos.list().all()
# kennethreitz_repos = gh.repos.list('kennethreitz').all()
_url = 'https://api.github.com/repos/Sanjay015/Name-Entity-Recognition'

commit_activity = '/stats/commit_activity'
contributors_activity = '/stats/contributors'
participants = '/stats/participation'
# Get the number of commits per hour in each day
daily_report = '/stats/punch_card'
"""
Each array contains the day number, hour number, and number of commits:
0-6: Sunday - Saturday
0-23: Hour of day
Number of commits
For example, [2, 14, 25] indicates that there were 25 total commits,
during the 2:00pm hour on Tuesdays. All times are based on the time zone
of individual commits.
"""
r = requests.get(_url + commit_activity)

if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print repoItem
