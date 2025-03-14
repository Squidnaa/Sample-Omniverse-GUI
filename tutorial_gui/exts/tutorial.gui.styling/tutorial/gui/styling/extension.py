import omni.ext
import omni.ui as ui
from .styles import StyleSheet

Style = StyleSheet


class TutorialGuiStylingExtension(omni.ext.IExt):
    
    def on_startup(self, ext_id):
        print("[tutorial.gui.styling] tutorial gui styling startup")

        self._count = 0

        self._window = ui.Window("My Window", width=300, height=300,
                                flags=ui.WINDOW_FLAGS_NO_COLLAPSE | ui.WINDOW_FLAGS_NO_RESIZE |
                                ui.WINDOW_FLAGS_NO_MOVE | ui.WINDOW_FLAGS_NO_CLOSE |
                                ui.WINDOW_FLAGS_NO_TITLE_BAR)
        self._window.frame.set_style(Style.my_window)
        with self._window.frame:
            with ui.VStack():
                with ui.ZStack():
                    ui.Rectangle(style=Style.custom_rectangle, height=125)
                    label = ui.Label("")
                    label.set_style(Style.my_label)


                def on_click():
                    self._count += 1
                    label.text = f"count: {self._count}"

                def on_reset():
                    self._count = 0
                    label.text = "empty"

                on_reset()

                with ui.HStack():
                    ui.Button("Add", clicked_fn=on_click, style=Style.add_button, height=100)
                    ui.Button("Reset", clicked_fn=on_reset, style=Style.reset_button, height=100)

    def on_shutdown(self):
        print("[tutorial.gui.styling] tutorial gui styling shutdown")
