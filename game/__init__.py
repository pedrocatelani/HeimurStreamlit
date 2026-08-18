class Game:
    status = {
        "max_hp": 11,
        "current_hp": 11,
        "max_mana": 9,
        "current_mana": 9,
        "max_stance": 5,
        "current_stance": 5,
        "base_attack": 0,
        "base_defense": 0,
        "crit_chance": 5,
        "crit_mult": 1.5,
        "elemental_strike": 1.4,
        "craft_discount": 0,
        "harvest_bonus": 0,
        "damage_resistance": 0,
    }
    atr = {
        "strenght": 3,
        "intelligence": 3,
        "dexterity": 3,
        "constitution": 3,
        "charisma": 3,
    }
    specs = {"name": "string", "char_class": "ranger", "char_alignment": "sun-born"}
    day_info = {
        "current_week_day": "Primus",
        "current_cicle": 1,
        "current_dungeon": "None",
        "current_period": "eevening",
    }
    events = ["Marshall", "Lyra"]
    inspect_event = "Marshall"
    relationships = [{"Marshall": 2}, {"Lyra": 1}]

    creation = ("2026-01-18 [14:01]",)

    def relationships_list(self):
        relations = []
        for r in self.relationships:
            relations.append(list(r.keys())[0])

        return relations


running_game = Game()
