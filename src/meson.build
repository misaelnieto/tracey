pkgdatadir = join_paths(
    get_option('prefix'), get_option('datadir'), meson.project_name()
)
moduledir = join_paths(pkgdatadir, 'tracey')
gnome = import('gnome')

gnome.compile_resources('tracey',
    'tracey.gresource.xml',
    gresource_bundle: true,
    install: true,
    install_dir: pkgdatadir,
)

python3 = import('python3')

conf = configuration_data()
conf.set('PYTHON', python3.find_python().path())
conf.set('VERSION', meson.project_version())
conf.set('pkgdatadir', pkgdatadir)

configure_file(
    input: 'tracey.in',
    output: 'tracey',
    configuration: conf,
    install: true,
    install_dir: get_option('bindir')
)

tracey_sources = [
    '__init__.py',
    'tracey_app.py',
    'parser.py',
]
install_data(tracey_sources, install_dir: moduledir)
