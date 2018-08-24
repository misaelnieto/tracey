# Desktop file
desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
    test(
        'Validate desktop file',
        desktop_utils, args: ['org.devsim.Tracey.desktop.in']
    )
endif

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
    test(
        'Validate appstream file',
        appstream_util,
        args: ['validate', 'org.devsim.Tracey.appdata.xml.in']
    )
endif

install_data('org.devsim.Tracey.gschema.xml',
    install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
    test(
        'Validate schema file', compile_schemas,
        args: ['--strict', '--dry-run', meson.current_source_dir()]
    )
endif

