from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

from pifs.connection import create_connection
from pifs.query import query


class Account:
    __instances = {}

    def __new__(cls, account_name: str, *_args: Tuple[Any], **_kwargs: Dict[str, Any]) -> Account:
        if account_name not in cls.__instances:
            cls.__instances[account_name] = super().__new__(cls)
        return cls.__instances[account_name]

    def __init__(self, account_name: Optional[str] = None) -> None:
        self._auto_commit_connection = create_connection(account_name, auto_commit=True)
        self._manual_commit_connection = create_connection(account_name, auto_commit=False)
        self._current_connection = self._auto_commit_connection

    def __enter__(self, auto_commit: bool = False) -> Account:
        if auto_commit:
            self._current_connection = self._auto_commit_connection
        else:
            self._current_connection = self._manual_commit_connection

        query.connection = self._current_connection
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._current_connection == self._manual_commit_connection:
            if exc_type is None:
                self._manual_commit_connection.commit()
            else:
                self._manual_commit_connection.rollback()
        query.connection = self._current_connection = self._auto_commit_connection
