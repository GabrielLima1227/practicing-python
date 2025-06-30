class Settings:
    def __init__(self, theme: str, language: str):
        self.theme = theme
        self.language = language

    def __str__(self):
        return f"Configurações Atuais: Tema='{self.theme}', Idioma='{self.language}'"

    def set_configurations(self, new_theme: str = None, new_language: str = None) -> None:
        if new_theme is not None:
            self.theme = new_theme
        if new_language is not None:
            self.language = new_language
        print(f"Configurações atualizadas: Tema = '{self.theme}', Idioma = '{self.language}'")


my_settings = Settings(theme='claro', language='pt-BR')
print(my_settings)

my_settings.set_configurations(new_theme='escuro')
print(my_settings)

my_settings.set_configurations(new_language='en-US')
print(my_settings)

my_settings.set_configurations(new_theme='claro', new_language='es-ES')
print(my_settings)

my_settings.set_configurations()
print(my_settings)