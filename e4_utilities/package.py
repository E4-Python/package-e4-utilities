from .json import *
from .refactor import *

class PythonPackage:
    def __init__(self, directory: str):
        self.directory = directory
        self.config_file_path = os.path.join(self.directory, 'package.json')
        self.config = load_json(self.config_file_path)

    def init(self, new_name: str, new_repository: str = ''):
        if not new_name: return

        # 패키지 이름 설정
        self.set_name(new_name)

        # 패키지 설명 설정
        parsed_name = new_name.split('_')
        pascal_cased_name = ' '.join(parsed_name)
        pascal_cased_name = pascal_cased_name.title()
        self.set_description(f'{pascal_cased_name}')

        # url 설정
        if not new_repository:
            new_repository = '-'.join(parsed_name)
            new_repository = 'package-' + new_repository
        self.set_url(new_repository)

    def save_config(self):
        save_json(self.config_file_path, self.config)

    def set_name(self, new_name: str):
        # 파이썬 패키지 정보 가져오기
        old_name = self.config['name']

        # 파이썬 패키지 정보 수정
        self.config['name'] = new_name
        self.config['packages'].remove(old_name)
        self.config['packages'].append(new_name)

        # 파이썬 파일 내용 수정
        file_paths = get_file_paths(self.directory, ['.py'], True)
        for file_path in file_paths:
            replace_text(file_path, old_name, new_name)

        # 파이썬 패키지 폴더명 수정
        replace_directory(os.path.join(self.directory, old_name), old_name, new_name)

    def set_version(self, new_version: str):
        self.config['version'] = new_version

    def set_description(self, new_description: str):
        self.config['description'] = new_description

    def set_url(self, new_repository: str, new_owner: str = ''):
        github_url = 'https://github.com/'
        parsed_url = self.config['url'].removeprefix(github_url).split('/')
        if len(parsed_url) != 2:
            return

        old_owner = parsed_url[0]

        new_url = github_url + new_owner + '/' + new_repository if new_owner else github_url + old_owner + '/' + new_repository
        self.config['url'] = new_url