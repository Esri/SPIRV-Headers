from conans import ConanFile

class SPIRVHeadersConan(ConanFile):
    name = "SPIRV-Headers"
    version = "0.0.1"
    url = "https://github.com/duncanthomson/SPIRV-Headers"
    license = "https://github.com/duncanthomson/SPIRV-Headers/blob/main/LICENSE"
    description = "Machine-readable files for the SPIR-V Registry"

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder
        relative = "3rdparty/SPIRV-Headers"

        # headers
        self.copy("*", src=base + "/include", dst=relative + "/include")
