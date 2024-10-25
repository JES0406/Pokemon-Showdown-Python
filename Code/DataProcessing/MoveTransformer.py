class MoveTransformer:
    def transform(self, move_info: dict) -> dict:
        """
        Transform the raw move data into a more structured dictionary format.
        :param move_info: Raw move data as a dictionary
        :return: Transformed move data as a dictionary
        """
        if not isinstance(move_info, dict):
            print(f"Error: Expected a dictionary but got {type(move_info)}")
            return None

        # Start transforming the move dictionary
        transformed_move = {
            "num": move_info.get("num", None),
            "name": move_info.get("name", None),
            "type": move_info.get("type", None),
            "category": move_info.get("category", None),
            "pp": move_info.get("pp", None),
            "basePower": move_info.get("basePower", None),
            "accuracy": move_info.get("accuracy", None),
            "priority": move_info.get("priority", None),
            "flags": {},
            'desc': move_info.get('desc', None),
            'shortDesc': move_info.get('shortDesc', None),
            'overrideDefensiveStat': move_info.get('overrideDefensiveStat', None),
        }

        # Apply the transformation helper methods
        transformed_move = self.handle_flags(transformed_move, move_info)
        transformed_move = self.handle_additional_effects(transformed_move, move_info)
        transformed_move = self.handle_target(transformed_move, move_info)
        transformed_move = self.handle_z_max_moves(transformed_move, move_info)
        transformed_move = self.handle_optional_effects(transformed_move, move_info)

        return transformed_move

    def handle_flags(self, transformed_move: dict, move_info: dict) -> dict:
        """
        Handle flags for the move.
        :param transformed_move: Transformed move data (dictionary).
        :param move_info: Raw move data (dictionary).
        :return: Transformed move data with flags included.
        """
        for flag in ['protect', 'mirror', 'contact', 'bullet', 'sound', 'heal', 'recharge', 'distance', 'snatch', 'metronome']:
            if flag in move_info.get("flags", {}):
                transformed_move["flags"][flag] = move_info["flags"].get(flag, False)
        flags_map = {
            "Shell Side Arm": "ShellSideArm",
            "Psyshock": "Psyshock", "Psystrike": "Psyshock", "Secret Sword": "Psyshock",
            "Photon Geyser": "PhotonGeyser",
            "Tera Blast": "TeraBlast",
            "Tera Storm": "TeraStorm",
            "Super Fang": "SuperFang",
            "Freeze-Dry": "FreezeDry"
        }

        move_name = move_info.get("name")
        if move_name in flags_map:
            transformed_move["flags"][flags_map[move_name]] = True

        transformed_move["flags"]["ignoreImmunity"] = move_info.get("ignoreImmunity", False)

        return transformed_move

    def handle_additional_effects(self, transformed_move: dict, move_info: dict) -> dict:
        """
        Handle additional effects for the move.
        :param transformed_move: Transformed move data (dictionary).
        :param move_info: Raw move data (dictionary).
        :return: Transformed move data with additional effects included.
        """
        if move_info.get("secondary") is not None:
            transformed_move["secondary"] = {
                "chance": move_info["secondary"].get("chance", None),
                "status": move_info["secondary"].get("status", None),
                "boosts": move_info["secondary"].get("boosts", None)
            }
        else:
            transformed_move["secondary"] = None
        return transformed_move

    def handle_target(self, transformed_move: dict, move_info: dict) -> dict:
        """
        Handle target of the move.
        :param transformed_move: Transformed move data (dictionary).
        :param move_info: Raw move data (dictionary).
        :return: Transformed move data with target information included.
        """
        transformed_move["target"] = move_info.get("target", None)
        return transformed_move

    def handle_z_max_moves(self, transformed_move: dict, move_info: dict) -> dict:
        """
        Handle Z-Move and Max Move specifics.
        :param transformed_move: Transformed move data (dictionary).
        :param move_info: Raw move data (dictionary).
        :return: Transformed move data with Z-Move and Max Move specifics included.
        """
        if "zMove" in move_info:
            transformed_move["zMove"] = {
                "boost": move_info["zMove"].get("boost", None),
                "effect": move_info["zMove"].get("effect", None),
                "basePower": move_info["zMove"].get("basePower", None)
            }

        if "maxMove" in move_info:
            transformed_move["maxMove"] = {
                "basePower": move_info["maxMove"].get("basePower", None)
            }

        return transformed_move

    def handle_optional_effects(self, transformed_move: dict, move_info: dict) -> dict:
        """
        Handle optional effects like recoil, heal, crit ratio, etc.
        :param transformed_move: Transformed move data (dictionary).
        :param move_info: Raw move data (dictionary).
        :return: Transformed move data with optional effects included.
        """
        optional_effects = ['recoil', 'heal', 'critRatio', 'drain', 'forceSwitch', 'selfBoost', 'weather']
        for effect in optional_effects:
            if effect in move_info:
                transformed_move[effect] = move_info.get(effect, None)
        return transformed_move
