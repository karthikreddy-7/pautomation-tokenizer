"""Orchestrate the PAutomation tokenization pipeline."""

from pathlib import Path

from src.interface import Transformer
from src.json_to_toon import JsonToToonTransformer
from src.vocabulary import VocabularyTransformer
from src.xml_to_json import XmlToJsonTransformer


class Pipeline(Transformer):
	def transform(self, content: str) -> str:
		"""Run the complete tokenization pipeline on content."""
		examples_dir = Path(__file__).parent / "examples"
		content = XmlToJsonTransformer().transform(content)
		(examples_dir / "sample.json").write_text(content, encoding="utf-8")
		content = JsonToToonTransformer().transform(content)
		(examples_dir / "sample.toon").write_text(content, encoding="utf-8")
		content = VocabularyTransformer().transform(content)
		return content


def main() -> None:
	sample_path = Path(__file__).parent / "examples" / "sample.PAutomation"
	content = sample_path.read_text(encoding="utf-8")
	Pipeline().transform(content)


if __name__ == "__main__":
	main()
