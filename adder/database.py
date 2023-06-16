from pifs.entity import Entity, EntityMetadata


class Database(Entity):

    def create(self, or_replace: bool = False, if_not_exists: bool = False):
        query = "create"
        if or_replace:
            query += " or replace"
        if if_not_exists:
            query += " if not exists"
        query += f" database {self.name}"