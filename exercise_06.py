#!/usr/bin/python3


class Harl:
    def __init__(self):
        """
        Initialize the Harl class with methods mapped to log levels in hierarchical order.
        """
        self._log_levels = [
            ("DEBUG", self._debug),
            ("INFO", self._info),
            ("WARNING", self._warning),
            ("ERROR", self._error),
        ]

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
        Display messages for the given log level and all levels above it.
        :param level: The log level as a string (e.g., "DEBUG", "INFO").
        """
        level_found = False
        for log_level, method in self._log_levels:
            if log_level == level:
                level_found = True
            if level_found:
                method()
        if not level_found:
            print("[UNKNOWN] Probably complaining about insignificant problems.")


# Example Usage
if __name__ == "__main__":
    harl = Harl()
    print("Testing Harl's logging filter:")
    # Testing filtering from "WARNING"
    print("\nStarting from WARNING:")
    harl.complain("WARNING")
    # Testing filtering from "INFO"
    print("\nStarting from INFO:")
    harl.complain("INFO")
    # Testing filtering from "DEBUG"
    print("\nStarting from DEBUG:")
    harl.complain("DEBUG")
    # Testing an unknown log level
    print("\nTesting an unknown log level:")
    harl.complain("TRACE")