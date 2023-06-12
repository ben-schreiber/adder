from __future__ import annotations
from typing import Dict, Optional

from pifs.connection import create_connection
from snowflake.connector import DictCursor, SnowflakeConnection


class QueryResult:
    def __init__(self, results_dict: Dict[str, str]) -> None:
        pass


class Query:
    def __init__(self) -> None:
        self._connection = None

    def __call__(self, query: str, fetch_rows: Optional[int] = None) -> QueryResult:
        cursor = self._connection.cursor(DictCursor)
        cursor.execute(query)
        if fetch_rows is not None:
            return cursor.fetchmany(fetch_rows)
        return cursor.fetchall()  # TODO

    @property
    def connection(self) -> SnowflakeConnection:
        if self._connection is None:
            self._connection = create_connection(auto_commit=True)
        return self._connection

    @connection.setter
    def connection(self, _c: SnowflakeConnection):
        if not isinstance(_c, SnowflakeConnection):
            raise ValueError(f"Connection must be of type SnowflakeConnection, not {type(_c)}")
        self._connection = _c


query = Query()
