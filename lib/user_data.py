import os
import json
from threading import Lock

DATA_FILE = 'data/links_and_users.json'
FILE_LOCK = Lock()

if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
    with open(DATA_FILE, 'w') as fwrite:
        fwrite.write('{}')

def _load_user_data():
    FILE_LOCK.acquire()
    with open(DATA_FILE) as fread:
        data = fread.read()

    FILE_LOCK.release()
    return json.loads(data)

def _write_user_data(data):
    FILE_LOCK.acquire()
    with open(DATA_FILE, 'w') as fwrite:
        fwrite.write(json.dumps(data))
    FILE_LOCK.release()

def add_youtube_link(author, name, url):
    user_data_dict = _load_user_data()
    user = author.split('#')[0]
    if author not in user_data_dict:
        user_data_dict[author] = {}

    user_data_dict[author][name] = url
    _write_user_data(user_data_dict)
    return f'Alright {author}. I\'ve added {name} to your list of videos.'

def remove_youtube_link(author, name):
    user_data_dict = _load_user_data()
    user = str(author).split('#')[0]
    try:
        del user_data_dict[author][name]
        _write_user_data(user_data_dict)
        return f'Ok {user}. I have removed `{name}` from your list of videos'
    except KeyError:
        return f'Sorry {user}. I don\'t have any videos that you named `{name}` in my database :('

def get_user_videos(author):
    user_data_dict = _load_user_data()
    msg = 'Here\'s what I have for you:\n```'
    for name in user_data_dict[author]:
        msg += f'{name} -> {user_data_dict[author][name]}\n'
    return msg + '```'
        
