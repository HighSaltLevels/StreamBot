import discord

from lib import user_data
from lib import video

HELP_MSG = '```Hello! I am StreamBot. I\'m a helpful little auto-streamer that stores and ' + \
           'streams your favorite youtube videos. Check out these commands below to figure out' + \
           ' how to use me to the fullest :)\n\n!add <name> <url>      - Add a YouTube video ' + \
           'to your list.\n!remove <name>         - Remove a video from your list\n!show      ' + \
           '            - Show all videos in your list\n!play <name> <channel> - Play the ' + \
           'specified video in the specified channel\n\nPlease note that when naming videos to' + \
           ' add, please use a single word, snake_case_with_undescores, or camelCaseLikeThis.' + \
           '\n\nCopywrite HighSaltLevels 2020```'

async def parse_message(client, msg):
    if msg.content.startswith('!add'):
        try:
            _, name, url = msg.content.split(' ')
            return user_data.add_youtube_link(str(msg.author), name, url)
        except ValueError:
            return 'You must add a link by typing ```!add <name> <url>```'

    if msg.content.startswith('!remove'):
        try:
            _, name = msg.content.split(' ')
            return user_data.remove_youtube_link(str(msg.author), name)
        except ValueError:
            return 'You must remove a video by typing ```!remove <name>```'

    if msg.content.startswith('!show'):
        return user_data.get_user_videos(str(msg.author))

    if msg.content.startswith('!play'):
        try:
            _, name, channel = msg.content.split(' ')

            for chan in client.get_all_channels():
                if chan.name == channel:
                    channel_obj = chan
                    break
            else:
                return f'Looks like `{channel}` is not a channel in this server'

            url = user_data.get_user_video_by_name(str(msg.author), name)
            return await video.play_video(client, channel_obj, name, url)

        except ValueError:
            return 'You must play a video by typing ```!play <name> <channel_name>```'
        except KeyError as error:
            return f'Sorry, I don\'t have any video named `{error}` for you in my database'

    if msg.content.startswith('!help'):
        return HELP_MSG

    cmd = msg.content.split(' ')[0]
    return f"I'm sorry, I don't understand {cmd}. Please type `!help` to see a list of commands"
