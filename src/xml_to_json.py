"""Convert PAutomation XML documents to JSON-compatible data."""

import json
import xmltodict
from .interface import Transformer

class XmlToJsonTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Convert PAutomation XML content to JSON text."""
		parsed = xmltodict.parse(content)
		return json.dumps(parsed, ensure_ascii=False, indent=2)
