"""Convert PAutomation XML documents to JSON-compatible data."""

from .interface import Transformer


class XmlToJsonTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Convert PAutomation XML content to JSON text."""
		raise NotImplementedError
