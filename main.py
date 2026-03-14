import flet as ft

def main(page: ft.Page):
    # رێکخستنا لاپەڕەی (وەکی مۆبایل)
    page.title = "Kurd Cinema"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0f0f0f" # ڕەشەکێ جوان
    page.padding = 20
    page.scroll = "auto"

    # لایێ سەرێ ئەپی (AppBar)
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MOVIE_FILTER, color="red"),
        title=ft.Text("KURD CINEMA", weight="bold", color="red"),
        bgcolor="#1a1a1a",
        center_title=True,
    )

    # فەنکشن بۆ دەمێ کلیک ل فلمی دهێتە کرن
    def movie_clicked(e, title):
        page.snack_bar = ft.SnackBar(ft.Text(f"دێ فلمێ ({title}) بۆ تە ڤەبیت..."))
        page.snack_bar.open = True
        page.update()

    # دروستکرنا کارتێ فلمی
    def create_movie_card(title, img_url, year):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=img_url, width=160, height=230, fit="cover", border_radius=10),
                ft.Text(title, weight="bold", size=14, overflow="ellipsis"),
                ft.Text(year, size=12, color="grey"),
            ]),
            padding=10,
            on_click=lambda e: movie_clicked(e, title),
            hover_color="#222222",
        )

    # لیستا فلمان (نموونە)
    movies_row = ft.Row(
        scroll="always",
        controls=[
            create_movie_card("Interstellar", "https://image.tmdb.org/t/p/w500/gEU2vRpyfsV61TzogOSsyIsu9s9.jpg", "2014"),
            create_movie_card("Inception", "https://image.tmdb.org/t/p/w500/o0I0BhptrJy7UrPhpsjTe6p9QvV.jpg", "2010"),
            create_movie_card("The Batman", "https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onun.jpg", "2022"),
            create_movie_card("John Wick", "https://image.tmdb.org/t/p/w500/fzcmQj9R9pqs6CDv78NfnG7uSfk.jpg", "2014"),
        ]
    )

    # دابەشکرنا بەشان
    page.add(
        ft.Text("فلمێن نوو", size=22, weight="bold"),
        movies_row,
        ft.Divider(height=30, color="transparent"),
        ft.Text("پێشنیارێن بۆ تە", size=22, weight="bold"),
        ft.ResponsiveRow([
            ft.Column(col={"sm": 6, "md": 4}, controls=[create_movie_card("Spiderman", "https://image.tmdb.org/t/p/w500/1g0mZsswsyCKGvS32ZpZnyyzJ4L.jpg", "2021")]),
            ft.Column(col={"sm": 6, "md": 4}, controls=[create_movie_card("Joker", "https://image.tmdb.org/t/p/w500/udDclKVUZv6qXM7D0lsT3m3nj3H.jpg", "2019")]),
        ])
    )

# کارپێکرنا ئەپی
ft.app(target=main)
