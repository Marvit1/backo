# In a file like debug_toolbar_panels.py
from debug_toolbar.panels import Panel


class DRFPanel(Panel):
    """
    A debug toolbar panel to display information about DRF views.
    """
    def generate_stats(self, request, response):
        # Add any relevant statistics here
        pass

    def title(self):
        return 'DRF'
