import pytest

@pytest.fixture(scope="session")
def tmp_file(tmpdir_factory) -> str:
    tmp_file = tmpdir_factory.mktemp("test_dir").join("tmp.txt")
    return str(tmp_file)
