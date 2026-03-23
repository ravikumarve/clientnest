import reflex as rx

config = rx.Config(
    app_name="clientnest",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)