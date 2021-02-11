from typing import List
from team.models import Team


class TeamController:
    def create(self, name: str, description: str) -> Team:
        team = Team(name=name, description=description)
        team.save()
        return team

    def update(self, id_: int, name: str, description: str) -> Team:
        team = self.get_by_id(id_)
        team.name = name
        team.description = description
        team.save()
        return team

    def delete(self, id_: int) -> None:
        team = self.get_by_id(id_)
        team.delete()

    def get_all(self) -> List[Team]:
        return Team.objects.all()

    def get_by_id(self, id_: int) -> Team:
        return Team.objects.filter(id=id_).get()
