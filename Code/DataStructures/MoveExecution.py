
from Code.DataStructures.Move import Move
from Code.DataStructures.Pokemon import Pokemon
import random

class MoveExecution:
    def calculate_damage(self, move: Move, attacker: Pokemon, defender: Pokemon, weather: str = None) -> float:
        base_power = 0

        # Handle Status moves
        if move.category == 'Status':
            move.use()  # Apply the effects of the Status move
            return 0  # Status moves typically don't deal damage

        # Get the base power from the move
        try:
            base_power = move.use()  # Ensure move.use() is properly called for the base power
        except ValueError as e:
            print(e)
            return 0  # Return 0 if there's an error

        # Calculate critical hit chance
        ratio = move.critRatio
        bound = max(1, 24//(3^(ratio-1))) # Critical hit ratio, we use the floor division to get the number of times we need to divide 24 by 3 to get the ratio
        roll = random.randint(1, bound)
        crit = roll == 1  # Critical hit on a roll of 1

        if crit:
            print('Critical hit!')

        # Calculate attack and defense based on move category
        if move.category == 'Physical':
            attack = attacker.stats['atk'] * attacker.get_boost('atk')
            defense = defender.stats['def'] if crit else defender.stats['def'] * defender.get_boost('def')
        elif move.category == 'Special':
            attack = attacker.stats['spa'] * attacker.get_boost('spa')
            defense = defender.stats['spd'] if crit else defender.stats['spd'] * defender.get_boost('spd')
        else:
            return 0  # If the move category is invalid, return 0

        # Calculate damage
        damage = (((2 * attacker.level / 5 + 2) * base_power * attack / defense) / 50 + 2)

        if weather != None:
            damage = self.apply_weather_effects(move, damage, weather)
        return damage
    
    def apply_damage(self, move: Move, attacker: Pokemon, defender: Pokemon, damage: float, weather: str) -> int:
        if move.type in attacker.types:
            damage = damage * 1.5
        
        damage *= random.uniform(0.85, 1.0)
        # Type effectiveness (to be implemented)
        damage = self.burned_damage(attacker, move, damage)

        damage = self.apply_weather_effects(move, damage, weather)

        defender.current_hp -= round(damage, 0)
        return round(damage, 0)

    def apply_weather_effects(self, move, damage, weather):
        if weather == 'Rain':
            if move.type == 'Water':
                return damage * 1.5
            elif move.type == 'Fire':
                return damage * 0.5
        elif weather == 'Sun':
            if move.type == 'Fire':
                return damage * 1.5
            elif move.type == 'Water':
                return damage * 0.5
        return damage
    
    def burned_damage(self, attacker: Pokemon, move: Move, damage: float) -> float:
        if move.category == 'Physical' and attacker.status == 'BRN':
            return damage * 0.5
        return damage
