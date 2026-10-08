"""Vocabulary-based compression helpers."""

from .interface import Transformer


class VocabularyTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Apply vocabulary-based compression to content."""
		raise NotImplementedError
