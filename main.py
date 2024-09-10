import flet as ft


def main(page: ft.Page):
    page.title = 'File Helper'
    page.theme_mode = 'dark'
    
    page.add(
        ft.Row(
            [
                ft.TextButton(text="File"),
                ft.TextButton(text="Edit"),
                ft.TextButton(text="Help")
            ]
        ),
        ft.Row(
            [
                ft.Column(
                    [
                        ft.TextButton(icon=ft.icons.SORT_ROUNDED, text="Sorter"),
                        ft.TextButton(icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE_ROUNDED, text="Renamer"),
                        ft.TextButton(icon=ft.icons.CHANGE_CIRCLE_ROUNDED, text="Converter"),
                    ]
                )
                
            ]
        )
    )
    
ft.app(target=main)