"""Convert TOON text back to PAutomation XML."""

import json
import toon_format
import xmltodict

from .interface import Transformer


class ToonToXmlTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Decode TOON text and serialize the resulting data as XML."""
		parsed = toon_format.loads(content)
		return xmltodict.unparse(json.loads(json.dumps(parsed)), full_document=False)