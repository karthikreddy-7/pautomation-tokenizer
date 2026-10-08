"""Shared interface for content transformations."""

from abc import ABC, abstractmethod


class Transformer(ABC):
    @abstractmethod
    def transform(self, content: str) -> str:
        """Transform content and return the transformed text."""
        raise NotImplementedError