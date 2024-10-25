
from Code.DataStructures.Move import Move
from Code.DataStructures.Pokemon import Pokemon
from Code.exceptions import NoPPException
from Code.constants import type_advantages
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
        except NoPPException as e:
            print(e)
            return 0  # Return 0 if there's an error

        # Calculate critical hit chance
        crit = self.crit_logic(move.critRatio)

        # Calculate attack and defense based on move category
        if move.flags.get('ShellSideArm') == True:
           damage = self.shell_side_arm(attacker, defender, base_power, crit, move)
        # The problem is that Photon geyser and Tera storm depend on the boost of the pokemon
        if move.flags.get('PhotonGeyser') == True or move.flags.get('TeraStorm') == True and attacker.terastilized == True:
            damage = self.photon_geyser(attacker, defender, base_power, crit, weather)
        elif move.flags.get('Psyshock') == True:
            damage = self.psyshock(attacker, defender, base_power, crit)
        else:
            damage = self.damage_formula(attacker, defender, base_power, crit, move.category)

        return damage
    
    def crit_logic(self, ratio: int) -> bool:
        bound = max(1, 24//(3^(ratio-1))) # Critical hit ratio, we use the floor division to get the number of times we need to divide 24 by 3 to get the ratio
        roll = random.randint(1, bound)
        crit = roll == 1  # Critical hit on a roll of 1

        if crit:
            print('Critical hit!')
        return crit
    
    def apply_damage(self, move: Move, attacker: Pokemon, defender: Pokemon, weather: str) -> int:
        if move.flags.get('SuperFang') != True:
            damage = self.calculate_damage(move, attacker, defender, weather)
            if move.type in attacker.types: # STAB bonus
                damage = damage * 1.5
            
            damage *= random.uniform(0.85, 1.0) # Random damage modifier between 0.85 and 1.0
            damage *= self.type_effectiveness(move, defender) # Type effectiveness
            damage = self.burned_damage(attacker, move, damage) # If the attacker is burned, reduce damage by half
            damage = self.apply_weather_effects(move, damage, weather) # Apply weather effects
        
        else:
            damage = defender.current_hp / 2

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

    def damage_formula(self, attacker: Pokemon, defender: Pokemon, base_power: int, crit: bool, category: str) ->float:
        attack, defense = self.attack_defense_calculation(attacker, defender, crit, category)
        damage = (((2 * attacker.level / 5 + 2) * base_power * attack / defense) / 50 + 2)
        return damage

    def attack_defense_calculation(self, attacker: Pokemon, defender: Pokemon, crit: bool, category: str) -> tuple:
        stat, def_stat = ('atk', 'def') if category == 'Physical' else ('spa', 'spd')

        attack = attacker.stats[stat] * attacker.get_boost(stat)
        defense = defender.stats[def_stat] if crit else defender.stats[def_stat] * defender.get_boost(def_stat)

        return attack, defense

    
    def shell_side_arm(self, attacker: Pokemon, defender: Pokemon, base_power: int, crit: bool, move: Move):
        special_damage = self.damage_formula(attacker, defender, base_power, crit, 'Special')
        physical_damage = self.damage_formula(attacker, defender, base_power, crit, 'Physical')
        if physical_damage > special_damage:
            damage = physical_damage
            move.contact = True
        else:
            damage = special_damage
            move.contact = False

        return damage
    
    def photon_geyser(self, attacker: Pokemon, defender: Pokemon, base_power: int, crit: bool):
        if attacker.stats['atk'] > attacker.stats['spa']:
            return self.damage_formula(attacker, defender, base_power, crit, 'Physical')
        else:
            return self.damage_formula(attacker, defender, base_power, crit, 'Special')
        
    def psyshock(self, attacker: Pokemon, defender: Pokemon, base_power: int, crit: bool):
        return self.damage_formula(attacker, defender, base_power, crit, 'Special')
    
    def type_effectiveness(self, move: Move, defender: Pokemon):
        effectiveness = 1
        for type_ in defender.types:
            if move.flags.get('freezedry') == True and type_ == 'Water':
                effectiveness *= 2
            else:
                if move.flags.get('ignoreImmunity') != True:
                    effectiveness *= type_advantages[move.type].get(type_, 1)
                elif move.flags.get('ignoreImmunity') == True and type_advantages[move.type].get(type_, 1) == 0:
                    effectiveness *= 1
                elif type_ == 'Flying' and move.type == 'Ground' and defender.grounded == True:
                    effectiveness *= 1
                else:
                    effectiveness *= type_advantages[move.type].get(type_, 1)
        return effectiveness