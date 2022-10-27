import discord
from discord import app_commands
from discord.ext import commands

from utility.utils import updateEmbed, is_ayaakaa, notAyaakaaEmbed

class OthersCog(commands.Cog, name='others'):
    
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='embed', description='embed')
    @app_commands.rename(
        description='embed-description', \
        cmd_1='cmd-1-name', cmd_1_des_ln_1='cmd-1-description', cmd_1_des_ln_2='cmd-1-description2', \
        cmd_2='cmd-2-name', cmd_2_des_ln_1='cmd-2-description', cmd_2_des_ln_2='cmd-2-description2', \
        cmd_3='cmd-3-name', cmd_3_des_ln_1='cmd-3-description', cmd_3_des_ln_2='cmd-3-description2'
        )
    async def update(self, interaction: discord.Interaction, description: str, \
        cmd_1: str = '', cmd_1_des_ln_1: str = '', cmd_1_des_ln_2: str = '', \
        cmd_2: str = '', cmd_2_des_ln_1: str = '', cmd_2_des_ln_2: str = '', \
        cmd_3: str = '', cmd_3_des_ln_1: str = '', cmd_3_des_ln_2: str = ''):
        is_ayaakaa_ = await is_ayaakaa(interaction)
        if is_ayaakaa_ == True:
            embed = updateEmbed(description=description)
            if len(cmd_1) >= 1:
                embed.add_field(name=cmd_1, value=f'{cmd_1_des_ln_1}\n{cmd_1_des_ln_2}', inline=False)
            if len(cmd_2) >= 1:
                embed.add_field(name=cmd_2, value=f'{cmd_2_des_ln_1}\n{cmd_2_des_ln_2}', inline=False)
            if len(cmd_3) >= 1:
                embed.add_field(name=cmd_3, value=f'{cmd_3_des_ln_1}\n{cmd_3_des_ln_2}', inline=False)
            await interaction.response.send_message(embed=embed)
        else:
            embed = notAyaakaaEmbed()
            await interaction.response.send_message(embed=embed, ephemeral= True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OthersCog(bot))
    
    