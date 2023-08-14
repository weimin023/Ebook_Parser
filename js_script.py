import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class js_utils:
    def run_javascript(driver, from_page, to_page):
        script = """
        function downloadPages(from, to) {
            for (i = from; i <= to; i++) {
                const pageCanvas = document.getElementById('page_' + i);
                if (pageCanvas === null) break;
                const pageNo = i;
                pageCanvas.toBlob(
                    blob => {
                        const anchor = document.createElement('a');
                        anchor.download = 'page_' + pageNo + '.png';
                        anchor.href = URL.createObjectURL(blob);
                        anchor.click();
                        URL.revokeObjectURL(anchor.href);
                    }
                );
            }
        }

        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        async function run(from, to) {
            for (let i = from; i <= to; i++) {
                this.GotoPage(i);
                await sleep(5 * 1000);
                downloadPages(i, i);
                console.log(`Page ${i} downloaded.`);
            }
            console.log(`Finish.`);
        }

        run(arguments[0], arguments[1]); // Call run function with arguments from execute_script
        """

        driver.execute_script(script, from_page, to_page)
        completion_element_id = 'finish-message'

        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, completion_element_id)))
        driver.quit()
        