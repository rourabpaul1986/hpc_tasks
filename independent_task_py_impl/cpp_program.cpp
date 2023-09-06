#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <unistd.h>
#include <vector>

// OpenCL utility layer include
#include "xcl2/xcl2.hpp"
#include <nlohmann/json.hpp>



using json = nlohmann::json;

class OpenCLDevice {
public:
    std::string name;
    std::string vendor;
    std::string version;
    // Add more device properties as needed
};

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <device_properties_json>" << std::endl;
        return 1;
    }

    std::string device_properties_json_str = argv[1];
    json device_properties_json = json::parse(device_properties_json_str);

    OpenCLDevice device;
    device.name = device_properties_json["name"];
    device.vendor = device_properties_json["vendor"];
    device.version = device_properties_json["version"];
    // Parse more device properties as needed

    // Access the device properties
    std::cout << "Device Name: " << device.name << std::endl;
    std::cout << "Device Vendor: " << device.vendor << std::endl;
    std::cout << "Device Version: " << device.version << std::endl;
    std::cout << "Driver Version: " << device.driver << std::endl;
    std::cout << "OpenCL C Version: " << device.opencl_c_version << std::endl;
    std::cout << "Device Profile: " << device.profile << std::endl;
    // Print more device properties as needed
    
    


    return 0;
}

