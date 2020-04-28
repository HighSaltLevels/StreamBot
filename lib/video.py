import discord

async def play_video(client, channel, name, url):
    print(f'Channel = {channel}')
    voice = await client.join_voice_channel(channel)
    player = await voice.create_ytdl_player(url)
    player.start()
    return f'OK. I\'ve started playing {name} in {channel} '
