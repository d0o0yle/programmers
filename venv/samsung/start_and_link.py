from itertools import combinations

def compute_score(team, scoreBoard):
    teamScore = 0
    for aPlayer in team:
        for bPlayer in team:
            teamScore += scoreBoard[aPlayer][bPlayer]

    return teamScore

def solution():
    N = int(input())
    scoreBoard = [[int(x) for x in input().split()] for _ in range(N)]

    teamList = list(combinations(range(N), N // 2))

    answers = []

    for team in teamList[:len(teamList)//2]:
        teamScore = compute_score(team, scoreBoard)
        otherTeam = set(range(N)) - set(team)
        otherTeamScore = compute_score(otherTeam, scoreBoard)
        answers.append(abs(teamScore-otherTeamScore))
    return min(answers)

if __name__ == '__main__':
    print(solution())