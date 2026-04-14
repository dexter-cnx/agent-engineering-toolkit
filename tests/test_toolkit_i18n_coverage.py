from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARCH_SRC = REPO_ROOT / "tools" / "toolkit-arch" / "src"
I18N_LIB = REPO_ROOT / "tools" / "toolkit-i18n" / "lib"

if str(ARCH_SRC) not in sys.path:
    sys.path.insert(0, str(ARCH_SRC))
if str(I18N_LIB) not in sys.path:
    sys.path.insert(0, str(I18N_LIB))

from toolkit_arch import cli as arch_cli  # noqa: E402
import toolkit_i18n as i18n_cli  # noqa: E402


class FeatureCoverageTests(unittest.TestCase):
    def test_zero_overlap_uses_real_key_intersection(self) -> None:
        defined = ["auth.login", "auth.logout"]
        used = ["auth.signin", "auth.signout"]

        arch_summary = arch_cli._summarize_feature_coverage(defined, used)
        i18n_summary = i18n_cli._feature_coverage_summary(defined, used)

        auth = arch_summary["by_feature"]["auth"]
        self.assertEqual(auth["defined_count"], 2)
        self.assertEqual(auth["used_count"], 2)
        self.assertEqual(auth["matched_count"], 0)
        self.assertEqual(auth["missing_count"], 2)
        self.assertEqual(auth["unused_count"], 2)
        self.assertEqual(auth["coverage_percent"], 0.0)

        auth = i18n_summary["auth"]
        self.assertEqual(auth["defined_count"], 2)
        self.assertEqual(auth["used_count"], 2)
        self.assertEqual(auth["matched_count"], 0)
        self.assertEqual(auth["missing_count"], 2)
        self.assertEqual(auth["unused_count"], 2)
        self.assertEqual(auth["coverage_percent"], 0.0)

    def test_partial_overlap_counts_only_shared_keys(self) -> None:
        defined = ["auth.login", "auth.logout", "auth.title"]
        used = ["auth.login", "auth.signout"]

        arch_summary = arch_cli._summarize_feature_coverage(defined, used)
        i18n_summary = i18n_cli._feature_coverage_summary(defined, used)

        auth = arch_summary["by_feature"]["auth"]
        self.assertEqual(auth["defined_count"], 3)
        self.assertEqual(auth["used_count"], 2)
        self.assertEqual(auth["matched_count"], 1)
        self.assertEqual(auth["missing_count"], 1)
        self.assertEqual(auth["unused_count"], 2)
        self.assertEqual(auth["coverage_percent"], 50.0)

        auth = i18n_summary["auth"]
        self.assertEqual(auth["defined_count"], 3)
        self.assertEqual(auth["used_count"], 2)
        self.assertEqual(auth["matched_count"], 1)
        self.assertEqual(auth["missing_count"], 1)
        self.assertEqual(auth["unused_count"], 2)
        self.assertEqual(auth["coverage_percent"], 50.0)

    def test_missing_translation_csv_raises_toolkit_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_csv = Path(tmpdir) / "missing.csv"

            with self.assertRaises(arch_cli.ToolkitError) as ctx:
                arch_cli._load_translation_keys(missing_csv)

        self.assertIn("translation csv not found", str(ctx.exception))
        self.assertNotIsInstance(ctx.exception, NameError)


if __name__ == "__main__":
    unittest.main()
