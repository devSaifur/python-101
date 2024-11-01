def handle_get_player_record(player_id):
    try:
        result = get_player_record(player_id)
        return result
    except IndexError:
        return "index is too high"
    except Exception as err:
        return err


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
