from mrjob.job import MRJob

class PokemonStatMapping(MRJob):

    ##key = ","
    def mapper(self, _, line):
        thelist = line.split("/n")
        for x in thelist:
            ##Split items into array
            ##pokemon = x.split(",")
            ##yield pokemon[1], pokemon[4]
            yield x, 1

    def reducer(self, key, values):
        pokemon = key.split(",")
        pokemonID = pokemon[0] + " - " + pokemon[1]

        lastIndex = len(pokemon) - 1
        pokemonStats = pokemonStats = pokemon[lastIndex-5] + "," + pokemon[lastIndex-4] + "," + pokemon[lastIndex-3] + "," + pokemon[lastIndex-2] + "," + pokemon[lastIndex-1] + "," + pokemon[lastIndex]

        
        """
        if(pokemon[4].isdigit()):
            checkPKMN4 = int(pokemon[4])
            pokemonStats = pokemon[4] + "," + pokemon[5] + "," + pokemon[6] + "," + pokemon[7] + "," + pokemon[8] + "," + pokemon[9]
        else:
            pokemonStats = pokemon[5] + "," + pokemon[6] + "," + pokemon[7] + "," + pokemon[8] + "," + pokemon[9] + "," + pokemon[10]
        """

        
        yield pokemonID, pokemonStats
        ##yield key, sum(values)

if __name__ == '__main__':
    PokemonStatMapping.run()
