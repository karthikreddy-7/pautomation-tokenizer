"""Vocabulary-based compression helpers."""

import re
from collections import Counter

from .interface import Transformer


class VocabularyTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Print case-insensitive word frequencies and return the content unchanged."""
		words = re.findall(r"[^\W\d_][\w'-]*", content.casefold())
		frequencies = Counter(words)
		#for word, count in sorted(frequencies.items(), key=lambda entry: (-entry[1], entry[0])):
		#	print(f"{word:<32} {count}")

		return content
