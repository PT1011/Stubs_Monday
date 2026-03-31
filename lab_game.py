import random


def get_random_item(player_name, rng=None):
    if rng is None:
        rng = random
    item = rng.choice(["sword", "shield", "potion"])
    return f"{player_name} found a {item}"


def award_badge(player_name, badge_name, logger):
    logger.log(f"{player_name} earned {badge_name}")
    return None
