# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

from datetime import datetime, timedelta


logger = logging.getLogger(__name__)

class MusicAlbum(models.Model):
    _name = 'music.album'
    _description = 'Álbum Musical'

    name = fields.Char('Album', required=True)
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
    album_id =  fields.Many2one('music.album', string='Álbum')
    date_release = fields.Date('Fecha de Lanzamiento')

    album_image = fields.Binary('Imagen del Álbum', related='album_id.album_image')
    
    @api.constrains('artist_ids')
    def _check_date_release(self):
        for record in self:
            artists = record.artist_ids
            for artist in artists:
                if record.date_release < artist.date_start:
                    raise models.ValidationError('¡El lanzamiento de la canción no pudo ser antes del comienzo del artista!')