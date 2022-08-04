from discord.ext import commands
from tabulate import tabulate
from datetime import datetime, timedelta
from pytz import timezone
from tabulate import tabulate
import time, re, discord

from discord import (ButtonStyle, Interaction, Member, SelectOption,
                     app_commands)
from discord.ui import Button, Modal, Select, TextInput, View
from utility.utils import defaultEmbed
from utility.paginator import GeneralPaginator
from utility.apps.sekai.music_info import get_group_music, get_song_embed

class SongCog(commands.Cog, name='song'):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
    class SelectOptions(Select):
        def __init__(self):
            options = [SelectOption(label='虛擬歌手', description='バーチャル・シンガー', value=0), 
                    SelectOption(label='25點，Nightcord見。', description='25時、ナイトコードで。', value=1), 
                    SelectOption(label='Leo/need', description='Leo/need', value=2), 
                    SelectOption(label='MORE MORE JUMP！', description='MORE MORE JUMP！', value=3), 
                    SelectOption(label='Vivid BAD SQUAD', description='Vivid BAD SQUAD', value=4), 
                    SelectOption(label='Wonderlands×Showtime', description='ワンダーランズ×ショウタイム', value=5)
                    ]
            super().__init__(placeholder='選擇歌曲分類', options=options)
            
    @app_commands.command(name='songs', description='get songs info')  
  
    async def song(self, interaction: discord.Interaction): 
        embeds = await get_group_music('vocaloid', self.bot.session)
        await interaction.response.send_message(embed=embeds[0])
        '''select = Select(placeholder='選擇歌曲分類', options = [SelectOption(label='虛擬歌手', description='バーチャル・シンガー'), 
                    SelectOption(label='25點，Nightcord見。', description='25時、ナイトコードで。'), 
                    SelectOption(label='Leo/need', description='Leo/need'), 
                    SelectOption(label='MORE MORE JUMP！', description='MORE MORE JUMP！'), 
                    SelectOption(label='Vivid BAD SQUAD', description='Vivid BAD SQUAD'), 
                    SelectOption(label='Wonderlands×Showtime', description='ワンダーランズ×ショウタイム')
                    ])
        async def song_callback(interaction: discord.Interaction):  
            #await i.response.send_message(f'{select.values[0]}')
            if select.values[0] == '虛擬歌手':
                #embed = await get_song_embed(1, self.bot.session)
                embeds = await get_group_music('vocaloid', self.bot.session)
                await interaction.response.send_message(embed=embeds[0])
                #await GeneralPaginator(interaction, embeds).start(embeded=True, follow_up=True)
            elif select.values[0] == '25點，Nightcord見。':
                embeds = await get_group_music('school_refusal', self.bot.session)
                await GeneralPaginator(i, embeds).start(embeded=True)
                await i.response.send_message('success')
            elif select.values[0] == 'Leo/need':
                embeds = await get_group_music('light_music_club', self.bot.session)
                await GeneralPaginator(i, embeds).start(embeded=True)
                await i.response.send_message('success')
            elif select.values[0] == 'MORE MORE JUMP！':
                embeds = await get_group_music('idol', self.bot.session)
                await GeneralPaginator(i, embeds).start(embeded=True) 
                await i.response.send_message('success')
            elif select.values[0] == 'Vivid BAD SQUAD':
                embeds = await get_group_music('street', self.bot.session)
                await GeneralPaginator(i, embeds).start(embeded=True)
                await i.response.send_message('success')
            elif select.values[0] == 'Wonderlands×Showtime':
                embeds = await get_group_music('theme_park', self.bot.session)
                await GeneralPaginator(i, embeds).start(embeded=True)
                await i.response.send_message('success')
        select.callback = song_callback
        view = View()
        view.add_item(select)
        await interaction.response.send_message(view=view) '''
              
        
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SongCog(bot))
