import discord
from goat import new_search, search
import traceback

TOKEN = ''
CHANNEL_ID = ''

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != CHANNEL_ID:
        return

    if message.content.split(' ')[0] == '!goat':
        try:
            # Use old API - has more info
            item = message.content.replace('!goat ', '')
            product = search(item)

            embed = discord.Embed(
                title=product['name'],
                url='https://www.goat.com/sneakers/'+product['slug'],
            )
            embed.set_thumbnail(url=product['main_picture_url'])
            embed.add_field(
                name='Colour',
                value=product['details']
            )
            embed.add_field(
                name='Style ID',
                value=product['sku']
            )
            embed.add_field(
                name='Lowest Price ($)',
                value=str(int(product['lowest_price_cents'])/100)
            )
            embed.add_field(
                name='Highest Offer ($)',
                value=str(int(product['maximum_offer_cents'])/100)
            )
            embed.add_field(
                name='Lowest Offer ($)',
                value=str(int(product['minimum_offer_cents'])/100)
            )
            embed.add_field(
                name='Want Count',
                value=product['want_count']
            )
            embed.add_field(
                name='Three-day Rolling Want Count',
                value=product['three_day_rolling_want_count']
            )
            await message.channel.send(embed=embed)

        except IndexError:
            # Use new API - has less info
            item = message.content.replace('!goat ', '')
            product = new_search(item)

            embed = discord.Embed(
                title=product['value'],
                url='https://www.goat.com/sneakers/'+product['data']['slug'],
            )
            embed.set_thumbnail(url=product['data']['image_url'])
            embed.add_field(
                name='Colour',
                value=product['data']['color']
            )
            embed.add_field(
                name='Style ID',
                value=product['data']['sku']
            )
            embed.add_field(
                name='Lowest Price ($)',
                value=str(int(product['data']['lowest_price_cents'])/100)
            )
            embed.add_field(
                name='Retail Price ($)',
                value=str(int(product['data']['retail_price_cents'])/100)
            )
            await message.channel.send(embed=embed)
        
        except:
            print(traceback.format_exc())
            response = 'An error occurred with your request.'
            await message.channel.send(response)


client.run(TOKEN)