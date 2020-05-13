import nflgame

import numpy as np1

import matplotlib.pyplot as plt1

%matplotlib inline

abbrev = str(input("Please enter the team's abbreviation code: "))

fballplayer = str(input("Please enter a player: "))

while True:
    try:
        yr = int(input("Please enter a year: "))
        break
    except ValueError:
        print("The year must be expressed as a number.")
        continue

lastpassyds = 0

lasttotyds = 0

seasonpassyds = 0

seasontotyds = 0

avgpassyds = 0

avgtotyds = 0

totpassyds = 0

tottotyds = 0

numgames = 0

yearnum = 0

lastsuccess = 0
GSISID = ""


def gsisizer(player):
    global GSISID
    PlayerList = player.split()
    String1 = PlayerList[0]
    Letter = String1[:1]
    String2 = PlayerList[1]
    GSISID = Letter + "." + String2


def lastgame(player, team, year):
    gsisizer(player)
    global lastpassyds

    global lasttotyds
    global lastsuccess

    weeknum = 17
    lastsuccess = 0

    while weeknum > 0:

        try:

            games = nflgame.games(year, week=weeknum, home=team, away=team)

            gamelist = nflgame.combine(games)
            while True:
                try:
                    lastpassyds = gamelist.name(GSISID).passing_yds
                    break
                except:
                    break
            while True:
                try:
                    lastrushyds = gamelist.name(GSISID).rushing_yds
                    break
                except:
                    lastrushyds = 0
                    break
            while True:
                try:
                    lastreceivingyds = gamelist.name(GSISID).receiving_yds
                    break
                except:
                    lastreceivingyds = 0
                    break
            while True:
                try:
                    lastdefintyds = gamelist.name(GSISID).defense_int_yds
                    break
                except:
                    lastdefintyds = 0
                    break
            while True:
                try:
                    lastpuntretyds = gamelist.name(GSISID).puntret_yds
                    break
                except:
                    lastpuntretyds = 0
                    break
            while True:
                try:
                    lastkickretyds = gamelist.name(GSISID).kickret_yds
                    break
                except:
                    lastkickretyds = 0
                    break
            while True:
                try:
                    lastfumbrecyds = gamelist.name(GSISID).fumbles_rec_yds
                    break
                except:
                    lastfumbrecyds = 0
                    break
            lasttotyds = lastrushyds+lastreceivingyds+lastdefintyds + \
                lastpuntretyds+lastkickretyds+lastfumbrecyds
            if lastpassyds == 0 and lasttotyds == 0:
                raise ValueError
            else:
                lastsuccess = 1

        except:

            weeknum = weeknum - 1

            continue

        break


def averageseason(player, team, year):

    global seasonpassyds

    global seasontotyds

    global avgpassyds

    global avgtotyds

    global numgames
    global yearnum

    games = nflgame.games(year, home=team, away=team)

    numgames = 0

    for i, game in enumerate(games):

        if game.players.name(GSISID):

            numgames = numgames + 1

            continue

    gamelist = nflgame.combine(games)

    while True:
        try:
            seasonpassyds = gamelist.name(GSISID).passing_yds
            break
        except:
            break

    while True:
        try:
            seasonrushyds = gamelist.name(GSISID).rushing_yds
            break
        except:
            seasonrushyds = 0
            break
    while True:
        try:
            seasonreceivingyds = gamelist.name(GSISID).receiving_yds
            break
        except:
            seasonreceivingyds = 0
            break
    while True:
        try:
            seasondefintyds = gamelist.name(GSISID).defense_int_yds
            break
        except:
            seasondefintyds = 0
            break
    while True:
        try:
            seasonpuntretyds = gamelist.name(GSISID).puntret_yds
            break
        except:
            seasonpuntretyds = 0
            break
    while True:
        try:
            seasonkickretyds = gamelist.name(GSISID).kickret_yds
            break
        except:
            seasonkickretyds = 0
            break
    while True:
        try:
            seasonfumbrecyds = gamelist.name(GSISID).fumbles_rec_yds
            break
        except:
            seasonfumbrecyds = 0
            break
    seasontotyds = seasonrushyds+seasonreceivingyds+seasondefintyds + \
        seasonpuntretyds+seasonkickretyds+seasonfumbrecyds

    if numgames != 0:

        avgpassyds = seasonpassyds/numgames

        avgtotyds = seasontotyds/numgames
        yearnum = yearnum + 1



def overallcareer(player, team):
    global totpassyds

    global tottotyds

    global yearnum

    totpassyds = 0

    tottotyds = 0

    yearnum = 0

    for i in range(2000, yr + 1):

        try:

            averageseason(fballplayer, abbrev, i)

            totpassyds = totpassyds + avgpassyds

            tottotyds = tottotyds + avgtotyds
        except:

            continue
    if yearnum != 0:
        totpassyds = totpassyds / yearnum

        tottotyds = tottotyds / yearnum


def interpretpass(player):
    if lastpassyds > avgpassyds > totpassyds:

        print(
            player + "'s passing yard performance in the last game was better than their average in the full season, which was better than their average in their entire career.")

    elif lastpassyds > totpassyds > avgpassyds:

        print(
            player + "'s passing yard performance in the last game was better than their average across their career, which was better than their average across the season.")

    elif avgpassyds > lastpassyds > totpassyds:

        print(
            player + "'s passing yard performance in the last game was worse than their average in the full season, but was better than their average in their entire career.")

    elif avgpassyds > totpassyds > lastpassyds:

        print(
            player + "'s passing yard performance in the last game was worse than their average in their entire career, which was worse than their average this season.")

    elif totpassyds > lastpassyds > avgpassyds:

        print(
            player + "'s passing yard performance in the last game was worse than their average across their career, but was better than their average in this season.")

    elif totpassyds > avgpassyds > lastpassyds:

        print(
            player + "'s passing yard performance in the last game was worse than their average in the full season, which was worse than their average in their entire career.")


def interprettot(player):
    if lasttotyds > avgtotyds > tottotyds:

        print(
            player + "'s all-purpose yard performance in the last game was better than their average in the full game, which was better than their average in their entire career.")

    elif tottotyds > lasttotyds > avgtotyds:

        print(
            player + "'s all-purpose yard performance in the last game was better than their average across their career, which was better than their average across the season.")

    elif avgtotyds > lasttotyds > tottotyds:

        print(
            player + "'s all-purpose yard performance in the last game was worse than their average in the full season, but was better than their average in their entire career.")

    elif avgtotyds > tottotyds > lasttotyds:

        print(
            player + "'s all-purpose yard performance in the last game was worse than their average in their entire career, which was worse than their average this season.")

    elif tottotyds > lasttotyds > avgtotyds:

        print(
            player + "'s all-purpose yard performance in the last game was worse than their average across their career, but was better than their average in this season.")

    elif tottotyds > avgtotyds > lasttotyds:

        print(
            player + "'s all-purpose yard performance in the last game was worse than their average in the full season, which was worse than their average in their entire career.")


def analysis(player, team, year):
    lastgame(player, team, year)
    if lastsuccess == 1:
        averageseason(player, team, year)

        overallcareer(player, team)

        if lastpassyds != 0 or avgpassyds != 0 or seasonpassyds != 0 or totpassyds != 0:
            print("The total amount of passing yards last game for",
                  player, "was: ", lastpassyds)

            print("The average amount of passing yards for", player,
                  "in the", year, "season is:", round(avgpassyds, 2))

            print("The total amount of passing yards for", player,
                  "in the", year, "season is", seasonpassyds)

            print("The total all-time average passing yards for",
                  player, "is:", round(totpassyds, 2))

        if lasttotyds != 0 or avgtotyds != 0 or seasontotyds != 0 or tottotyds != 0:
            print("The total amount of all-purpose yards last game for",
                  player, " was: ", lasttotyds)

            print("The average amount of all-purpose yards for", player,
                  "in the", year, "season is:", round(avgtotyds, 2))

            print("The total amount of all-purpose yards for",
                  player, "in the", year, "season is:", seasontotyds)

            print("The total all-time average all-purpose yards for",
                  player, "is:", round(tottotyds, 2))

        print("The total number of games for", player,
              "in the", year, "season is: ", numgames)

        print("This details the performance of", player, "from the", year -
              yearnum+1, "to the ", year, " season with the team abbreviated:", team)

        if lastpassyds == avgpassyds == totpassyds == 0:

            allpurpgraph()
            interprettot(player)

        elif lasttotyds == avgtotyds == tottotyds == 0:

            passinggraph()
            interpretpass(player)

        else:
            allpurpgraph()
            passinggraph()
            interpretpass(player)

            interprettot(player)
        plt1.show()
    else:
        print("Data error. Try a different year, player, or team.")


def passinggraph():
    PassingYards = [lastpassyds, avgpassyds, totpassyds]

    PassingPeriodAvg = ['Prior Game Avg', 'Season Avg', 'Entire Career Avg']

    xpos1 = np1.arange(len(PassingPeriodAvg))

    xpos1

    plt1.figure(1)

    plt1.bar(xpos1, PassingYards, label="Player Average")

    plt1.xticks(xpos1, PassingPeriodAvg)

    plt1.ylabel("Passing Yards")

    plt1.title('Player Passing Performance')

    plt1.legend()


def allpurpgraph():
    # import numpy as np2

    # import matplotlib.pyplot as plt2

    Yards = [lasttotyds, avgtotyds, tottotyds]

    PeriodAvg = ['Prior Game Avg', 'Season Avg', 'Entire Career Avg']

    xpos2 = np1.arange(len(PeriodAvg))

    xpos2

    plt1.figure(2)

    plt1.bar(xpos2, Yards, label="Player Average")

    plt1.xticks(xpos2, PeriodAvg)

    plt1.ylabel("All-Purpose Yards")

    plt1.title('Player All-Purpose Yard Performance')

    plt1.legend()


analysis(fballplayer, abbrev, yr)

