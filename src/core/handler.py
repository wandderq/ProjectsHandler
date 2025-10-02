import os
import json
import logging as lg

from core.structures import Project
from string import Template

logger = lg.getLogger("projectshandler")


class PathNotFoundError(Exception):
    pass


class ProjectsHandler:
    def __init__(self, projects_path: str) -> None:
        if not os.path.isdir(projects_path):
            raise PathNotFoundError(f"Projects directory '{projects_path}' not found")

        self.required_project_files = {
            "TODO.md": Template("TODO for $pname\n\n"),
            "DESCRIPTION.md": Template(
                "Description for $pname.\nWARN: This file is some kind of developer's notes, not for production (add to .gitignore)\n\n"
            ),
            "project.json": Template("$pjson"),
        }
        self.projects_path = os.path.abspath(projects_path)

    def init_project_files(self, project: Project) -> None:
        spec_path = os.path.join(project.path, ".project")
        os.makedirs(spec_path, exist_ok=True)
        spec_files = os.listdir(spec_path)
        
        logger.debug(f'Existing spec_files: {spec_files}')
        
        if spec_files:
            if all([file in spec_files for file in self.required_project_files.keys()]):
                overwrite = (
                    input(f"Project alreday exists. Overwrite it? y/n: ").lower().strip()
                    == "y"
                )
                if not overwrite:
                    return
            else:
                overwrite = (
                    input("Some project files alreday exist. Overwrite it? y/n: ")
                    .lower()
                    .strip()
                    == "y"
                )
        else:
            overwrite = True

        for file_name, file_content in self.required_project_files.items():
            if (not file_name in spec_files) or overwrite:
                file_path = os.path.join(spec_path, file_name)
                logger.debug(f"Writing file: {file_path}")

                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(
                        file_content.safe_substitute(
                            pname=project.name,
                            pjson=json.dumps(
                                project.json(), indent=4, ensure_ascii=False
                            ),
                        )
                    )
