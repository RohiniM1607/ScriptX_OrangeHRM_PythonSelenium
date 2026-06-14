class BuzzPage:
    buzz_menu = "//span[text()='Buzz']"
    post_text_area = "//textarea[@placeholder=\"What's on your mind?\"]"
    post_button = "//button[@type='submit']"

    success_message = "//div[contains(@class,'oxd-toast-content')]"

    latest_post_text = "(//p[contains(@class, 'orangehrm-buzz-post-body-text')])[1]"