import os

class Screenshot:

    @staticmethod
    def take_screenshot(driver, file_name):
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        driver.save_screenshot(os.path.join(screenshots_dir, file_name))

