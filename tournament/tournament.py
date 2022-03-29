import dataclasses
import operator

POINTS_PER_WIN = 3
POINTS_PER_DRAW = 1

HEADER = "Team                           | MP |  W |  D |  L |  P"


@dataclasses.dataclass
class TeamTally:
    name: str
    win: int = 0
    loss: int = 0
    draw: int = 0

    @property
    def matches_played(self):
        return self.win + self.loss + self.draw

    @property
    def points(self):
        return self.win * POINTS_PER_WIN + self.draw * POINTS_PER_DRAW


def tally(rows):
    team_map: dict[str, TeamTally] = {}

    def get_team(name):
        if team := team_map.get(name):
            return team

        team = team_map[name] = TeamTally(name=name)
        return team

    for row in rows:
        team_name_a, team_name_b, result = row.split(";")
        team_a = get_team(team_name_a)
        team_b = get_team(team_name_b)

        if result == "win":
            team_a.win += 1
            team_b.loss += 1
        elif result == "loss":
            team_b.win += 1
            team_a.loss += 1
        elif result == "draw":
            team_b.draw += 1
            team_a.draw += 1

    return [HEADER] + [
        f"{team.name:31}|{team.matches_played:3} |{team.win:3} |{team.draw:3} |{team.loss:3} |{team.points:3}"
        for team in sorted(
            sorted(team_map.values(), key=operator.attrgetter("name")),
            key=operator.attrgetter("points"),
            reverse=True,
        )
    ]
