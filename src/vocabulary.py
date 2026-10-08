"""Vocabulary-based compression helpers."""

from .interface import Transformer


class VocabularyTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Pass content through until vocabulary compression rules are defined."""
		return content
