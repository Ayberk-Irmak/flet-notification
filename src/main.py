import flet as ft
import flet_permission_handler as fph
from notification import send_notification


def main(page: ft.Page):
    page.title = "Notification Example"

    ph = fph.PermissionHandler()
    page.overlay.append(ph)

    status_text = ft.Text("Notification Permission Status Unknown...", color=ft.Colors.GREY)

    notify_button = ft.ElevatedButton("Send Notification", disabled=True)

    def on_notify_click(e):
        title = " DFlet Notification"
        text = " This is a text Notification from ITAcademy"
        send_notification(title, text, status_text)
        page.update()
    
    notify_button.on_click = on_notify_click

    def check_permission(e):
        result = ph.check_permission(e.control.data)
        status_text.value = f"Permission Check. {e.control.data.name} - {result}"
        notify_button.disabled = not result
        status_text.color = ft.Colors.GREEN if result else ft.Colors.RED
        page.update()

    def request_permission(e):
        result = ph.request_permission(e.control.data)
        result_two = ph.request_permission(fph.PermissionType.ACCESS_NOTIFICATION_POLICY)
        status_text.value = f"Permission requested: {e.control.data.name} - {result}"
        notify_button.disabled = not result
        status_text.color = ft.Colors.GREEN if result else ft.Colors.RED
        page.update()


    page.add(
        ft.AppBar(title=ft.Text("Notification Permission Manager")),
        status_text,
        ft.OutlinedButton(
            "Check Notification Permission",
            data= fph.PermissionType.NOTIFICATION,
            on_click=check_permission,
        ),
        ft.OutlinedButton(
            "Request Notification Permission",
            data= fph.PermissionType.NOTIFICATION,
            on_click=request_permission
        ),
        notify_button
    )


ft.app(main)
