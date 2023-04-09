from argparse import ArgumentParser

from cli import CLI
from config import DEFAULT_USERNAME


class CustomParser:
    def __init__(self):
        parser = ArgumentParser()
        command_group = parser.add_argument_group('general behaviour')
        command_group.add_argument('command')
        options_group = parser.add_argument_group('website and username')
        options_group.add_argument('--website', '-w', default=None)
        options_group.add_argument('--username', '-u', default=DEFAULT_USERNAME)

        self.args = parser.parse_args()
        command = self.args.command

        if hasattr(self, command):
            getattr(self, command)()
        else:
            print('Unrecognized command')

    def gui(self):
        from gui import GUI
        GUI(DEFAULT_USERNAME).main()

    def cli(self):
        CLI().main()

    def quick(self):
        website, username = self.args.website, self.args.username
        if website is None:
            print('Please, provide a website using --website (-w) argument')
        else:
            response = CLI().quick(website, username)
            print(response)

    def lookup(self):
        website = self.args.website
        if website is None:
            print('Please, provide a website using --website (-w) argument')
        else:
            response = CLI().find_password(website)
            print(response)
