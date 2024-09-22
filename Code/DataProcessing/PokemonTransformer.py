class PokemonTransformer:
    @staticmethod
    def transform(data: dict) -> dict:
        return {
            'type': data.get('types'),
            'stats': data.get('baseStats'),
            'height': data.get('heightm'),
            'weight': data.get('weightkg'),
            'otherFormes': data.get('otherFormes'),
            'tier': data.get('tier'),
            'gender': data.get('gender')
        }
