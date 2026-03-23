import reflex as rx


def webhook_ls() -> rx.Component:
    # This is a webhook endpoint, not a page
    return rx.text("LemonSqueezy Webhook Endpoint")
