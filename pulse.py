from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    for i in range(10):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.pulselive.co.ke/influencer-awards/business/1j5g3fz")
        page.frame_locator("iframe").get_by_label("Khalif Kairo (Kai & Karo)").check()
        page.frame_locator("iframe").get_by_role("button", name="Vote").click()
        page.frame_locator("iframe").locator("#answer_12696698").click()
        page.frame_locator("iframe").locator("#captcha_12696698").click()
        element_content = page.frame_locator("iframe").locator("#captcha_12696698").inner_text()
    #print("Content of the clicked element:", element_content)
        equation = element_content.replace('=', '')
        operands = equation.split('+')

        # Convert the operands to integers and calculate the sum
        operand1 = int(operands[0].strip())
        operand2 = int(operands[1].strip())
        result = operand1 + operand2
        result_str = str(result)
        
        page.frame_locator("iframe").locator("#answer_12696698").fill(result_str)
        print("Captcha:", result_str)
        page.frame_locator("iframe").get_by_role("button", name="Vote").click()


        # ---------------------
        #context.close()
        #browser.close()


with sync_playwright() as playwright:
    run(playwright)
