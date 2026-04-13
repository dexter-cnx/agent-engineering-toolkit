# Starter App: How to use

## 1. Create project shell

```bash
flutter create my_app
```

## 2. Copy starter files

Copy the contents of `starter-app-template/` into the new project.

## 3. Install packages

```bash
flutter pub get
```

## 4. Generate localization JSON if needed

```bash
python scripts/generate_l10n_from_csv.py
```

## 5. Run tests

```bash
flutter test
```

## 6. Start app

```bash
flutter run
```

## Included example flows

- Home dashboard
- Mock login flow
- Riverpod providers
- Clean-ish domain/data/presentation split
- Localization CSV source of truth
