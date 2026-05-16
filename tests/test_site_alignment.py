from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text()


class SiteAlignmentTest(unittest.TestCase):
    def test_footer_links_bel_air_intel_and_cain_union_without_replacing_mainframe_positioning(self):
        self.assertRegex(HTML, r'<a[^>]+href="https://belairintel\.com"[^>]*>Bel Air Intel</a>')
        self.assertRegex(HTML, r'<a[^>]+href="https://cainunion\.com"[^>]*>Cain Union</a>')
        self.assertIn("Mainframe Studio", HTML)
        self.assertIn("growth", HTML.lower())

    def test_mainframe_is_framed_as_growth_layer_not_parent_control_plane(self):
        self.assertIn("public growth layer", HTML.lower())
        self.assertIn("Bel Air Intel", HTML)
        self.assertIn("architect", HTML.lower())


if __name__ == "__main__":
    unittest.main()
