import json
import importlib

class ConfigParser:

    __slots__ = ("file", "config", "providers", "targets", "messages")

    def __init__(self, file):
        self.file = file
        self.config = {}
        self.providers = {}
        self.targets = []
        self.messages = []
        self.update_config()

    def update_config(self):
        data = open(self.file).read()
        self.config = json.loads(data)
        self.targets = []
        self.messages = []

    def get_target_list(self):
        if self.targets:
            return self.targets

        self.targets = []
        self.targets.extend(self.config["targets"])
        if "debug" in self.config and self.config["debug"]:
            self.targets.append(None)

        return self.targets

    def get_messages(self):
        if self.messages:
            return self.messages

        if "messages" not in self.config:
            print("No messages")
            return []
        else:
            self.messages = []
            for message in self.config["messages"]:
                provider, arguments = message.popitem()

                if provider not in self.providers:
                    module = importlib.import_module(provider + "Provider")
                    self.providers[provider] = getattr(module, provider + "Provider")

                message = self.providers[provider](**arguments)
                self.messages.append(message)

            return self.messages

    def is_verbose(self):
        return "verbose" in self.config and self.config["verbose"]





