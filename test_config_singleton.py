# test_config_singleton.py
import unittest
from config_singleton.py import Config

class TestConfigSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        config1 = Config()
        config2 = Config()
        self.assertIs(config1, config2, "Config should be the same instance")

    def test_load_config(self):
        config = Config()
        self.assertIn("database", config.get_config(), "Config should contain 'database' key")

    def test_update_config(self):
        config = Config()
        config.update_config("host", "127.0.0.1")
        self.assertEqual(config.get_config()["host"], "127.0.0.1", "Config 'host' should be updated")

if __name__ == "__main__":
    unittest.main()
