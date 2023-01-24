class Dashboard(object):
    ship_type = "div[class*='MuiSelect-root']"
    weight = "html > body > div > section > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div > input"
    home_port = "html > body > div > section > div > div > div:nth-of-type(1) > div:nth-of-type(3) > div > div > input"
    search = "button"
    results_table = "tbody[class='MuiTableBody-root']"
    invalid_search = "div[class='MuiAlert-message']"
