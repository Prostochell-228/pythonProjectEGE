a = "lazXBXHvqyx20WdbkazLmm5NOLiXSUIDHSj17Vnj3RKC7Dx5nRdhuy95bhqsouKPhZ0GpNNLBZdvprvTdklekKqH2GE6Ozvd3WKIi3JBL7kBgnRrFi97j5frmoUgtFvkHeLegHX6cXkiGtcT93tFt5WxeYdK1CAA4lbAjhPwvOQHSF48Optd9AS3t2YIsw68q9VvYK3vYS2hDgN40ed5c1iKbNEkFSxDLXipuNgmE2uZC5T9xYoHRVOzzIiRNJZO01SgZ9YAk6Y48UIX4WBveNLHMwqxmyKorQh3tGJrz7VxUZFBCI92z1W84Ak3fRcOGvGBQQB0lH0xqGmrpZbkv6gW51HRAfYjbbmX66ZW3yfC91DQIhLgtZz34KEktWD2miL2D8auOXPiZ1LVqVQWRBsUpEbzsS3ChaW7DvjxvnlLhmYjMVb4VaXQptaVP4tICmuyvTYULI0XfzmYrtwSwFeJRohtxyWlO0BFD6fop0NTFmnJJbsS3YA5zulC5SllQc8tM44Hs5OnokYdRVsslCHeznHCcqS4njH3ukqTpb94u5d0uOxEA541PmyB0FnxpD7G40SOQRRtQ4CPkH6ppkhd8s9FC0tUD7ciPQD36xA3Q1ACBzVEbRdFEQXc3XQutQrYahOwHVKettOARZ1pAMTCEMUpQ5Eq2CqvSIk0y0godoGZRNOCOA79QqyO3NbC70OMDRmLK50BKgxMmEhxb7hnEX4RPnhoXlS6TNz8P9EutXcIxih4b7cTrgAnArKepLS6q6vGwXhlQyxmUiPrlZgqQE2Dzdnx0YNOxaGHAPTiW9DG1nl4ccF2GXkvTGpIqgeYynfL3rYYiOKvS2yzcu0Eui0FEyAlaoyZJAtWdRmPKzplf2fd33r9h97GgyqdDkJH6PYenFVvhlLsMGcdNV5tQ0uswTYMk78NRuWPmeety56YQIf4Axm3ID4SFy06IdBEZt62EpomW0pSKkdYDJeF1z1iownkzrqjWRC1"
c = 0
v = 1
h = []
for i in range(len(a) - 1):
    v += 1
    if a[i] > a[i + 1]:
        c += 1
    else:
        h.append([c, v])
        c = 0
h.append([c, v])
print(max(h))
