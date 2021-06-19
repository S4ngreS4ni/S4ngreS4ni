import calendars
import datetime
import globals
import requests
from bs4 import BeautifulSoup
import discord


class Closest_competition:
    """Closest competition class"""

    def __init__(self, eventsList):
        """Class with the closest competitionself.

        Args:
            eventsList (list): List of competitions.
        """
        self.eventsList = eventsList

    def create_list_of_dates(self):
        """Creates a list of dates of given eventself.

        Returns:
            list: List of dates.
        """
        datesList = [datetime.datetime.strptime(
            self.eventsList[i]['eventDate'], '%d-%m-%Y') for i in
            range(len(self.eventsList))]  # lista dat w odpowiednim formacie
        return datesList

    def fetch_event_url(self):
        """Fetches URL of the closest competitionself.

        Returns:
            str: URL
        """
        for elem in range(len(self.eventsList)):
            if self.eventsList[elem]['eventDate'] == \
                    self.pick_closest_date():
                eventUrl = self.eventsList[elem]['eventUrl']
        return eventUrl

    def pick_closest_date(self):
        """Show nearest competition date (to today)self.

        Returns:
            str: Nearest competition date.
        """
        return min(self.create_list_of_dates()).strftime('%d-%m-%Y')


class Competition_info(Closest_competition):
    """class of competition info"""

    def __init__(self):
        """Closest competition further info from skijumping.pl

        Args:
            eventUrl ([str], optional): [closest competition URL]. Defaults to
                eventUrl.
        """
        super().__init__(calendars.MainCalendar(globals.compType)
                         .make_events_list())
        self.eventUrl = super().fetch_event_url()

    def parse(self):
        """Parses the code from eventUrl

        Returns:
            BeautifulSoup: Parsed source code from eventUrl
        """
        sourceCode = requests.get(self.eventUrl).text
        sourceCodeParsed = BeautifulSoup(
            sourceCode, 'lxml')
        return sourceCodeParsed

    def show_main_comp_info(self):
        """Creates main info about competition in a dictionary form

        Returns:
            dict: dictionary with competition info
        """
        infoBox = self.parse().find(class_='info')

        compInfo = {
            'eventType': infoBox.div.get_text(),
            'hill': infoBox.span.get_text(),
            'country': infoBox.img['title'],
            'date': infoBox.select("div div:nth-of-type(7)")[0].get_text()
        }
        return compInfo

    def show_comp_program(self):
        """Shows program of closest competition.

        Returns:
            list: List containing competition program.
        """
        programBox = self.parse().find(
            id='competition_program').get_text()
        compProgram = []
        for item in programBox.replace('\r', '').split('\n'):
            if item != '':
                compProgram.append(item)
        return compProgram

    def show_tv_schedule(self):
        tvChannels = self.parse().find(id='competition_tv')
        compTvChannel = []
        for item in tvChannels.find_all('img'):
            compTvChannel.append(item['title'])

        tvProgram = self.parse().find(id='competition_tv').div.get_text()
        tvProgram = ' '.join(tvProgram.split())
        compTvInfo = []
        for line in tvProgram.split(' LIVE'):
            if line != '':
                compTvInfo.append(line)

        tvSchedule = []
        for i in range(len(compTvChannel)):
            tvSchedule.append(str(compTvChannel[i] + ': ' + compTvInfo[i]))
        return tvSchedule

    def count_days_to_next_comp(self):
        """Tells how many days it is to the next competitionself.

        Returns:
            int: Number of days to next competition.
        """
        nextCompDate = datetime.datetime.strptime(
            super().pick_closest_date(), '%d-%m-%Y').date()
        todaysDate = datetime.datetime.today().date()
        daysToNextComp = nextCompDate - todaysDate
        return str(daysToNextComp.days)


def create_message():
    nextComp = Competition_info()
    message = discord.Embed(title="Kiedy kolejne skoki?",
                            description="Kolejne skoki " +
                            globals.compType.replace('ps', 'PŚ').upper(
                            ) + " odbędą się za " +
                            nextComp.count_days_to_next_comp() + " dni (" +
                            nextComp.show_main_comp_info()['date'] +
                            ").")

    message.add_field(name="Impreza", value=nextComp.show_main_comp_info()[
        'eventType'], inline=True)
    message.add_field(name="Kraj", value=nextComp.show_main_comp_info()[
        'country'], inline=True)
    message.add_field(name="Skocznia", value=nextComp.show_main_comp_info()
                      ['hill'], inline=True)

    program = ''
    for item in nextComp.show_comp_program():
        if item[0].isalpha() is True:
            item = "**" + item + "**"
        program += item + "\n"
    if program == '* wszystkie godziny według czasu polskiego\n':
        program = 'Brak ustalonego programu.'

    message.add_field(name="Program zawodów: ",
                      value=program, inline=False)

    tv = ''
    for item in nextComp.show_tv_schedule():
        tv += item + '\n'
    if len(tv) == 0:
        tv = 'Brak transmisji.'

    message.add_field(name="Transmisje: ", value=tv, inline=False)

    message.set_thumbnail(url='https://i.imgur.com/feY33rK.png')

    return message
