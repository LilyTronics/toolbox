"""
Base view for all tools.
Make a subclass for each tool from this base view.
"""

import wx


class ViewBase(wx.Frame):

    def __init__(self, title, version):
        super().__init__(None, title=f"{title} - V{version}")
        self.panel = wx.Panel(self)


if __name__ == "__main__":

    class TestFrame(ViewBase):

        def __init__(self, title, version):
            super().__init__(title, version)


    app = wx.App(redirect=False)
    f = TestFrame("Test view", "9.99")
    f.Show()
    app.MainLoop()
