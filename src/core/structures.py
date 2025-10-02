class Project:
    def __init__(self,
            name: str,
            path: str,
            version: str,
            languages: list,
            frameworks: list,
            description: str
        ) -> None:
        
        self.name = name
        self.path = path
        self.version = version
        self.languages = languages
        self.frameworks = frameworks
        self.description = description
    
    def json(self) -> dict:
        return {
            'name': self.name,
            'path': self.path,
            'version': self.version,
            'language': self.languages,
            'framevorks': self.frameworks,
            'description': self.description
        }