"""Tests for vocabulary compression."""

from src.vocabulary import VocabularyTransformer


def test_transform_prints_sorted_word_frequencies_and_returns_content(capsys) -> None:
	content = "Pega pega token"

	result = VocabularyTransformer().transform(content)

	assert result == content
	assert capsys.readouterr().out.splitlines() == [
		"Word frequency in TOON",
		"WORD                             COUNT",
		"----------------------------------------",
		"pega                             2",
		"token                            1",
	]
