from argparse import Namespace
from core.handler import ProjectsHandler
from core.structures import Project


class TerminalUserInterface:
    def __init__(self, args: Namespace) -> None:
        self.handler = ProjectsHandler(args.projects_path)
        self.args = args

    def init_command(self) -> None:
        self.handler.init_project_files(
            Project(
                name=self.args.name,
                path=self.args.path,
                version=self.args.version,
                languages=self.args.languages,
                frameworks=self.args.frameworks,
                description=self.args.description,
            )
        )

    def info_command(self) -> None: ...

    def list_command(self) -> None: ...

    def update_command(self) -> None: ...
