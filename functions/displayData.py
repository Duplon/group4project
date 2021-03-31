from functions import getKillsDeaths, gameModeStatsDict, getRatio
from functions.main import *


def displayData(allPlayerData, selectedGame, gamemodeStats):
    guide = Application
    kills = getKillsDeaths.getKills(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
    deaths = getKillsDeaths.getDeaths(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)
    guide.textBox1.delete('1.0', 'END')
    for counter in gamemodeStats[selectedGame]:
        try:
            print(counter.capitalize() + " " + str(allPlayerData['player']['stats'][selectedGame][counter]))
            guide.textBox1.insert('END', f"{counter.capitalize()}: {str(allPlayerData['player']['stats'][selectedGame][counter])}")
        except:
            print(counter.capitalize() + " " + "0")
            guide.textBox1.insert('END', 'No stats available.')
    print(getRatio.ratio(kills, deaths))
