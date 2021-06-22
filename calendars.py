from bs4 import BeautifulSoup
import requests
import discord


class MainCalendar:
    """Main calendar"""

    def __init__(self, typeOfEvent: str):
        """Creates a main calendar object of given event typeself.

        Args:
            typeOfEvent (str): [ps, lgp, coc, letni_coc, fis_cup]
        """
        self.typeOfEvent = typeOfEvent

    def make_events_list(self):
        sourceCode = requests.get(
            'https://www.skijumping.pl/zawody/' + self.typeOfEvent).text

        # Sparsowana strona skijumping.pl
        parsedSourceCode = BeautifulSoup(sourceCode, 'lxml')

        # Cała tabela kalendarza.
        calendarMain = parsedSourceCode.find(
            'table', class_='competition-calendar-table')

        # Lista zawierająca wiersze tabeli kalendarza, bez nagłówka, wierszy
        # z klasą period i wierszy z samym enterem
        rows = [BeautifulSoup(str(row), 'lxml')
                for row in calendarMain.tbody.children if row != '\n' and
                'period' not in str(row)]

        # Lista eventów (w formie listy słowników, każdy event to słownik)
        events = []
        for row in rows:
            events.append({
                'eventId': row.find('a', target='_blank').get(
                    'href')[8:12],
                'eventDate': row.find('td').text[1:],
                'eventCountry': row.find('img').get('alt'),
                'eventCity': row.find('a').text,
                'eventHill': row.find_all('td')[3].a.text,
                'eventType': row.find_all('td')[4].img.get('alt'),
                'eventUrl': 'https://www.skijumping.pl' +
                row.find('a', target='_blank').get('href')})
        return events


class Message:
    """Build an embed for discord message with calendar"""

    def __init__(self, typeOfCal: str):
        """[Build an embed for discord message with calendar]

        Args:
            typeOfCal (str): [Type of calendar (lgp, ps, coc, fis_cup,
                 letni_coc)]
        """
        self.typeOfCal = typeOfCal

    def add_fields_to_embed(self, data, calendarEmbed):
        """Adds fields to embed

        Args:
            data (list): Variable with currently generated chunk of data
            calendarEmbed (embed): An embed object to which fields will be
            added
        """
        flags = {
            'Polska': ':flag_pl:',
            'Rosja': ':flag_ru:',
            'Finlandia': ':flag_fi:',
            'Niemcy': ':flag_de:',
            'Szwajcaria': ':flag_ch:',
            'Austria': ':flag_au:',
            'Japonia': ':flag_jp:',
            'Norwegia': ':flag_no:',
            'Francja': ':flag_fr:',
            'Słowenia': ':flag_si:',
            'Kazachstan': ':flag_kz:',
            'Rumunia': ':flag_ro:',
            'Chiny': ':flag_cn:',
            'USA': ':flag_us:',
            'Czechy': ':flag_cz:',
            'Estonia': ':flag_ee:',
            'Korea': ':flag_kr:',
            'Szwecja': ':flag_se:'
        }

        for event in range(len(data)):
            try:
                country = flags[data[event]['eventCountry']]
            except KeyError:
                country = data[event]['eventCountry']
            city = data[event]['eventCity']
            date = data[event]['eventDate']
            hill = data[event]['eventHill']
            eventType = str(data[event]['eventType']).replace('konkurs ', '')

            calendarEmbed.add_field(name='Data', value=date, inline=True)
            calendarEmbed.add_field(
                name='Miejsce', value=f"{country} {city} - {hill}",
                inline=True)
            calendarEmbed.add_field(
                name='Rodzaj', value=eventType, inline=True)
        calendarEmbed.set_footer(text='_' * 80)

    def create_message(self):
        """Creates embed list for use in the message

        Returns:
            list: list of embeds to use
        """
        cal = MainCalendar(self.typeOfCal).make_events_list()
        calendarEmbedsList = []
        calendarEmbed = discord.Embed(
            title="Kalendarz " + self.typeOfCal.replace('ps', 'PŚ').replace(
                'letni_coc', 'Letni COC').replace('fis_cup',
                                                  'FIS Cup').upper(),
            colour=Message.barColour)
        chunk = len(cal) // 8
        index1 = 0
        index2 = 8
        for _ in range(chunk):
            data = cal[index1:index2]
            self.add_fields_to_embed(data, calendarEmbed)
            calendarEmbedsList.append(calendarEmbed)
            calendarEmbed = discord.Embed(
                title="cd.", colour=Message.barColour)
            index1 += 8
            index2 += 8

        if len(cal) != 0:
            data = cal[index1:]
            self.add_fields_to_embed(data, calendarEmbed)
            calendarEmbedsList.append(calendarEmbed)

        return calendarEmbedsList
    barColour = 0
