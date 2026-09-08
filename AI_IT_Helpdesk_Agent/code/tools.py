import socket
import subprocess


def check_internet_connection():
    """Check whether the computer can reach the internet."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "Internet connection is available."
    except OSError:
        return "Internet connection is not available."


def get_network_information():
    """Get basic network information."""
    try:
        result = subprocess.run(
            ["ipconfig"],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Unable to get network information: {e}"


def ping_test():
    """Test connectivity using ping."""
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "8.8.8.8"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "Ping test successful."
        else:
            return "Ping test failed."

    except Exception as e:
        return f"Ping test error: {e}"