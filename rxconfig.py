import reflex as rx

config = rx.Config(
    app_name="reflex_var",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)