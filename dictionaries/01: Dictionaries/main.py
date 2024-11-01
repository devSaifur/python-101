def get_character_record(name, server, level, rank):
    info = {
        "id": f"{name}#{server}",
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
    }

    return info
