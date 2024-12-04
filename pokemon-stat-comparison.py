from mrjob.job import MRJob

class PokemonStatMapping(MRJob):
    pkmnCount = 0
    totalHP = 0
    totalAtt = 0
    totalDef = 0
    totalSAtt = 0
    totalSDef = 0
    totalSpd = 0
    
    ##splits file by line
    def mapper(self, _, line):
        thelist = line.split("/n")
        for x in thelist:
            yield x, 1

    ##reduces data to just id/name and stat values.
    def reducer(self, key, values):
        pokemon = key.split(",")
        pokemonID = pokemon[0] + " - " + pokemon[1]

        lastIndex = len(pokemon) - 1
        pokemonStats = pokemonStats = pokemon[lastIndex-5] + "," + pokemon[lastIndex-4] + "," + pokemon[lastIndex-3] + "," + pokemon[lastIndex-2] + "," + pokemon[lastIndex-1] + "," + pokemon[lastIndex]

        if(pokemon[0] != "No"): ##To ensure header is not counted
            self.pkmnCount += 1
            self.totalHP += int(pokemon[lastIndex-5])
            self.totalAtt += int(pokemon[lastIndex-4])
            self.totalDef += int(pokemon[lastIndex-3])
            self.totalSAtt += int(pokemon[lastIndex-2])
            self.totalSDef += int(pokemon[lastIndex-1])
            self.totalSpd += int(pokemon[lastIndex])
        
        yield pokemonID, pokemonStats
        ##yield key, sum(values)
    print(pkmnCount)
    
    """
    avgHP = totalHP/pkmnCount
    avgAtt = totalAtt/pkmnCount
    avgDef = totalDef/pkmnCount
    avgSAtt = totalSAtt/pkmnCount
    avgSDef = totalSDef/pkmnCount
    avgSpeed = totalSpd/pkmnCount

    print("Average HP: " + str(avgHP))
    print("Average Attack: " + str(avgAtt))
    print("Average Defense: " + str(avgDef))
    print("Average Special Attack: " + str(avgSAtt))
    print("Average Special Defense: " + str(avgSDef))
    print("Average Speed: " + str(avgSpd))
    """

if __name__ == '__main__':
    PokemonStatMapping.run()
