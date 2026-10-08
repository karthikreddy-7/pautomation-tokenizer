"""Convert JSON-compatible data to TOON text."""
import json
import toon_format
from .interface import Transformer

class JsonToToonTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Convert JSON text to TOON text."""
		return toon_format.dumps(json.loads(content))
