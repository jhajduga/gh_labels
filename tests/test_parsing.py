import pytest
import tomllib
from labelsync import sync


def test_parse_toml_file(tmp_path):
    """Test whether labels are correctly parsed from a TOML file."""
    # Prepare a minimal TOML input
    toml_content = '''
    [[label]]
    name = "bug"
    description = "Something isn't working"
    color = "d73a4a"

    [[label]]
    name = "feature"
    description = "New feature added"
    color = "0e8a16"
    '''

    toml_file = tmp_path / "labels.toml"
    toml_file.write_text(toml_content)

    # Parse with the same logic used by the sync script
    with open(toml_file, "rb") as f:
        data = tomllib.load(f)

    assert "label" in data
    assert len(data["label"]) == 2

    assert data["label"][0]["name"] == "bug"
    assert data["label"][1]["name"] == "feature"
    assert data["label"][1]["color"] == "0e8a16"
