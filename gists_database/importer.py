import requests
import sqlite3

def import_gists_to_database(db, username, commit=True):
    url = 'https://api.github.com/users/{}/gists'.format(username)
    resp = requests.get(url)
    resp.raise_for_status()
    gist_data = resp.json()
    for gist in gist_data:
        a_dict = {
            'github_id':gist['id'],
            'html_url':gist['html_url'],
            'git_pull_url':gist['git_pull_url'],
            'git_push_url':gist['git_push_url'],
            'commits_url':gist['commits_url'],
            'forks_url':gist['forks_url'],
            'public':gist['public'],
            'created_at':gist['created_at'],
            'updated_at':gist['updated_at'],
            'comments':gist['comments'],
            'comments_url':gist['comments_url']
            }
        cursor = db.execute("""INSERT INTO gists (github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at,
        updated_at, comments, comments_url)
        values (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public, :created_at, :updated_at, :comments, 
        :comments_url)
        """, a_dict)
        if commit:
            db.commit()