from conans import ConanFile


class SPIRVHeadersConan(ConanFile):
    name = "SPIRV-Headers"
    version = "0.0.1"
    url = "https://github.com/Esri/SPIRV-Headers/blob/runtimecore"
    license = "https://github.com/Esri/SPIRV-Headers/blob/runtimecore/LICENSE"
    description = "Machine-readable files for the SPIR-V Registry"

    # Use the OS default to get the right line endings
    settings = "os"

    def package(self):
        base = self.source_folder
        relative = "3rdparty/SPIRV-Headers"

        # headers
        self.copy("*", src=base + "/include", dst=relative + "/include")
