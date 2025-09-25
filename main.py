import flet as ft

dados = {
    "ministros": [],
    "escala": [],
    "repertorio": [],
    "agenda": [],
    "devocionais": []
}

def main(page: ft.Page):
    page.title = "Gestão de Ministério de Louvor"
    page.theme_mode = "light"
    page.padding = 0
    page.bgcolor = "#142136"

    def header(title, back_route=None):
        return ft.Container(
            content=ft.Row([
                ft.IconButton(icon="arrow_back", icon_color="white", on_click=lambda e: page.go(back_route)) if back_route else ft.Container(),
                ft.Text(title, size=28, weight="bold", color="white"),
            ], alignment="start"),
            padding=ft.padding.only(left=24, top=32, bottom=24),
            bgcolor="#142136",
            width=float("inf"),
        )

    def nav_tile(icon_name, label, route):
        return ft.ListTile(
            leading=ft.Icon(name=icon_name, color="#142136", size=32),
            title=ft.Text(label, size=22, weight="w500"),
            trailing=ft.Icon(name="chevron_right", color="#525252"),
            height=64,
            on_click=lambda e: page.go(route)
        )

    menu = ft.Container(
        content=ft.Column([
            ft.Container(nav_tile("person_outline", "Ministros", "/ministros"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("event", "Escala de Culto", "/escala"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("music_note", "Repertório Musical", "/repertorio"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("event_note", "Agenda de Ensaios", "/agenda"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("book_outlined", "Devocionais", "/devocionais"), bgcolor="white"),
        ]),
        padding=ft.padding.only(left=24, right=24, top=16),
        bgcolor="white",
        border_radius=ft.border_radius.only(bottom_left=36, bottom_right=36),
        expand=True
    )

    def card_view(titulo, chave, icon_name):
        cards = []
        for item in dados[chave]:
            cards.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Row([
                            ft.Icon(name=icon_name, size=40, color="#142136"),
                            ft.Text(item, size=18, weight="w500", expand=True),
                        ], alignment="start"),
                        padding=20,
                        bgcolor="#f5f5f5",
                        border_radius=12,
                        margin=ft.margin.only(bottom=10)
                    )
                )
            )

        botao = ft.ElevatedButton("Adicionar", icon="add", bgcolor="#142136", color="white", on_click=lambda e: page.go(f"/add_{chave}"))

        return ft.Container(
            content=ft.Column(
                [header(titulo, "/")] + cards + [botao],
                scroll="auto",
                alignment="start",
                horizontal_alignment="start",
                spacing=10
            ),
            padding=20
        )

    def form_view(titulo, chave, campos):
        inputs = [ft.TextField(label=campo, width=400) for campo in campos]

        def salvar(e):
            valores = [inp.value for inp in inputs if inp.value]
            if valores:
                dados[chave].append(" - ".join(valores))
                page.go(f"/{chave}")

        return ft.Container(
            content=ft.Column([
                header(f"Adicionar {titulo}", f"/{chave}"),
                *inputs,
                ft.ElevatedButton("Salvar", icon="save", bgcolor="#142136", color="white", on_click=salvar)
            ], alignment="center", horizontal_alignment="center", spacing=20),
            padding=20
        )

    def route_change(route):
        page.views.clear()
        views = {
            "/": ft.View("/", [header("Gestão de Ministério de Louvor"), menu]),
            "/ministros": ft.View("/ministros", [card_view("Ministros", "ministros", "person")]),
            "/escala": ft.View("/escala", [card_view("Escala de Culto", "escala", "event")]),
            "/repertorio": ft.View("/repertorio", [card_view("Repertório Musical", "repertorio", "music_note")]),
            "/agenda": ft.View("/agenda", [card_view("Agenda de Ensaios", "agenda", "event_note")]),
            "/devocionais": ft.View("/devocionais", [card_view("Devocionais", "devocionais", "book_outlined")]),
            "/add_ministros": ft.View("/add_ministros", [form_view("Ministro", "ministros", ["Nome", "Função", "Telefone", "E-mail"])]),
            "/add_escala": ft.View("/add_escala", [form_view("Escala de Culto", "escala", ["Data", "Ministro Responsável", "Músicas", "Observações"])]),
            "/add_repertorio": ft.View("/add_repertorio", [form_view("Música", "repertorio", ["Título", "Autor", "Tom", "Link", "Categoria"])]),
            "/add_agenda": ft.View("/add_agenda", [form_view("Ensaio", "agenda", ["Data", "Hora", "Local", "Responsável", "Observações"])]),
            "/add_devocionais": ft.View("/add_devocionais", [form_view("Devocional", "devocionais", ["Título", "Texto Bíblico", "Mensagem", "Link"])]),
        }
        page.views.append(views.get(route.route, ft.View(route.route, [header("Página não encontrada", "/")])))
        page.update()

    page.on_route_change = route_change
    page.go("/")

import flet as ft

dados = {
    "ministros": [],
    "escala": [],
    "repertorio": [],
    "agenda": [],
    "devocionais": []
}

def main(page: ft.Page):
    page.title = "Gestão de Ministério de Louvor"
    page.theme_mode = "light"
    page.padding = 0
    page.bgcolor = "#142136"

    def header(title, back_route=None):
        return ft.Container(
            content=ft.Row([
                ft.IconButton(icon="arrow_back", icon_color="white", on_click=lambda e: page.go(back_route)) if back_route else ft.Container(),
                ft.Text(title, size=28, weight="bold", color="white"),
            ], alignment="start"),
            padding=ft.padding.only(left=24, top=32, bottom=24),
            bgcolor="#142136",
            width=float("inf"),
        )

    def nav_tile(icon_name, label, route):
        return ft.ListTile(
            leading=ft.Icon(name=icon_name, color="#142136", size=32),
            title=ft.Text(label, size=22, weight="w500"),
            trailing=ft.Icon(name="chevron_right", color="#525252"),
            height=64,
            on_click=lambda e: page.go(route)
        )

    menu = ft.Container(
        content=ft.Column([
            ft.Container(nav_tile("person_outline", "Ministros", "/ministros"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("event", "Escala de Culto", "/escala"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("music_note", "Repertório Musical", "/repertorio"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("event_note", "Agenda de Ensaios", "/agenda"), bgcolor="white"),
            ft.Divider(height=1, color="#efefef"),
            ft.Container(nav_tile("book_outlined", "Devocionais", "/devocionais"), bgcolor="white"),
        ]),
        padding=ft.padding.only(left=24, right=24, top=16),
        bgcolor="white",
        border_radius=ft.border_radius.only(bottom_left=36, bottom_right=36),
        expand=True
    )

    def card_view(titulo, chave, icon_name):
        cards = []
        for item in dados[chave]:
            cards.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Row([
                            ft.Icon(name=icon_name, size=40, color="#142136"),
                            ft.Text(item, size=18, weight="w500", expand=True),
                        ], alignment="start"),
                        padding=20,
                        bgcolor="#f5f5f5",
                        border_radius=12,
                        margin=ft.margin.only(bottom=10)
                    )
                )
            )

        botao = ft.ElevatedButton("Adicionar", icon="add", bgcolor="#142136", color="white", on_click=lambda e: page.go(f"/add_{chave}"))

        return ft.Container(
            content=ft.Column(
                [header(titulo, "/")] + cards + [botao],
                scroll="auto",
                alignment="start",
                horizontal_alignment="start",
                spacing=10
            ),
            padding=20
        )

    def form_view(titulo, chave, campos):
        inputs = [ft.TextField(label=campo, width=400) for campo in campos]

        def salvar(e):
            valores = [inp.value for inp in inputs if inp.value]
            if valores:
                dados[chave].append(" - ".join(valores))
                page.go(f"/{chave}")

        return ft.Container(
            content=ft.Column([
                header(f"Adicionar {titulo}", f"/{chave}"),
                *inputs,
                ft.ElevatedButton("Salvar", icon="save", bgcolor="#142136", color="white", on_click=salvar)
            ], alignment="center", horizontal_alignment="center", spacing=20),
            padding=20
        )

    def route_change(route):
        page.views.clear()
        views = {
            "/": ft.View("/", [header("Gestão de Ministério de Louvor"), menu]),
            "/ministros": ft.View("/ministros", [card_view("Ministros", "ministros", "person")]),
            "/escala": ft.View("/escala", [card_view("Escala de Culto", "escala", "event")]),
            "/repertorio": ft.View("/repertorio", [card_view("Repertório Musical", "repertorio", "music_note")]),
            "/agenda": ft.View("/agenda", [card_view("Agenda de Ensaios", "agenda", "event_note")]),
            "/devocionais": ft.View("/devocionais", [card_view("Devocionais", "devocionais", "book_outlined")]),
            "/add_ministros": ft.View("/add_ministros", [form_view("Ministro", "ministros", ["Nome", "Função", "Telefone", "E-mail"])]),
            "/add_escala": ft.View("/add_escala", [form_view("Escala de Culto", "escala", ["Data", "Ministro Responsável", "Músicas", "Observações"])]),
            "/add_repertorio": ft.View("/add_repertorio", [form_view("Música", "repertorio", ["Título", "Autor", "Tom", "Link", "Categoria"])]),
            "/add_agenda": ft.View("/add_agenda", [form_view("Ensaio", "agenda", ["Data", "Hora", "Local", "Responsável", "Observações"])]),
            "/add_devocionais": ft.View("/add_devocionais", [form_view("Devocional", "devocionais", ["Título", "Texto Bíblico", "Mensagem", "Link"])]),
        }
        page.views.append(views.get(route.route, ft.View(route.route, [header("Página não encontrada", "/")])))
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main, view=ft.AppView.WEB_BROWSER)


