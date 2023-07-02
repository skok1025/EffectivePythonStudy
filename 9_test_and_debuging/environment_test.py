from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main


class EnvironmentTest(TestCase):
    def setUp(self) -> None:
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)

    def tearDown(self) -> None:
        self.test_dir.cleanup()

    def test_modify_file(self):
        with open(self.test_path / 'data.bin', 'w') as f:
            f.write('hello')
        self.assertEqual('hello', open(self.test_path / 'data.bin').read())

if __name__ == '__main__':
    main()