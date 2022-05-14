# imports
from plyer import notification
import time

# variables
title = 'title'
message = "message"
toast = "toast"

# notifier
notification.notify(
    title=title,
    message=message,
    app_icon=None,
    timeout=8,
    toast=toast
)

# end_of_code
