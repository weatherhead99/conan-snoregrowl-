from conans import ConanFile, CMake, tools
import os

class SnoregrowlConan(ConanFile):
    name = "snoregrowl++"
    version = "0.5.0"
    license = "BSD 3 Clause"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "SnoreGrowl is a fork of gntp-send which is a command line tool for sending Growl notifications."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    sha256 = "5180628ce1c732abfc1001db48302b0d63534a3d62dc50a4655e0b4675a918be"

    def source(self):
        tools.get("https://github.com/Snorenotify/SnoreGrowl/archive/v%s.tar.gz"
                  % self.version, sha256=self.sha256)
        
    def build(self):
        cmake = CMake(self)
        if self.options.shared:
            cmake.definitions["SNOREGROWL_STATIC"] = "OFF"
        else:
            cmake.definitions["SNOREGROWL_STATIC"] = "ON"
            
        sf = os.path.join(self.source_folder,"SnoreGrowl-%s" % self.version)
        cmake.configure(source_folder=sf)
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs=tools.collect_libs(self)
        if self.settings.compiler == "gcc":
            self.cpp_info.libs.append("-lpthread")


