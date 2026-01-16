from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file='uiconfigfile.ini'):
        self.config = ConfigParser()
        # First attempt: read the path as given (absolute or relative to cwd)
        read_files = self.config.read(config_file)
        if not read_files:
            # If not found, try resolving relative to this module's directory
            module_dir = os.path.dirname(__file__)
            alt_path = os.path.join(module_dir, config_file)
            self.config.read(alt_path)

    def _get_list_option(self, option_name, default=None):
        # Try DEFAULT first; if missing, search other sections; return safe list
        val = None
        # config['DEFAULT'] is always available but may have no value for the key
        try:
            val = self.config['DEFAULT'].get(option_name)
        except Exception:
            val = None
        if val is None:
            for sec in self.config.sections():
                val = self.config[sec].get(option_name)
                if val:
                    break
        if not val:
            return default or []
        # split on comma and strip spaces, ignore empty items
        return [item.strip() for item in val.split(',') if item.strip()]

    def get_llm_options(self):
        return self._get_list_option('LLM_OPTIONS')

    def get_usecase_options(self):
        return self._get_list_option('USECASE_OPTIONS')

    def get_groq_model_options(self):
        return self._get_list_option('GROQ_MODEL_OPTIONS')

    def get_page_title(self):
        # Similar fallback logic for singular values
        val = None
        try:
            val = self.config['DEFAULT'].get('PAGE_TITLE')
        except Exception:
            val = None
        if val is None:
            for sec in self.config.sections():
                val = self.config[sec].get('PAGE_TITLE')
                if val:
                    break
        return val or ''