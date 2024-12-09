from mrjob.job import MRJob

## Produce a condensed list of unique pokemon until gen 8 and their stats 
class PokemonStatMapping(MRJob):

    ##splits file by line
    def mapper(self, _, line):
        thelist = line.split("/n")
        for x in thelist:
            yield x, 1

    ##reduces data to just id/name and stat values.
    def reducer(self, key, values):
        pokemon = key.split(",")
        pokemonID = pokemon[0] + " - " + pokemon[1] + " - " + pokemon[2]
        statTotal = 0
        lastIndex = len(pokemon) - 1

        # use a for loop to sum all stats of each pokemon
        for i in range(6):
            try:
                statTotal += int(pokemon[lastIndex - i])
            except ValueError:
                pass

        pokemonStats = pokemon[lastIndex-5] + "," + pokemon[lastIndex-4] + "," + pokemon[lastIndex-3] + "," + pokemon[lastIndex-2] + "," + pokemon[lastIndex-1] + "," + pokemon[lastIndex] + "," + str(statTotal)
        
        if pokemonID[0] == '0':
            yield pokemonID, pokemonStats
        else:
            pass


if __name__ == '__main__':
    PokemonStatMapping.run()
