"""Convert JSON-compatible data to TOON text."""

from .interface import Transformer


class JsonToToonTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Convert JSON text to TOON text."""
		raise NotImplementedError
