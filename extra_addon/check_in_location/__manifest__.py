# -*- encoding: utf-8 -*-
{
    'name': "Attendances Checkin Location",
    'version': '3.0',
    'summary': 'Check-in with location.',
    'category': 'Human Resources/Attendances',
    'description': """Check-in with location.""",
    "depends": ['web', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'views/attendance_location.xml',
        'data/attendance_location_data.xml',
    ],
    "assets": {
        'web.assets_backend': [
            '/check_in_location/static/src/scss/my_attendances.scss',
            '/check_in_location/static/src/js/my_attendances.js',
        ],
        'web.assets_qweb': {
            '/check_in_location/static/src/xml/my_attendances.xml',
        },
    },
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    # Author
    'author': 'Leuwint Technologies',
    'website': 'https://www.leuwint.com/',
    'maintainer': 'Leuwint Technologies',
    
    'installable': True,
    'application'   : True,
    'auto_install'  : False,
}
