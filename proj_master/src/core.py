import os
from proj_master.file_content import get_readme_content, get_gitignore_content, get_licence_content
from datetime import datetime


class ProjectStructureGenerator:
    folders = ['dev', 'src', 'tests', 'utils']
    files = ['requirements.txt', 'README.md', 'LICENSE', '.gitignore']

    _folders_pro = ['docs', 'data', 'config', 'logs']
    _files_pro = ['requirements-dev.txt', 'setup.py', 'CHANGELOG.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md',
                  'MANIFEST.in', 'pyproject.toml']

    def __init__(self, project_name: str, developer_name: str, pro_mode: bool = False):
        self.project_name: str = project_name

        self.readme_md_content: str = get_readme_content(project_name=self.project_name)
        self.gitignore_content: str = get_gitignore_content()
        self.license_content: str = get_licence_content(dev_name=developer_name, year=datetime.now().year)

        if pro_mode:
            self.folders.extend(self._folders_pro)
            self.files.extend(self._files_pro)

    def create_folders(self):
        # creating root dir
        os.makedirs(self.project_name)

        # iterating over self.folders, creating and placing '.keep' files in them
        for folder in self.folders:
            folder_to_create = os.path.join(self.project_name, folder)

            os.makedirs(folder_to_create)

            with open(folder_to_create + '/.keep', mode="w") as _:
                pass

    def create_files(self):
        for file_name in self.files:
            with open(os.path.join(self.project_name, file_name), 'w') as file:

                match file_name:
                    case "README.md":
                        file.write(self.readme_md_content)

                    case '.gitignore':
                        file.write(self.gitignore_content)

                    case "LICENSE":
                        file.write(self.license_content)

                    case _:
                        pass
