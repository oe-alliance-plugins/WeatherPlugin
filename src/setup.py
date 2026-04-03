from setuptools import setup
import setup_translate

pkg = 'Extensions.WeatherPlugin'
setup(name='enigma2-plugin-extensions-weatherplugin',
       version='3.0',
       description='E2 Weather Plugin',
       package_dir={pkg: 'WeatherPlugin'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'weather.png', 'icons/*.gif', 'icons/www.google.com']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
