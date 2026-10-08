"""Structural compression helpers."""

from .interface import Transformer


class StructuralTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Apply structural compression to content."""
		raise NotImplementedError
