#!/usr/bin/env python3
"""
climbinng leaderboard
"""



from typing import List


def climbingLeaderboard(ranked: List[int], player: List[int]) -> List[int]:
    """Returns the rank"""
    scores = sorted(list(set(ranked)), reverse=True)
    player_ranks = []
    for score in player:
        while scores and score >= scores[-1]:
            scores.pop()
        player_ranks.append(len(scores) + 1)

    return player_ranks

if __name__ == '__main__':
    ranked = [100, 90, 90, 80]
    player = [ 70, 80, 105]
    print(climbingLeaderboard(ranked, player))