from androguard.misc import apk

class APKAnalyzer:
    def __init__(self, apk_path):
        self.apk = apk.APK(apk_path)

    def get_package_name(self):
        return self.apk.get_package()

    def get_version_name(self):
        return self.apk.get_androidversion_name()

    def get_version_code(self):
        return self.apk.get_androidversion_code()

    def get_permissions(self):
        return self.apk.get_permissions()

    def get_main_activity(self):
        return self.apk.get_main_activity()

    def get_signature(self):
        return self.apk.get_signature()

    def analyze(self):
        metadata = {
            'package_name': self.get_package_name(),
            'version_name': self.get_version_name(),
            'version_code': self.get_version_code(),
            'permissions': self.get_permissions(),
            'main_activity': self.get_main_activity(),
            'signature': self.get_signature()
        }
        return metadata

# Example usage:
if __name__ == "__main__":
    apk_analyzer = APKAnalyzer("/Users/tinmaungzin/Downloads/sample.apk")
    metadata = apk_analyzer.analyze()
    print(metadata)
