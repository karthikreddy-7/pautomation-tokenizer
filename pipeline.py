"""Orchestrate the PAutomation tokenization pipeline."""

from src.interface import Transformer


class Pipeline(Transformer):
	def transform(self, content: str) -> str:
		"""Run the complete tokenization pipeline on content."""
		raise NotImplementedError
