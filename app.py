import flet as ft


def main(page: ft.Page):
    ft.Window.bgcolor = ft.colors.BLACK87
    contain = ft.Container(padding=10)
    
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    page.update()
    
    #bt = ft.ElevatedButton(on_click=pick_files())
    
    #page.add(contain(bt))
    
    page.update()
if __name__ == "__main__":
    ft.app(target=main)
    