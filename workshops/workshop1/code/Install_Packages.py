packages = [
'azureml',
'azureml.datadrift',

'pandas',
'mlflow',
'numpy',
'sklearn',
'joblib',
'requests',
'json',
]

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
        print('IMPORT SUCCESS: ', package)
    except ImportError:
        import pip
        print(package, ' NOT FOUND, installing...')
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

for p in packages:
    install_and_import(p)