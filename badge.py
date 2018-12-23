from pybadges import badge

s = badge(left_text="pre-commit", right_text="23%", right_color="red")
# s is a string that contains the badge data as an svg image.
print(s[:40])  # => <svg height="20" width="191.0" xmlns="ht

LOGO_URL = "https://raw.githubusercontent.com/pre-commit/pre-commit.github.io/real_master/favicon.ico"

