# -*- coding: UTF-8 -*-

from tethys_sdk.base import TethysAppBase, url_map_maker

# todo make the update button not ask for login every time (make it work on the server???)
# todo record demonstration videos

# todo OPTIONAL- improve the written instructions section
# todo OPTIONAL- create a persistent store of old reports and email/download/print option (header button)
# todo OPTIONAL- let the user toggle between elevations and depths on the historical charts
# todo OPTIONAL- add hydrologic factors to analysis like evaporation or infiltration?


class Embalses(TethysAppBase):
    """
    Tethys app class for Herramientas de Operaciones de los Embalses.
    """
    name = 'Administracion de los Embalses'
    index = 'embalses:home'
    icon = 'embalses/images/indrhi.png'
    package = 'embalses'
    root_url = 'embalses'
    color = '#01AEBF'
    description = 'Una aplicación para visualizar datos históricos y hacer simulaciones de elevaciones para los ' \
                  'embalses en la Republica Dominicana.'
    tags = 'reservoirs, hydrology, streamflow prediction'
    enable_feedback = False
    feedback_emails = []
    youtubelink = r'https://youtu.be/aWU-x75_g1U'    # link to the tutorials

    def url_maps(self):
        UrlMap = url_map_maker(self.root_url)

        url_maps = (

            # OVERVIEW PAGES
            UrlMap(
                name='home',
                url='embalses',
                controller='embalses.controllers.home'
            ),
            UrlMap(
                name='reportar',
                url='embalses/reportar',
                controller='embalses.controllers.reportar'
            ),
            UrlMap(
                name='instrucciones',
                url='embalses/instrucciones',
                controller='embalses.controllers.instructions'
            ),

            # SIMULATIONS PAGES
            UrlMap(
                name='simulations',
                url='embalses/simulaciones',
                controller='embalses.controllers.simulations'
            ),

            # RESERVOIR SPECIFIC PAGES
            UrlMap(                     # this is the controller for the page that shows reservoir specific stats
                name='template',        # {name} is an argument the controller needs to accept second
                url='embalses/{name}',
                controller='embalses.controllers.reservoirviewer'
            ),

            # CONTROLLERS FOR AJAX PAGES
            UrlMap(
                name='historicalchart',
                url='embalses/ajax/reshistplot',
                controller='embalses.ajax.reservoirhistoricalplot'
            ),
            UrlMap(
                name='storageplot',
                url='embalses/ajax/resstorageplot',
                controller='embalses.ajax.reservoirstorageplot'
            ),
            UrlMap(
                name='overview',
                url='embalses/ajax/overviewpage',
                controller='embalses.ajax.overviewpage'
            ),
            UrlMap(
                name='simulationtable',
                url='embalses/ajax/simulationTable',
                controller='embalses.ajax.simulationtable'
            ),
            UrlMap(
                name='getsfptflows',
                url='embalses/ajax/getSFPTflows',
                controller='embalses.ajax.getsfptflows'
            ),
            UrlMap(
                name='reservoirstatistics',
                url='embalses/ajax/reservoirstatistics',
                controller='embalses.ajax.reservoirstatistics'
            ),
            UrlMap(
                name='updatesheet',
                url='embalses/ajax/updatesheet',
                controller='embalses.ajax.updatesheet'
            ),
            UrlMap(
                name='performsimulation',
                url='embalses/ajax/performsimulation',
                controller='embalses.ajax.performsimulation'
            ),
        )

        return url_maps
