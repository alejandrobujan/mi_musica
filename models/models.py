# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError
from odoo.tools.translate import _

from datetime import datetime, timedelta


logger = logging.getLogger(__name__)

class MusicAlbum(models.Model):
    _name = 'music.album'
    _description = 'Álbum Musical'

    name = fields.Char('Álbum', required=True)
    date_release = fields.Date('Fecha de Lanzamiento')
    album_image = fields.Binary('Carátula')
    artist_id = fields.Many2one('music.artist', string='Artista')
    track_ids = fields.One2many('music.track', string="Canciones", inverse_name='album_id')

class MusicGender(models.Model):
    _name = 'music.gender'
    _description = 'Género Musical'

    name = fields.Char('Género', required=True)
    description = fields.Text('Descripción')

class MusicArtist(models.Model):
    _name = 'music.artist'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Artista Musical'

    partner_id = fields.Many2one('res.partner', string='Artista', ondelete='cascade')
    member_image = fields.Binary('Imagen', related='partner_id.image')
    date_start = fields.Date('En activo desde')
    date_of_birth = fields.Date('Fecha de Nacimiento')

class MusicTrack(models.Model):
    _name = 'music.track'
    _description = 'Canción'

    name = fields.Char('Canción', required=True)
    gender_id = fields.Many2one('music.gender', string='Género')
    artist_ids = fields.Many2many('music.artist', string='Artistas')
    artist_names = fields.Char('Artistas',compute="get_artist_names")
    album_id =  fields.Many2one('music.album', string='Álbum')
    date_release = fields.Date('Fecha de Lanzamiento')
    
    url = fields.Char('Ruta a la canción')
    player = fields.Char('Reproducir', compute="make_player",default='')

    album_image = fields.Binary('Imagen del Álbum', related='album_id.album_image')

    @api.multi
    def get_artist_names(self):
        for record in self:
            if type(record.artist_ids) is not bool:
                record.artist_names = ""
                for artist in record.artist_ids:
                    record.artist_names += artist.partner_id.name
                    record.artist_names += ", "
                if type(record.artist_names) is not bool:
                    record.artist_names = record.artist_names[:-2]
            else:
                record.artist_names = "Desconocido"

    @api.multi
    def make_player(self):
        for record in self:
            if type(record.url) is not bool and len(record.url) != 0:
                record.player = "<audio controls=\"\"><source src=\""+str(record.url)+"\" type=\"audio/mpeg\" /></audio>"
            else:
                record.player = "<p>No se ha especificado la URL. Especifícala para mostrar el reproductor.</p>"
    
    @api.constrains('artist_ids')
    def _check_date_release(self):
        for record in self:
            artists = record.artist_ids
            for artist in artists:
                if type(artist.date_start) is not bool:
                    if record.date_release < artist.date_start:
                        raise models.ValidationError('¡El lanzamiento de la canción no pudo ser antes del comienzo del artista!')
                    

