import time
from threading import Timer
from backend.components import TFTUpdater


class TFTScheduler:
    """
    Class to schedule TFT data updates.
    """


    def __init__(self, paths):
        """
        Initializes the TFTScheduler class.
        """
        
        self.paths = paths


    def start(self):
        """
        Schedules TFT data updates.
        """
        
        # Create an instance of TFTUpdater
        updater = TFTUpdater(paths=self.paths)

        # Call the update function initially
        updater.update()

        # Schedule the update function to run every 12 hours
        interval = 12 * 60 * 60  # 12 hours in seconds
        Timer(interval, updater.update).start()

        # Keep the scheduler running indefinitely
        while True:
            time.sleep(1)