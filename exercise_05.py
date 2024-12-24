#!/usr/bin/python3


class Harl:
    def __init__(self):
        """
        Initialize the Harl class with methods mapped to log levels.
        """
        self._log_levels = {
            "DEBUG": self._debug,
            "INFO": self._info,
            "WARNING": self._warning,
            "ERROR": self._error,
        }

    def _debug(self):
        print("[DEBUG] I love having extra bacon for my 7XL-double-cheese-triple-pickle-special-ketchup burger. I really do!")

    def _info(self):
        print("[INFO] I cannot believe adding extra bacon costs more money. You didn’t put enough bacon in my burger!")

    def _warning(self):
        print("[WARNING] I think I deserve to have some extra bacon for free. I’ve been coming for years!")

    def _error(self):
        print("[ERROR] This is unacceptable! I want to speak to the manager now.")

    def complain(self, level: str):
        """
        Call the appropriate log level method based on the input.
        :param level: The log level as a string (e.g., "DEBUG", "INFO").
        """
        if level in self._log_levels:
            self._log_levels[level]()
        else:
            print("[UNKNOWN] This log level is not recognized.")


# Example Usage
if __name__ == "__main__":
    harl = Harl()
    print("Testing Harl's logging system:")
    # Testing all log levels
    harl.complain("DEBUG")
    harl.complain("INFO")
    harl.complain("WARNING")
    harl.complain("ERROR")
    print("\nTesting an unknown log level:")
    harl.complain("TRACE")
