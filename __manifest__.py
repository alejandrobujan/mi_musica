# -*- coding: utf-8 -*-
{
    'name': "Mi Musica",
    'summary': """Gestiona canciones, artistas y álbumes.""",
    'description': """Módulo para la gestión de música. Trabaja con canciones, artistas y álbumes. Desarrollado para el módulo de SXE en IES San Clemente en 2020.""",
    'author': "Alejandro Buján",
    'website': "https://github.com/alejandrobujan/mi_musica",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/music_album.xml',
        'views/music_artist.xml',
        'views/music_track.xml'
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
