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

helpKalendarz.add_field(
    name="!kiedyskoki ps", value="Wysyła na priv najbliższy konkurs Pucharu \
        Świata", inline=True)
helpKalendarz.add_field(
    name="!kiedyskoki lgp", value="Wysyła na priv najbliższy konkurs Letniego Grand \
        Prix", inline=True)
helpKalendarz.add_field(
    name="!kiedyskoki coc", value="Wysyła na priv najbliższy konkurs Pucharu \
        Kontynentalnego", inline=True)
helpKalendarz.add_field(
    name="!kiedyskoki lcoc", value="Wysyła na priv najbliższy konkurs Pucharu \
        Kontynentalnego", inline=True)
helpKalendarz.add_field(
    name="!kiedyskoki fs", value="Wysyła na priv najbliższy konkurs Fis Cup",
    inline=True)

helpKalendarz.add_field(
    name="!skokobot help", value="Pokazuje to na co właśnie patrzysz.",
    inline=False)

helpKalendarz.set_footer(text="SkokoBot by SangreSani")
