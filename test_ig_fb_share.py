from pages.drivers import Drivers
from pages.facebook_page import FacebookPage
from pages.instagram_page import InstagramPage

# test descriptions
# share image from instagram to facebook with validation

# test setup
ig_img_name = 'Test Test'

# facebook login
user_gmail = 'test.integrate.10@gmail.com'
pw_gmail = 'testpw_02'

# instagram login
user_ig = 'radek.spacek.165'
pw_ig = 'testpw_02'

# INSTAGRAM
browser1 = Drivers('--start-maximized').chrome()
ip = InstagramPage(driver=browser1)

# test start
ip.go()

# login to ig
ip.ig_user_input.input_text(user_ig)
ip.ig_pw_input.input_text(pw_ig)
ip.ig_login_button.click()
ip.ig_notnow_button.click()

# share img to fb
ip.profile_link.click()
ip.image.click()
ip.menu_button.click()
ip.share_button.click()
ip.share_fb_button.click()

# switch to fb login tab from ig
browser1.switch_to.window(browser1.window_handles[1])
ip.email_fb_input.input_text(user_gmail)
ip.pw_fb_input.input_text(pw_gmail)
ip.login_fb_button.click()

# name and post img to be shared
ip.comment_img.input_text(ig_img_name)
ip.post_fb_button.click()

# switch back to ig tab
browser1.switch_to.window(browser1.window_handles[0])
ip.close_share.click()
ip.close_image.click()

# FACEBOOK
browser2 = Drivers('--start-maximized').chrome()
fp = FacebookPage(driver=browser2)
fp.go()

# login to fb
fp.fb_user_input.input_text(user_gmail)
fp.fb_pw_input.input_text(pw_gmail)
fp.fb_login_button.click()

# go to shared image and get img name
fp.profile_button.click()
fb_img_name = fp.img_name.text

# validate image name
assert fb_img_name == ig_img_name
print(f'fb image name "{fb_img_name}" correspond to ig image name "{ig_img_name}"')
print('Test passed')

browser1.quit()
browser2.quit()




































