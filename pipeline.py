"""Orchestrate the PAutomation tokenization pipeline."""

from pathlib import Path

from src.interface import Transformer
from src.analysis import compare_xml
from src.json_to_toon import JsonToToonTransformer
from src.toon_to_xml import ToonToXmlTransformer
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
	examples_dir = Path(__file__).parent / "examples"
	original_xml = (examples_dir / "sample.PAutomation").read_text(encoding="utf-8")
	toon = Pipeline().transform(original_xml)
	reconstructed_xml = ToonToXmlTransformer().transform(toon)
	(examples_dir / "reconstructed.PAutomation").write_text(
		reconstructed_xml, encoding="utf-8"
	)

	comparison = compare_xml(original_xml, reconstructed_xml)
	print(f"XML equivalent after canonicalization: {comparison}")


if __name__ == "__main__":
	main()
