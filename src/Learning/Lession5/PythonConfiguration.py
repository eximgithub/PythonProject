# https://martin-thoma.com/configuration-files-in-python/
# https://charlesreid1.github.io/a-singleton-configuration-class-in-python.html#get-variable-functions
import json
import os

import typing


class Config(object):
    #########################
    # Begin Singleton Section
    #########################

    _CONFIG_FILE: typing.Optional[str] = None
    _CONFIG: typing.Optional[dict] = None

    def __init__(self, config_file=None):
        if config_file is None:
            config_file = Config.get_required_env_var("CONFIG_FILE")

        # Check that specified config file exists
        assert os.path.exists(config_file)

        # Use singleton pattern to store config file location/load config once
        Config._CONFIG_FILE = config_file
        with open(config_file, 'r') as f:
            Config._CONFIG = json.load(f)

    @staticmethod
    def get_config_file() -> str:
        return Config._CONFIG_FILE

    @staticmethod
    def get_required_env_var(envvar: str) -> str:
        if envvar not in os.environ:
            raise Exception(f"Please set the {envvar} environment variable")
            # raise ConfigException(f"Please set the {envvar} environment variable")
        return os.environ[envvar]

    @staticmethod
    def get_required_env_var(envvar: str) -> str:
        if envvar not in os.environ:
            raise Exception("Please set the {envvar} environment variable")
        return os.environ[envvar]

    @staticmethod
    def get_required_config_var(configvar: str) -> str:
        assert Config._CONFIG
        if configvar not in Config._CONFIG:
            raise Exception(f"Please set the {configvar} variable in the config file {Config._CONFIG_FILE}")
        return Config._CONFIG[configvar]

# class TempConfig(object):
#     """
#     Temporarily patch the Config class to use the config
#     dictionary specified in the constructor.
#     """

#     def __init__(self, config_dict, *args, **kwargs):
#         """This is the step that's run when object constructed"""
#         super().__init__()
#         # This is the temp configuration the user specified
#         self.config_dict = config_dict
#         # Make a temp dir for our temp config file
#         self.temp_dir = tempfile.mkdtemp()
#         # Make a temp config file
#         _, self.temp_json = tempfile.mkstemp(suffix=".json", dir=self.temp_dir)
#         # Set the wuz variable to the temporary directory
#         self.config_dict['wuz'] = self.temp_dir

#     def __enter__(self, *args, **kwargs):
#         """This is what's returned to the "as X" portion of the context manager"""
#         self._write_config(self.temp_json, json.dumps(self.config_dict))
#         # Re-init Config with new config file
#         Config(self.temp_json)
#         return self.temp_json

#     def __exit__(self, *args, **kwargs):
#         """
#         Close the context and clean up; the *args are needed in case there is
#         an exception (we don't deal with those here)
#         """
#         # Delete temp file
#         os.unlink(self.temp_json)
#         # Delete temp dir
#         shutil.rmtree(self.temp_dir)
#         # Reset all config variables
#         Config.reset()

#     def _write_config(self, target: str, contents: str):
#         """Utility method: write string contents to config file"""
#         with open(target, "w") as f:
#             f.write(contents)


with open("config.json") as json_data_file:
    data = json.load(json_data_file)
print(data)
