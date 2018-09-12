from conans import ConanFile, CMake
import os

class TestPackageConan(ConanFile):
    generators = "cmake"
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(os.path.join("bin","test_find_package"))
        self.run(os.path.join("bin","test_manual_conan"))
