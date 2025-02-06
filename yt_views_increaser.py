#Dataimpulse login
# username d7a07d433161639a3d10
# password b53ca01b31a1af85

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

proxy = "gw.dataimpulse.com:823" 
username = "d7a07d433161639a3d10"  
password = "b53ca01b31a1af85" 


chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')

driver = uc.Chrome(options=chrome_options)

watching = int(input("How many seconds do you want to watch the videos? "))
num_urls = int(input("Enter the number of YouTube URLs you want to open: "))
youtube_urls = [input(f"Enter YouTube video URL {i + 1}: ") + "?autoplay=1" for i in range(num_urls)]

repeat_count = int(input("Enter the number of views you want to get: "))


def open_all_tabs():

    for youtube_url in youtube_urls:
        driver.execute_script(f"window.open('{youtube_url}', '_blank');")
    time.sleep(2)  


def setup_video_in_tabs():
    for handle in driver.window_handles[1:]:  
        driver.switch_to.window(handle)
        try:
            # Wait for the video element and set up autoplay, mute, low resolution, and start time
            video_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )
            
            try:
                element = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button')
                if element:
                    element.click()
            except NoSuchElementException:
                pass
            time.sleep(3)
            try:
                element = driver.find_element(By.XPATH, '#//*[@id="skip-button:3"]')
                if element:
                    time.sleep(7)
                    element.click()
            except NoSuchElementException:
                pass


            driver.execute_script("""
                var video = document.querySelector('video');
            if (video) {
                video.muted = true;  // Mute the video
                video.play();  // Start playing

                // Attempt to skip ad if "Skip Ads" button appears
                function skipAd() {
                    var skipButton = document.querySelector('.ytp-ad-skip-button');
                    if (skipButton) {
                        skipButton.click();
                    }
                }
                // Check every 500 ms for the "Skip Ads" button
                setInterval(skipAd, 500);

                // Set to low quality (144p if available) after checking for ads
                setTimeout(() => {
                    var settingsButton = document.querySelector('.ytp-settings-button');
                    settingsButton.click();
                    setTimeout(() => {
                        var qualityMenu = Array.from(document.querySelectorAll('.ytp-menuitem'))
                                                .find(item => item.innerText.includes('Quality'));
                        if (qualityMenu) {
                            qualityMenu.click();
                            setTimeout(() => {
                                var lowQualityOption = Array.from(document.querySelectorAll('.ytp-menuitem'))
                                                            .find(item => item.innerText.includes('144p') || item.innerText.includes('240p'));
                                if (lowQualityOption) {
                                    lowQualityOption.click();
                                }
                            }, 500);
                        }
                    }, 500);
                }, 500); // Wait briefly before changing quality to allow for any ad to play and be skipped
            }
        """)
        except Exception as e:
            print("Setup failed, retrying manual play:", e)


def close_all_tabs():
    driver.switch_to.window(driver.window_handles[0])
    for handle in driver.window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()
    driver.switch_to.window(driver.window_handles[0])

try:
    
    for cycle in range(repeat_count):
        print(f"Cycle {cycle + 1} of {repeat_count} - Opening and setting up tabs...")
        
        open_all_tabs()

        setup_video_in_tabs()
    
        print("Waiting for seconds...")
        time.sleep(watching)

        print("Closing all tabs...")
        close_all_tabs()

    print("Task completed successfully.")

finally:
    driver.quit()  


from selenium import webdriver

# Create a new instance of the WebDriver (e.g., Chrome, Firefox)
driver = webdriver.Chrome()

# Set the size of the window (optional)
driver.set_window_size(500, 400)

# Position the window in the top-left corner (coordinates 0, 0)
driver.set_window_position(5, 400)
driver.set_window_position(0, 0)
driver.set_window_position(400, 4)
driver.set_window_position(900, 4)
driver.set_window_position(900, 400)
driver.set_window_position(500, 400)

# Open a website
driver.get("https://www.example.com")

# Perform any other actions with the driver...

# Close the browser
driver.quit()