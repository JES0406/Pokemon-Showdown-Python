import math

class PokemonStatsCalculator:
    def calculate_stats(self, base_stats, ivs, evs, level):
        stats = {}
        for stat, base_value in base_stats.items():
            if stat == 'hp':
                stats[stat] = self.calculate_hp(base_value, ivs.get(stat, 0), evs.get(stat, 0), level)
            else:
                stats[stat] = self.calculate_other_stat(base_value, ivs.get(stat, 0), evs.get(stat, 0), level)
        return stats

    def calculate_hp(self, base, iv, ev, level):
        return math.floor(((2 * base + iv + math.floor(ev / 4)) * level) / 100) + level + 10

    def calculate_other_stat(self, base, iv, ev, level):
        return math.floor(((2 * base + iv + math.floor(ev / 4)) * level) / 100) + 5
