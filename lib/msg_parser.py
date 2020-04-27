from lib import user_data

HELP_MSG = '```Hello! I am StreamBot. I\'m a helpful little auto-streamer that stores and ' + \
           'streams your favorite youtube videos. Check out these commands below to figure out' + \
           ' how to use me to the fullest :)\n\n!add <name> <url>      - Add a YouTube video ' + \
           'to your list.\n!delete <name>         - Remove a video from your list\n!show      ' + \
           '            - Show all videos in your list\n!play <name> <channel> - Play the ' + \
           'specified video in the specified channel\n\nPlease note that when naming videos to' + \
           ' add, please use a single word, snake_case_with_undescores, or camelCaseLikeThis.' + \
           '\n\nCopywrite HighSaltLevels 2020```'

def parse_message(client, msg):
    if msg.content.startswith('!add'):
        try:
            _, name, url = msg.content.split(' ')
            return user_data.add_youtube_link(str(msg.author), name, url)
        except ValueError:
            return 'You must add a link by typing ```!add <name> <url>```'

    if msg.content.startswith('!delete'):
        try:
            _, name = msg.content.split(' ')
            return user_data.remove_youtube_link(str(msg.author), name)
        except ValueError:
            return 'You must delete a video by typing ```!delete <name>```'

    if msg.content.startswith('!show'):
        return user_data.get_user_videos(str(msg.author))

    if msg.content.startswith('!play'):
        return 'Not implemented yet'

    if msg.content.startswith('!help'):
        return HELP_MSG

    cmd = msg.content.split(' ')[0]
    return f"I'm sorry, I don't understand {cmd}. Please type `!help` to see a list of commands"
