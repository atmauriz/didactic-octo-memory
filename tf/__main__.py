import argparse

parser = argparse.ArgumentParser(description="""TestFolder command line tool.""")
parser.add_argument(
    "--debug",
    action="store_true",
    help="Print debug info"
)

subparsers = parser.add_subparsers(dest="command", help="Operation")

# go subparser
go_parser = subparsers.add_parser(
    "go",
    help="Test Automation operation got it from the yaml file definition in the 'tests' folder"
)
go_parser.add_argument(
    "mode",
    help="select mode operation",
    choices=("soft", "hard")
)

# serve subparser
serve_parser = subparsers.add_parser(
    "serve",
    help="Test Automation operation serve a socket channel to communicate"
)
serve_parser.add_argument(
    "--host",
    help="Hostname of 'testfolder'"
)
serve_parser.add_argument(
    "--port",
    help="Port of 'testfolder'"
)

arguments = parser.parse_args()
if not arguments.command:
    parser.print_help()
