import time
from threading import Timer
from TFTUpdater import TFTUpdater


class TFTScheduler:
    """
    Class to schedule TFT data updates.
    """


    def __init__(self):
        """
        Initializes the TFTScheduler class.
        """
        
        pass


    def scheduler(self):
        """
        Schedules TFT data updates.
        """
        
        # Create an instance of TFTUpdater
        updater = TFTUpdater()

        # Call the update function initially
        updater.update()

        # Schedule the update function to run every 12 hours
        interval = 12 * 60 * 60  # 12 hours in seconds
        Timer(interval, updater.update).start()

        # Keep the scheduler running indefinitely
        while True:
            time.sleep(1)