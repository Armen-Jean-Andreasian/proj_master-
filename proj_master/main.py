from proj_master.src import ProjectStructureGenerator


class Cat:
    @staticmethod
    def build_structure(project_name: str, developer_name: str, pro_mode=False):
        """
        Builds project structure.

        Params:
        `project_name` – Name of the project (root dir name as well).
        `pro_mode` – (False by default)
            If `pro_mode` is off, folders and files to create:
                - 'dev', 'src', 'tests', 'utils'
                - 'requirements.txt', 'README.md', 'LICENSE', '.gitignore'
            If it's on:
                - 'dev', 'src', 'tests', 'utils', 'docs', 'data', 'config', 'logs'
                - 'requirements.txt', 'README.md', 'LICENSE', '.gitignore', 'requirements-dev.txt', 'setup.py',
                  'CHANGELOG.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md','MANIFEST.in', 'pyproject.toml'
        """

        generator = ProjectStructureGenerator(project_name, developer_name, pro_mode)
        generator.create_folders()
        generator.create_files()

        print(f"Project structure created for '{project_name}'")
