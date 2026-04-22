# Implementation Checklist

- [ ] Logger interface lives in the app or core boundary
- [ ] Structured context model exists for feature, screen, request, or session fields
- [ ] Formatter is deterministic and covered by tests
- [ ] Redaction rules remove secrets and personal data
- [ ] Bootstrap wiring initializes the logger once
- [ ] Crash reporting or analytics integrations stay behind adapters
