from mrjob.job import MRJob

class PokemonStatAggregation(MRJob):

    def mapper(self, _, line):

        # Example line: "0001 - Bulbasaur - grass/poison" "45,49,49,65,65,45,318"
        key, value = line.split("\t")

        # remove surrounding quotations from keys and values
        key = key.strip('\"')
        value = value.strip('\"')
        
        # get gen based on pokedex number

        pokemon_id = key.split(" - ")[0]
        pokedex = int(pokemon_id)
        
        if 1 <= pokedex <= 151:
            gen = 1
        elif 152 <= pokedex <= 251:
            gen = 2
        elif 252 <= pokedex <= 386:
            gen = 3
        elif 387 <= pokedex <= 493:
            gen = 4
        elif 494 <= pokedex <= 649:
            gen = 5
        elif 650 <= pokedex <= 721:
            gen = 6
        elif 722 <= pokedex <= 809:
            gen = 7
        elif 810 <= pokedex <= 898:
            gen = 8
        else:
            return
        
        # Get stats from the value (format: "45,49,49,65,65,45,318")
        stats = list(map(int, value.split(",")))
        
        yield gen, stats

    def reducer(self, key, values):

        totalHp = totalAtt = totalDef = totalSatt = totalSdef = totalSpd = totalStatTotal = 0
        count = 0
        
        # aggregate stats for each generation
        for stats in values:
            totalHp += stats[0]
            totalAtt += stats[1]
            totalDef += stats[2]
            totalSatt += stats[3]
            totalSdef += stats[4]
            totalSpd += stats[5]
            totalStatTotal += stats[6]
            count += 1

        # calculate the averages
        avgHp = totalHp / count
        avgAtt = totalAtt / count
        avgDef = totalDef / count
        avgSatt = totalSatt / count
        avgSdef = totalSdef / count
        avgSpd = totalSpd / count
        avgStatTotal = totalStatTotal / count

        # yield the generation and average stats
        yield key, [avgHp, avgAtt, avgDef, avgSatt, avgSdef, avgSpd, avgStatTotal]

if __name__ == '__main__':
    output = PokemonStatAggregation.run()
