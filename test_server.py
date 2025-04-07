import unittest
import jsonrpclib
import os

class TestNDCServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.proxy = jsonrpclib.Server("http://localhost:5001")

    def test_whoareyou(self):
        result = self.proxy.whoareyou()
        self.assertIn("server", result.lower())

    def test_ping(self):
        result = self.proxy.ping()
        self.assertEqual(result, "pong")

    def test_get_version(self):
        version = self.proxy.get_version()
        self.assertRegex(version, r"\d+\.\d+\.\d+")

    def test_make_and_delete_folder(self):
        folder_name = "testfolder123"
        result = self.proxy.make_folder(folder_name)
        self.assertIn("created", result.lower())
        self.assertTrue(os.path.exists(folder_name))

        result = self.proxy.delete_folder(folder_name)
        self.assertIn("deleted", result.lower())
        self.assertFalse(os.path.exists(folder_name))

    def test_search_found(self):
        test_file = "testfile.txt"
        with open(test_file, "w") as f:
            f.write("temporary test file")
        result = self.proxy.search(test_file)
        os.remove(test_file)
        self.assertIn("found", result.lower())

    def test_search_not_found(self):
        result = self.proxy.search("thisfiledoesnotexist.txt")
        self.assertIn("not found", result.lower())

    def test_list_friends(self):
        result = self.proxy.list_friends()
        self.assertIsInstance(result, list)

    def test_heartbeat_format(self):
        result = self.proxy.heartbeat()
        self.assertIsInstance(result, dict)

    def test_pass_msg_loopback(self):
        result = self.proxy.pass_msg("hello", "1")
        self.assertIn("received", result.lower())

if __name__ == '__main__':
    unittest.main()

