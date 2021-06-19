import discord

helpKalendarz = discord.Embed(
    title="SkokoBot - Komendy", colour=7419530)

helpKalendarz.add_field(
    name="!kalendarz ps", value="Wysyła na priv kalendarz Pucharu Świata",
    inline=True)
helpKalendarz.add_field(
    name="!kalendarz lgp", value="Wysyła na priv kalendarz Letniego Grand \
        Prix", inline=True)
helpKalendarz.add_field(
    name="!kalendarz coc", value="Wysyła na priv kalendarz Pucharu \
        Kontynentalnego", inline=True)
helpKalendarz.add_field(
    name="!kalendarz lcoc", value="Wysyła na priv kalendarz Letniego Pucharu \
        Kontynentalnego", inline=True)
helpKalendarz.add_field(
    name="!kalendarz fs", value="Wysyła na priv kalendarz Fis Cup",
    inline=True)

helpKalendarz.set_footer(text="SkokoBot by SangreSani")
