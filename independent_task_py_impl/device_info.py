import pyopencl as cl
import json
import subprocess

def get_accelerator_devices():
    # Get a list of platforms
    platforms = cl.get_platforms()

    # Filter devices to get only accelerator devices
    accelerator_devices = []
    for platform in platforms:
        devices = platform.get_devices(device_type=cl.device_type.ACCELERATOR)
        accelerator_devices.extend(devices)

    return accelerator_devices


def print_device_properties(device):
    print("Device Name:", device.name)
    print("Device Vendor:", device.vendor)
    print("Device Version:", device.version)
    print("Driver Version:", device.driver_version)
    print("OpenCL C Version:", device.opencl_c_version)
    print("Device Profile:", device.profile)
    print("Device Type:", cl.device_type.to_string(device.type))
    print("Global Memory Size (bytes):", device.global_mem_size)
    print("Local Memory Size (bytes):", device.local_mem_size)
    print("Max Compute Units:", device.max_compute_units)
    print("Max Work Group Size:", device.max_work_group_size)
    print("Max Work Item Sizes:", device.max_work_item_sizes)
# Call the function to get the list of OpenCL accelerator devices



def get_device_properties_as_json(device):
    properties = {
        "name": device.name,
        "vendor": device.vendor,
        "version": device.version,
        # Add more properties as needed
    }
    return json.dumps(properties)

accelerator_devices = get_accelerator_devices()

# Print information about accelerator devices
for device in accelerator_devices:
    print_device_properties(device)
    print("-" * 30)
"""# Call the function to get the list of OpenCL accelerator devices
accelerator_devices = get_accelerator_devices()

# Select the first accelerator device (you can choose the one you want)
selected_device = accelerator_devices[0]

# Get the device properties as a JSON string
device_properties_json = get_device_properties_as_json(selected_device)

# Pass the device properties JSON as a command-line argument to the C++ program
subprocess.call(["./cpp_program", device_properties_json])"""






