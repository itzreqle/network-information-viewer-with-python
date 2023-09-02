# Network Information Viewer with Python

## Overview

This Python script retrieves and displays information about the network interfaces and IP addresses of your computer. It is designed to work on Mac, Linux, and Windows systems and uses the `psutil` and `termcolor` libraries.

## How It Works

The script performs the following steps:

1. Gets the hostname of the computer using the `socket.gethostname()` function.

2. Retrieves the IP addresses associated with the computer using `socket.gethostbyname_ex(hostname)`.

3. Fetches network interface configurations using the `psutil.net_if_addrs()` function.

4. Prints the hostname and IP addresses in colored text.

5. Prints network interface configurations, including interface names, IP addresses, netmasks, and MAC addresses.

## Installation

Follow these steps to install and run the script:

### Prerequisites

Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Clone the Repository

Clone this repository to your local machine using the following `git` command:

```bash
git clone https://github.com/itzreqle/network-information-viewer-with-python.git
```

### Dependencies

This script relies on two Python libraries, `psutil` and `termcolor`. You can install them using `pip`:

```bash
pip install psutil termcolor
```

### Running the Script

1. Open a terminal or command prompt.
    
2. Navigate to the directory where the script (`network_info.py`) is located within the cloned repository.
    
3. Run the script with Python:
    
    ```bash
    python network_info.py
    ```
    
## Compatibility

This script is compatible with Mac, Linux, and Windows operating systems.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.
