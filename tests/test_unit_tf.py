import pytest
import socketserver

from tf.core import engine


@pytest.mark.unit
class TestTestFolder:

    tf = None

    @classmethod
    def setup_class(cls):
        cls.tf = engine.TestFolder()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @classmethod
    def teardown_class(cls):
        del cls.tf

    def test_instance(self):
        assert isinstance(self.tf, engine.TestFolder), f"Instance missmatch need to be a {engine.TestFolder.__name__}"

    def test_sub_instance(self):
        assert issubclass(self.tf.__class__, socketserver.ThreadingTCPServer), f"Subclass missmatch need to be a {socketserver.ThreadingTCPServer.__name__}"
