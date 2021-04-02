import pytest

from tf.core import engine


@pytest.mark.system
class TestTestFolder:

    def test_instance(self):
        tf = engine.TestFolder()
        assert isinstance(tf, engine.TestFolder), f"Instance missmatch need to be a {engine.TestFolder.__name__}"
